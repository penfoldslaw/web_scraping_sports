from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
from sklearn.preprocessing import StandardScaler
import pandas
from feature_function import select_features
from data_functions import his_player_defense_data, current_player_defense_data, build_data_path, his_usage_team
import pandas as pd
import numpy as np
from IPython.display import display
import sys
from datetime import datetime
import os
import logging



import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from scipy.stats import linregress


def prediction(player_names: dict, date_list: list, stats_path: dict, player_base_path, defense_base_path, schedule_base_path ,selected_feature_target, prediction_target):
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



    fga_prediction_data, df_defense = his_usage_team(player_names, date_list, stats_path, player_base_path, defense_base_path)
    fga_prediction_results = {}

    # Select the best features for each player
    feature_dic = select_features(player_names, date_list, stats_path, player_base_path, defense_base_path, selected_feature_target)

    for player, team in player_names.items():
        # Load schedule data for the player's team
        schedule_path = build_data_path(schedule_base_path, schedule_team=team)
        schedule_df = pd.read_csv(schedule_path)

        # Retrieve player-specific prediction data
        df = fga_prediction_data.get(player)

        if df is None:
            print(f"Skipping {player} - No data available.")
            continue  # Move to the next player


        # Convert schedule dates to timestamp format
        schedule_df['Date_in_Seconds'] = pd.to_datetime(schedule_df['DATE']).astype('int64') // 10**9
        # schedule_df['home_away'] = schedule_df['location'].apply(lambda x: 1 if x == 'away' else 0)
        schedule_df['home_away'] = schedule_df['home_team'].apply(lambda x: 1 if x == team else 0)


        # first_team = schedule_df['schedule_team'].iloc[0]

        column_with_team = schedule_df.columns[(schedule_df == team).any()].tolist()

        # If the team is found in a column, retrieve the opposing team (example for 'away_team')
        if column_with_team:
            print(f"{team} found in column(s): {column_with_team}")
            # Example: Get the opposing team from another column (e.g., 'away_team')
            row_index = schedule_df[schedule_df[column_with_team[0]] == team].index[0]
            check_player_team_column = column_with_team[0]  # Adjust this to the correct column name for the opposing team
            if check_player_team_column == 'schedule_team':
                for_opposing_team = 'home_team'
            
            if check_player_team_column == 'home_team':
                for_opposing_team = 'schedule_team'

            opposing_team = schedule_df.loc[row_index, for_opposing_team]  # Adjust this to the correct column name for the opposing team
            print(f"The opposing team for {team} is: {opposing_team}")
        else:
            print(f"{team} not found in the DataFrame.")

        first_team = opposing_team


        # this is for getting the last row of the team the player played against so it can be used to predict what comes next
        filtered_df = df[df['Away'] == first_team]
        

        last_5_games = df.tail(10)

        # Retrieve the selected features for the current player from the feature dictionary.
        # If the player is not found in feature_dic, return an empty list instead of None to avoid errors.
        features = feature_dic.get(player, [])



        # some players can't connect to the his_usage datatframe well I don't why
        features = [feature for feature in features if feature in df.columns]
        
        # If no valid features remain, print a message and skip the player.
        if not features:
            print(f"No valid features found for {player} for predicting {prediction_target}")
            continue



        target = prediction_target

        # print(f"Available columns for {player}: {df.columns.tolist()}")
        # print(f"Selected features for {player}: {features}")

        # Split data into training and testing sets based on a timestamp
        timestamp = int(pd.Timestamp('2025-02-10').timestamp())
        train_data = df#[df['Date_in_Seconds'] < timestamp]
        test_data = df#[df['Date_in_Seconds'] >= timestamp]


        train_data_chose = df[df['Date_in_Seconds'] < timestamp]
        test_data_chose = df[df['Date_in_Seconds'] >= timestamp]

        
        X_train_chose = train_data_chose[features].fillna(0)
        y_train_chose = train_data_chose[target].fillna(0)
        X_test_chose = test_data_chose[features].fillna(0)
        y_test_chose = test_data_chose[target].fillna(0) 



        X_train = train_data[features].fillna(0)
        y_train = train_data[target].fillna(0)
        X_test = test_data[features].fillna(0)
        y_test = test_data[target].fillna(0) 

        # display(X_train.head(1))
        # print(f"X_train shape: {X_train.shape}")
        # print(f"y_train shape: {y_train.shape}")
        # print(X_train.head())  # View first few rows
        # print(y_train.head())  # View first few rows

        # print(features)  # Check selected feature names
        # print(X_train.columns)  # See available columns


        if not features:  # If feature_columns is an empty list
            print(f"Skipping training: No selected {target} features.")
            sys.exit(1) 



        # Train linear regression model
        model = LinearRegression()
        model.fit(X_train, y_train)

        if X_train_chose.empty or y_train_chose.empty:
            print(f"[WARNING] No training data for feature '{selected_feature_target}'. Skipping.")
            # return pd.DataFrame()  # or return None, or a dummy result
            continue

        if X_test_chose.empty or y_test_chose.empty:
            print(f"[WARNING] No testing data for feature '{selected_feature_target}'. Skipping.")
            continue

        # train model  with test to see who to choose
        model_chose = LinearRegression()
        model_chose.fit(X_train_chose, y_train_chose)


        y_pred_chose = model_chose.predict(X_test_chose)
        # Calculate error metrics
        mae_chose = mean_absolute_error(y_test_chose, y_pred_chose)
        mse_chose = mean_squared_error(y_test_chose, y_pred_chose)
        rmse_chose = np.sqrt(mse_chose)

        # Make sure predictions and actual test values are in a DataFrame

        results_df = pd.DataFrame({
            'Actual': y_test_chose,
            'Predicted': y_pred_chose
        })

        # Show the first few rows of the DataFrame to compare
        print(results_df.head())



        # print(f"{player}, MAE: {mae_chose}, RMSE: {rmse_chose}")


        # y_pred = model.predict(X_test)

        # Calculate error metrics
        # mae = mean_absolute_error(y_test, y_pred)
        # mse = mean_squared_error(y_test, y_pred)
        # rmse = np.sqrt(mse)

        # print(f"{player}, MAE: {mae}, RMSE: {rmse}")

        # Define feature exclusion lists
        exclude_features = ['RANK', 'OffRtg', 'W', 'L', 'DefRtg', 'NetRtg', 'AST%', 'AST/TO', 'ASTRatio',
                            'OREB%', 'DREB%', 'REB%', 'TOV%', 'eFG%', 'TS%', 'PACE', 'POSS', 'TEAM', 'PIE']
        exclude_features_schedule = ['home_away', 'schedule_team', 'DATE', 'location', 'season_defense']

        # Convert schedule dates to timestamp format
        schedule_df['Date_in_Seconds'] = pd.to_datetime(schedule_df['DATE']).astype('int64') // 10**9
        # schedule_df['home_away'] = schedule_df['location'].apply(lambda x: 1 if x == 'away' else 0)
        schedule_df['home_away'] = schedule_df['home_team'].apply(lambda x: 1 if x != team else 0)


        # Extract defensive stats for the scheduled team
        last_season = df_defense["season_defense"].iloc[-1]
        df_for_schedule = df_defense.loc[df_defense["season_defense"] == last_season, exclude_features]
        first_team = opposing_team
        # schedule_team_result = schedule_df.loc[schedule_df['schedule_team'] == first_team, 'schedule_team'].values[0]
        schedule_team_result = schedule_df.loc[schedule_df[for_opposing_team] == first_team, for_opposing_team].values[0]
        schedule_values = {feature: df_for_schedule.loc[df_for_schedule['TEAM'] == schedule_team_result, feature].values[0] 
                           for feature in exclude_features if feature in df_for_schedule.columns}
        
 
        # print(schedule_values)  # Debugging: Ensure schedule values are correctly retrieved

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




        # display(last_5_games)

        combined_df_recent_team_played = pd.concat([last_5_games,filtered_df])

        combined_df_recent_team_played = combined_df_recent_team_played[features]

        combined_df_recent_team_played = combined_df_recent_team_played.reset_index(drop=True)


        # display(combined_df_recent_team_played)

        # Define the rolling window size (e.g., 3 for the last 3 games)
        window_size = 2

        # Apply rolling average for each feature (adjust the columns as needed)
        rolling_avg_df = combined_df_recent_team_played.rolling(window=window_size, min_periods=1).mean()

        # Reset index to align with original DataFrame if necessary
        rolling_avg_df = rolling_avg_df.reset_index(drop=True)

        rolling_avg_df_use = rolling_avg_df.iloc[[-1]]


        combined_df_recent_team_played_r = pd.concat([filtered_df,last_5_games])

        combined_df_recent_team_played_r = combined_df_recent_team_played_r[features]

        combined_df_recent_team_played_r = combined_df_recent_team_played_r.reset_index(drop=True)


        rolling_avg_df_use_r = combined_df_recent_team_played_r.iloc[[-1]]







        # display(X_future.head(10))
        # Step 1: Calculate mean and standard deviation of the target variable (PTS, REB, etc.)
        mean_target = y_train.mean()
        std_target = y_train.std()

        # Step 2: Define reasonable bounds (e.g., within 3 standard deviations)
        lower_bound = mean_target - 3 * std_target
        upper_bound = mean_target + 3 * std_target

        

        # future predictions happens here
        # future_predictions = model.predict(X_future) #rolling_avg_df_use
        # future_predictions_last_game = model.predict(rolling_avg_df_use)
        # future_predictions_last_game_r = model.predict(rolling_avg_df_use_r)
        # ensemble_predictions = np.mean([future_predictions,future_predictions_last_game,future_predictions_last_game_r ], axis=0)

        predictions =[]

        # X_future
        if not X_future.empty:
            try:
                future_predictions = model.predict(X_future)[0]
                if not np.isnan(future_predictions):
                    predictions.append(future_predictions)
            except Exception as e:
                print(f"Error predicting for {player}: {e}")
        

        # rolling_avg_df_use
        if not rolling_avg_df_use.empty:
            try:
                future_predictions_last_game = model.predict(rolling_avg_df_use)[0]
                if not np.isnan(future_predictions_last_game):
                    predictions.append(future_predictions_last_game)
            except Exception as e:
                print(f"Error predicting for {player}: {e}")
        
        # rolling_avg_df_use_r
        if not rolling_avg_df_use_r.empty:
            try:
                future_predictions_last_game_r = model.predict(rolling_avg_df_use_r)[0]
                if not np.isnan(future_predictions_last_game_r):
                    predictions.append(future_predictions_last_game_r)
            except Exception as e:
                print(f"Error predicting for {player}: {e}")

        # Final handling of predictions
        if not predictions:
            print(f"No valid predictions for {player}.")
            return []
        
        #clip prediction
        ensemble_predictions = np.mean(predictions, axis=0)
        future_predictions = np.clip(ensemble_predictions, lower_bound, upper_bound).astype('int')



        # creating rolling mean average
        df[f"Rolling_Mean_{target}"] = df[target].rolling(window=20).mean()
        df[f"Rolling_Std_{target}"] = df[target].rolling(window=20).std()
        df[f"Rolling_CV_{target}"] = df[f"Rolling_Std_{target}"] / df[f"Rolling_Mean_{target}"]

        rounded_future_prediction = abs(future_predictions)

        # print(player)
        # display(X_future.head(10))
        # print(player, target, rounded_future_prediction)
        # display(df[[f"Rolling_CV_{target}"]].tail(1))

        if pd.isna(df[f"Rolling_CV_{target}"].iloc[-1]) or np.isinf(df[f"Rolling_CV_{target}"].iloc[-1]):
            df.loc[df.index[-1], f"Rolling_CV_{target}"] = 0

        rolling_cv = df[f"Rolling_CV_{target}"].iloc[-1]
        highest_cv_seen = df[f"Rolling_CV_{target}"].max()

        cv_fluctuate = rolling_cv * rounded_future_prediction

        if cv_fluctuate > rounded_future_prediction:
            cv_low_prediction = abs(cv_fluctuate - rounded_future_prediction)

        # cv_low_prediction = abs(rounded_future_prediction- cv_fluctuate)
        # cv_high_prediction = rounded_future_prediction + cv_fluctuate



        # player_prediction = f"{cv_low_prediction.astype('int')} - {rounded_future_prediction} - {cv_high_prediction.astype('int')}"

        cv_low_prediction = abs(rounded_future_prediction - cv_fluctuate)
        cv_high_prediction = rounded_future_prediction + cv_fluctuate

        # Convert to integers
        cv_low_prediction = cv_low_prediction.astype(int)
        cv_high_prediction = cv_high_prediction.astype(int)
        rounded_future_prediction = rounded_future_prediction.astype(int)

        # Apply the logic to modify cv_low_prediction
        if cv_low_prediction == 0 and rounded_future_prediction == 0 and cv_high_prediction == 0:
            cv_low_prediction = 0  # Set to 0 if all are 0
        elif cv_low_prediction > 0:
            pass  # Keep cv_low_prediction as is if it's already greater than 0
        else:
            cv_low_prediction = 1  # Otherwise, set to 1

        # Construct the player prediction string
        player_prediction = f"{cv_low_prediction} - {rounded_future_prediction} - {cv_high_prediction}"


        

        if rolling_cv > 1:
            confidence_score = max(0, 1 - (rolling_cv / highest_cv_seen))
        else:
            confidence_score = 1 - rolling_cv  # More stability → Higher confidence

        confidence_score_percentage = round(confidence_score * 100, 2)


        lower_bound, upper_bound = cv_low_prediction, rounded_future_prediction




        from scipy.stats import norm

        # CONFIG: Toggle to use z-score
        use_z_score = True  # Set to False if you only want ±1 std range
        confidence = 0.95    # Confidence level if using z-score (e.g., 95%)

        # 1. Rolling calculations
        df[f"Rolling_Mean_{target}"] = df[target].rolling(window=20).mean()
        df[f"Rolling_Std_{target}"] = df[target].rolling(window=20).std()
        df[f"Rolling_CV_{target}"] = df[f"Rolling_Std_{target}"] / df[f"Rolling_Mean_{target}"]

        # 2. Handle NaN or inf values
        if pd.isna(df[f"Rolling_Std_{target}"].iloc[-1]) or np.isinf(df[f"Rolling_Std_{target}"].iloc[-1]):
            df.loc[df.index[-1], f"Rolling_Std_{target}"] = 0

        if pd.isna(df[f"Rolling_CV_{target}"].iloc[-1]) or np.isinf(df[f"Rolling_CV_{target}"].iloc[-1]):
            df.loc[df.index[-1], f"Rolling_CV_{target}"] = 0

        # 3. Prediction + volatility
        rounded_future_prediction = abs(future_predictions)
        rolling_std = df[f"Rolling_Std_{target}"].iloc[-1]
        rolling_cv = df[f"Rolling_CV_{target}"].iloc[-1]
        highest_cv_seen = df[f"Rolling_CV_{target}"].max()

        # 4. Calculate bounds using std or z * std
        if use_z_score:
            z = norm.ppf(1 - (1 - confidence) / 2)
            conf_low = rounded_future_prediction - z * rolling_std
            conf_high = rounded_future_prediction + z * rolling_std
        else:
            conf_low = rounded_future_prediction - rolling_std
            conf_high = rounded_future_prediction + rolling_std

        # 5. Convert to integers & clip lower bound
        conf_low = max(0, int(conf_low))
        conf_high = int(conf_high)
        rounded_future_prediction = int(rounded_future_prediction)

        # 6. Build prediction string
        player_prediction = f"{conf_low} - {rounded_future_prediction} - {conf_high}"


        

        if rolling_cv > 1:
            confidence_score = max(0, 1 - (rolling_cv / highest_cv_seen))
        else:
            confidence_score = 1 - rolling_cv  # More stability → Higher confidence

        confidence_score_percentage = round(confidence_score * 100, 2)


        lower_bound, upper_bound = cv_low_prediction, rounded_future_prediction


        if target == 'FGA':
            target = 'PTS'

        # trend_df = df[target].tail(10).tolist()
        trend_df = df[target].tail(10).tolist()[::-1]



        fga_prediction_results[player] = [team,player_prediction,confidence_score_percentage,trend_df, rmse_chose]

        
        
        df_results = pd.DataFrame.from_dict(fga_prediction_results, orient='index', columns=['team',target,f'cv-1_{target}' ,f'recentgames_{target}',f'rmse_{target}'])
        # Reset index and rename it properly
        df_results.reset_index(inplace=True)
        df_results.rename(columns={'index': 'Player'}, inplace=True)
        today_date = datetime.today().strftime('%Y-%m-%d')
        #create a directory if one doesn't exist
        directory = f'D:/prediction_output/{target}_outputs'
        os.makedirs(directory, exist_ok=True)    
        df_results.to_csv(f'{directory}/{target}_output_{today_date}.csv', index=False)
        # display(df_results)

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