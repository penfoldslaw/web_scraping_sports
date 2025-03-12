from data_functions import his_player_defense_data, current_player_defense_data, build_data_path, his_usage_team
import pandas as pd
import numpy as np
from IPython.display import display
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Lasso
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np



def fga_prediction(player_names: dict, date_list: list, usage_path, player_base_path, defense_base_path, schedule_base_path):
    fga_prediction_data, df_defense = his_usage_team(player_names, date_list, usage_path, player_base_path, defense_base_path)
    fga_prediction_results = {}

    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.metrics import mean_squared_error
    from sklearn.model_selection import cross_val_score
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_absolute_error, mean_squared_error
    import numpy as np



    for player, team in player_names.items():
        # Get schedule data for the player's team
        schedule_path = build_data_path(schedule_base_path, schedule_team=team)
        schedule_df = pd.read_csv(schedule_path)
        
        # Get player-specific prediction data
        df = fga_prediction_data[player]
        
        # Model training and prediction code
        features = ['PACE', 'team_pace', 'USG', 'DefRtg', 'MIN_x', 'home_away', 'Date_in_Seconds', 'OffRtg', 'team_offrtg']
        target = 'FGA'

        timestamp = int(pd.Timestamp('2024-12-31').timestamp())
        train_data = df[df['Date_in_Seconds'] < timestamp]
        test_data = df[df['Date_in_Seconds'] >= timestamp]

        X_train = train_data[features]
        y_train = train_data[target]
        X_test = test_data[features]
        y_test = test_data[target]

        model = LinearRegression()
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)


        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)

        print(f"{player}, MAE: {mae}, RMSE: {rmse}")

        # EWMA calculation for minutes
        alpha = 0.2
        df['EWMA_MIN'] = df['MIN_x'].ewm(span=(2/alpha - 1), adjust=False).mean()
        last_actual = df['MIN_x'].iloc[-1]
        last_smoothed = df['EWMA_MIN'].iloc[-1]
        next_value = alpha * last_actual + (1 - alpha) * last_smoothed
        next_value = round(next_value, 2)

        # Get defensive stats for the scheduled team
        last_season = df_defense["season_defense"].iloc[-1]
        df_for_schedule = df_defense.loc[df_defense["season_defense"] == last_season, ['TEAM', 'PACE', 'DefRtg', 'OffRtg']]

        first_team = schedule_df['schedule_team'].iloc[0]
        schedule_team_result = schedule_df.loc[schedule_df['schedule_team'] == first_team, 'schedule_team'].values[0]
        schedule_defrtg = df_for_schedule.loc[df_for_schedule['TEAM'] == schedule_team_result, 'DefRtg'].values[0]
        schedule_pace = df_for_schedule.loc[df_for_schedule['TEAM'] == schedule_team_result, 'PACE'].values[0]
        schedule_offrtg = df_for_schedule.loc[df_for_schedule['TEAM'] == schedule_team_result, 'OffRtg'].values[0]

        # Convert schedule dates to seconds
        schedule_df['Date_in_Seconds'] = pd.to_datetime(schedule_df['DATE']).astype('int64') // 10**9
        schedule_df['home_away'] = schedule_df['location'].apply(lambda x: 1 if x == 'away' else 0)

        # Create future prediction dataframe
        X_future = pd.DataFrame({
            'PACE': [schedule_pace],
            'team_pace': [df['team_pace'].iloc[-1]],
            'USG': [df['USG'].iloc[-1]],
            'DefRtg': [schedule_defrtg],
            'MIN_x': [next_value],
            'home_away': [schedule_df['home_away'].iloc[0]],
            'Date_in_Seconds': [schedule_df['Date_in_Seconds'].iloc[0]],
            'OffRtg': [df['OffRtg'].iloc[-1]],
            'team_offrtg': [schedule_offrtg]
        })

        future_predictions = model.predict(X_future)
        fga_prediction_results[player] = future_predictions[0].round(1)

    return fga_prediction_results




# def select_features(player_names, date_list, stats_path, player_base_path, defense_base_path, target):
#     player_df, _ = his_usage_team(player_names, date_list, stats_path, player_base_path, defense_base_path)
    
#     selected_features_dict = {}
    
#     max_features_player = None
#     max_features = 0

#     for player, df in player_df.items():
#         df_X = df.drop(columns=[target,'Date','Matchup','Team','Home/Away_game','W/L', 'Away', 'season', 'TEAM', 'season_defense'])
        
#         scaler = StandardScaler()
#         X = scaler.fit_transform(df_X)
#         y = df[target]  # Target variable
        
#         # Grid search parameters for Lasso
#         param_grid = {'alpha': [0.001, 0.01, 0.1, 1, 10]}
#         grid_search = GridSearchCV(Lasso(), param_grid, cv=5, scoring='r2')
#         grid_search.fit(X, y)
        
#         # Get the best alpha and fit Lasso
#         best_alpha = grid_search.best_params_['alpha']
#         best_lasso = Lasso(alpha=best_alpha)
#         best_lasso.fit(X, y)
        
