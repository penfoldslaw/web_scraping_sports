from data_functions import his_player_defense_data, current_player_defense_data, build_data_path
import pandas as pd
import numpy as np
from IPython.display import display

def his_usage_team(player_names: dict, date_list: list, usage_path,player_base_path,defense_base_path):
    current_player_dic = {}

    for player, team in player_names.items():
        current_player_frames =[]

        for date in date_list:
            usage_path =build_data_path(usage_path,date=date)
            usage_data = pd.read_csv(usage_path)

            #merging player and defense dat into one
            merged_data, current_defense_df = his_player_defense_data(player_base_path,defense_base_path,player,date)

            #adding season to usage_data
            usage_data['season'] = date

            #Getting the player usage percentage for usage data and adding to merge
            player_usage = usage_data.loc[usage_data['Player'] == player, 'USG%'].values[0]
            merged_data['USG'] = player_usage

            #adding the current player team pace
            team_stat = current_defense_df.loc[current_defense_df['TEAM'] == team, 'PACE'].values[0]
            merged_data["team_pace"] = team_stat

            # adding current player team OffRtg
            team_offrtg = current_defense_df.loc[current_defense_df['TEAM'] == team, 'OffRtg'].values[0]
            merged_data["team_offrtg"] = team_offrtg

            team_poss = current_defense_df.loc[current_defense_df['TEAM'] == team, 'POSS'].values[0]
            merged_data["team_poss"] = team_poss
            
            # Exclude rows where the TEAM column matches the given team
            merged_data = merged_data[merged_data['TEAM'] != team]


            # merged_data = merged_data[['season','Date', 'Home/Away_game' ,'Matchup' ,'PTS','MIN_x', 'Team', 'TEAM', 'FGA', 'USG', 'DefRtg', 'PACE','team_pace']]

            # Turn date into seconds
            merged_data['Date_in_Seconds'] = pd.to_datetime(merged_data['Date']).astype('int64') // 10**9
            merged_data = merged_data.sort_values(by="Date_in_Seconds")


            # Turn Home/Away game into 1 and 0
            merged_data['home_away'] = merged_data['Home/Away_game'].apply(lambda x: 1 if x == 'Away' else 0)
            # Dropping duplicates
            merged_data = merged_data.drop_duplicates()
            
            # Append the DataFrame for this date to the player's list
            current_player_frames.append(merged_data)

        # Combine all dates for the current player into one DataFrame
        current_player_dic[player] = pd.concat(current_player_frames, ignore_index=True)


    return current_player_dic, current_defense_df


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
   

            

            

            

            



            
