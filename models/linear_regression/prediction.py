from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
from sklearn.preprocessing import StandardScaler
import pandas
from feature_function import his_usage_team, select_features
from data_functions import his_player_defense_data, current_player_defense_data, build_data_path
import pandas as pd
import numpy as np
from IPython.display import display




import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

def prediction(player_names: dict, date_list: list, usage_path, player_base_path, defense_base_path, schedule_base_path, selected_feature_target, prediction_target):
    """
    Predicts future data for NBA players using historical data and rolling averages.

    Parameters:
        player_names (dict): Dictionary mapping player names to their respective teams.
        date_list (list): List of dates to consider for analysis.
        usage_path (str): Path to player usage data.
        player_base_path (str): Path to player statistics data.
        defense_base_path (str): Path to team defense statistics.
        schedule_base_path (str): Path to team schedules.
        selected_feature_target (str): Target feature for selecting model input features.
        prediction_target (str): The feature to be predicted (e.g., FGA).

    Returns:
        pd.DataFrame: A DataFrame containing predicted values and RMSE for each player.
    """
    fga_prediction_data, df_defense = his_usage_team(player_names, date_list, usage_path, player_base_path, defense_base_path)
    fga_prediction_results = {}

    # Select the best features for each player
    feature_dic = select_features(player_names, date_list, usage_path, player_base_path, defense_base_path, selected_feature_target)

    for player, team in player_names.items():
        # Load schedule data for the player's team
        schedule_path = build_data_path(schedule_base_path, schedule_team=team)
        schedule_df = pd.read_csv(schedule_path)

        # Retrieve player-specific prediction data
        df = fga_prediction_data[player]
        features = feature_dic[player] 
        target = prediction_target

        # Split data into training and testing sets based on a timestamp
        timestamp = int(pd.Timestamp('2024-12-31').timestamp())
        train_data = df[df['Date_in_Seconds'] < timestamp]
        test_data = df[df['Date_in_Seconds'] >= timestamp]

        X_train = train_data[features].fillna(0)
        y_train = train_data[target].fillna(0)
        X_test = test_data[features].fillna(0)
        y_test = test_data[target].fillna(0) 

        # Train linear regression model
        model = LinearRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        # Calculate error metrics
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)

        print(f"{player}, MAE: {mae}, RMSE: {rmse}")

        # Compute exponentially weighted moving average (EWMA) for minutes played
        alpha = 0.2
        df['EWMA_MIN'] = df['MIN_x'].ewm(span=(2/alpha - 1), adjust=False).mean()
        last_actual = df['MIN_x'].iloc[-1]
        last_smoothed = df['EWMA_MIN'].iloc[-1]
        next_value = alpha * last_actual + (1 - alpha) * last_smoothed
        next_value = round(next_value, 2)

        # Define feature exclusion lists
        exclude_features = ['RANK', 'OffRtg', 'W', 'L', 'DefRtg', 'NetRtg', 'AST%', 'AST/TO', 'ASTRatio',
                            'OREB%', 'DREB%', 'REB%', 'TOV%', 'eFG%', 'TS%', 'PACE', 'POSS', 'TEAM', 'PIE']
        exclude_features_schedule = ['home_away', 'schedule_team', 'DATE', 'location', 'season_defense']

        # Convert schedule dates to timestamp format
        schedule_df['Date_in_Seconds'] = pd.to_datetime(schedule_df['DATE']).astype('int64') // 10**9
        schedule_df['home_away'] = schedule_df['location'].apply(lambda x: 1 if x == 'away' else 0)

        # Extract defensive stats for the scheduled team
        last_season = df_defense["season_defense"].iloc[-1]
        df_for_schedule = df_defense.loc[df_defense["season_defense"] == last_season, exclude_features]
        first_team = schedule_df['schedule_team'].iloc[0]
        schedule_team_result = schedule_df.loc[schedule_df['schedule_team'] == first_team, 'schedule_team'].values[0]
        schedule_values = {feature: df_for_schedule.loc[df_for_schedule['TEAM'] == schedule_team_result, feature].values[0] 
                           for feature in exclude_features if feature in df_for_schedule.columns}
        
 
        print(schedule_values)  # Debugging: Ensure schedule values are correctly retrieved

        # Extract rolling average features
        rolling_features = [col for col in features if col not in exclude_features]
        for col in rolling_features:
            df[f'{col}'] = df[col].rolling(window=20).mean().fillna(0).astype(int)
        df_last_rolling = df.iloc[[-1]][[f'{col}' for col in rolling_features]].reset_index(drop=True)

        # Update rolling feature set with scheduled team values
        for value in features:
            if value in exclude_features:
                df_last_rolling[value] = schedule_values.get(value)
        for value in features:
            if value in exclude_features_schedule:
                df_last_rolling[value] = schedule_df[value].iloc[0]

        # Ensure feature order is consistent with model input
        df_last_rolling = df_last_rolling.reindex(columns=features)
        X_future = df_last_rolling
        display(X_future)  # Debugging: Display final feature set for prediction

        # Make future predictions
        future_predictions = model.predict(X_future).astype('int')
        fga_prediction_results[player] = [future_predictions[0].round(1), rmse]

        # Format results into a DataFrame
        df_results = pd.DataFrame.from_dict(fga_prediction_results, orient='index', columns=[target, 'RMSE'])
        df_results.reset_index(inplace=True)
        df_results.rename(columns={'index': 'Player'}, inplace=True)

    return df_results



if __name__ == "__main__":
    raise ImportError("This script is intended to be imported as a module, not executed directly.")


# player_names =  {
#     "Devin Booker": "PHX",
#     "Anthony Edwards": "MIN",
#     "Kevin Durant": "PHX",
#     "Naz Reid": "MIN",
#     "Julius Randle": "MIN",
#     "Bradley Beal": "PHX",
#     "Bol Bol": "PHX",
#     "Donte DiVincenzo": "MIN",
#     "Jaden McDaniels": "MIN",
#     "Nick Richards": "PHX",
#     "Mike Conley": "MIN"
# }

# date_list = ["2022-23","2023-24","2024-25"]
# usage_path = "D:/nba_usage_csv_historic/usage_csv_{date}/{date}_content.csv"
# schedule_base_path = "D:/nba_scheduled_csv/schedule_csv_2025/{schedule_team}_schedule_content.csv"
# player_base_path = "D:/nba_player_csv_historic/season_{date}/all_quarters/{player}_content.csv"
# defense_base_path = "D:/nba_defense_history_csv/defense_csv_{date}/all_quarter_defense_content.csv"

# results = prediction(player_names, date_list, usage_path, player_base_path, defense_base_path, schedule_base_path,'PTS','PTS')

# display(results)