#         # Select non-zero coefficient features
#         X = pd.DataFrame(X, columns=df_X.columns)
#         selected_features = X.columns[best_lasso.coef_ != 0].tolist()
        
#         # Store selected features
#         selected_features_dict[player] = selected_features
        
#         # Track the player with the most features
#         if len(selected_features) > max_features:
#             max_features = len(selected_features)
#             max_features_player = player

#     # If a player has no selected features, assign the features of the player with the most features
#     for player in selected_features_dict:
#         if not selected_features_dict[player]:  # If empty
#             selected_features_dict[player] = selected_features_dict.get(max_features_player, [])

#     return selected_features_dict


def select_features(player_names, date_list, usage_path, player_base_path, defense_base_path, target):
    player_df, _ = his_usage_team(player_names, date_list, usage_path, player_base_path, defense_base_path)
    
    selected_features_dict = {}
    
    max_features_player = None
    max_features = 0

    for player, df in player_df.items():
        df_X = df.drop(columns=[target, 'Date', 'Matchup', 'Team', 'Home/Away_game', 'W/L', 'Away', 'season', 'TEAM', 'season_defense'])
        
        # Apply StandardScaler to scale the features
        scaler = StandardScaler()
        X = scaler.fit_transform(df_X)
        y = df[target]  # Target variable
        
        # Grid search parameters for Lasso
        param_grid = {'alpha': [0.001, 0.01, 0.1, 1, 10]}
        
        # Use GridSearchCV to find the best alpha
        grid_search = GridSearchCV(Lasso(max_iter=5000000000), param_grid, cv=5, scoring='r2')  # Increase max_iter here
        grid_search.fit(X, y)
        
        # Get the best alpha and fit Lasso
        best_alpha = grid_search.best_params_['alpha']
        best_lasso = Lasso(alpha=best_alpha, max_iter=5000000000)  # Ensure enough iterations for convergence
        best_lasso.fit(X, y)
        
        # Select non-zero coefficient features
        X = pd.DataFrame(X, columns=df_X.columns)
        selected_features = X.columns[best_lasso.coef_ != 0].tolist()
        
        # Store selected features
        selected_features_dict[player] = selected_features
        
        # Track the player with the most features
        if len(selected_features) > max_features:
            max_features = len(selected_features)
            max_features_player = player

    # If a player has no selected features, assign the features of the player with the most features
    for player in selected_features_dict:
        if not selected_features_dict[player]:  # If empty
            selected_features_dict[player] = selected_features_dict.get(max_features_player, [])

    return selected_features_dict



if __name__ == "__main__":
    raise ImportError("This script is intended to be imported as a module, not executed directly.")


# player_names = { 'Alex Caruso':'OKC', 'Isaiah Hartenstein':'OKC', 'Shai Gilgeous-Alexander':'OKC'}
# date_list = ["2022-23","2023-24","2024-25"]
# usage_path = "D:/nba_usage_csv_historic/usage_csv_{date}/{date}_content.csv"
# schedule_base_path = "D:/nba_scheduled_csv/schedule_csv_2025/{schedule_team}_schedule_content.csv"
# player_base_path = "D:/nba_player_csv_historic/season_{date}/all_quarters/{player}_content.csv"
# defense_base_path = "D:/nba_defense_history_csv/defense_csv_{date}/all_quarter_defense_content.csv"

# results = fga_prediction(player_names, date_list, usage_path, player_base_path, defense_base_path, schedule_base_path)


# for player, fga_predictions in results.items():
#     print(fga_predictions)



#example of how to use select_features
# player_names = {
#     "Jayson Tatum": "BOS",
#     # "Nikola Jokic": "DEN",
#     "Jamal Murray": "DEN",
#     "Jaylen Brown": "BOS",
#     "Derrick White": "BOS",
#     "Payton Pritchard": "BOS",
#     "Michael Porter Jr.": "DEN",
#     "Russell Westbrook": "DEN",
#     "Christian Braun": "DEN",
#     "Al Horford": "BOS",
#     # "Julian Strawther": "DEN",
#     "Sam Hauser": "BOS",
#     "Zeke Nnaji": "DEN",
#     "Luke Kornet": "BOS"
# }
# date_list = ["2022-23","2023-24","2024-25"]
# usage_path = "D:/nba_usage_csv_historic/usage_csv_{date}/{date}_content.csv"
# schedule_base_path = "D:/nba_scheduled_csv/schedule_csv_2025/{schedule_team}_schedule_content.csv"
# player_base_path = "D:/nba_player_csv_historic/season_{date}/all_quarters/{player}_content.csv"
# defense_base_path = "D:/nba_defense_history_csv/defense_csv_{date}/all_quarter_defense_content.csv"


# feature_dic = select_features(player_names, date_list, usage_path, player_base_path, defense_base_path,'PTS')

# for player, features in feature_dic.items():
#     # print(player)
#     features = feature_dic[player] 
#     print(player,':',features)
   

            

            

            

            



            
