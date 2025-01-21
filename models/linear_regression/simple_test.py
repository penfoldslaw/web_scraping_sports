import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from IPython.display import display
import os
import datetime
from datetime import datetime

date_list = ['2024-25']
player_name = ['Jayson Tatum', 'Devin Booker', 'Trae Young']
schedule_team = ['BOS', 'PHX', 'ATL']
player_team_mapping = {
    'Nikola Vucevic':'CHI','Norman Powell':'LAC','James Harden': 'LAC', 'Giannis Antetokounmpo': 'MIL', 'Kawhi Leonard': 'LAC', 'Luka Doncic': 'DAL', 'LeBron James': 'LAL', 
    'Damian Lillard': 'MIL', 'Karl-Anthony Towns': 'NYK', 'Trae Young': 'ATL', 'Anthony Davis': 'LAL', 'Russell Westbrook': 'DEN',
    'Bradley Beal': 'PHX', 'Kyrie Irving': 'DAL', 'Nikola Jokic': 'DEN', 'Devin Booker': 'PHX', 'Joel Embiid': 'PHI',
    'John Collins': 'UTAH', 'Domantas Sabonis': 'SAC', 'Andre Drummond': 'PHI', 'Nikola Vucevic': 'CHI', 'DeMar DeRozan': 'SAC',
    'Jusuf Nurkic': 'PHX', 'Zach LaVine': 'CHI', 'Ben Simmons': 'BKN', 'Brandon Ingram': 'NO', 'Jayson Tatum': 'BOS',
    'Jimmy Butler': 'MIA', 'Pascal Siakam': 'IND', 'DAngelo Russell': 'GSW', 'Deandre Ayton': 'POR', 'Kyle Lowry': 'CHA',
    'Bam Adebayo': 'MIA', 'Stephen Curry': 'GSW', 'Khris Middleton': 'MIL', 'Kristaps Porzingis': 'BOS', 'Donovan Mitchell': 'CLE',
    'Rudy Gobert': 'MIN', 'DeAaron Fox': 'SAC', 'Jrue Holiday': 'BOS', 'Paul George': 'LAC', 'Chris Paul': 'GSW',
    'CJ McCollum': 'NO', 'Clint Capela': 'ATL', 'Zion Williamson': 'NO', 'Julius Randle': 'NYK',
    'Andrew Wiggins': 'GSW', 'Tobias Harris': 'PHI', 'Kevin Love': 'MIA', 'Spencer Dinwiddie': 'DAL'
}


player_dataframes = {}  # Dictionary to store each player's DataFrame
schedule_team_dataframes = {}  # Dictionary to store each team's DataFrame

for player, schedule_team in player_team_mapping.items():
    single_player_df = pd.DataFrame()
    defense_df = pd.DataFrame()
    schedule_df = pd.DataFrame()

    for date in date_list:


        if os.path.exists(path) and os.path.exists(path_defense):
            # Player data
            season_df_player = pd.read_csv(path)
            season_df_player['season'] = date
            single_player_df = pd.concat([single_player_df, season_df_player], ignore_index=True).drop_duplicates()

            # Defense data
            defense_df_season = pd.read_csv(path_defense)
            defense_df_season['season_defense'] = date
            defense_df = pd.concat([defense_df, defense_df_season], ignore_index=True).drop_duplicates()

            # Schedule data
            season_df_schedule = pd.read_csv(path_schedule)
            season_df_schedule['season_schedule'] = date
            schedule_df = pd.concat([schedule_df, season_df_schedule], ignore_index=True).drop_duplicates()

        else:
            print(f'{date} not found either for {player} or defense')

        # Add the player's DataFrame to the dictionary 
    pd.set_option('display.max_rows', 1000)  # Maximum number of rows to display
    pd.set_option('display.max_columns', None)  # Show all columns
    pd.set_option('display.width', 1000)  # Adjust column width for better readability
    
    player_dataframes[player] = single_player_df
    schedule_team_dataframes[schedule_team] = schedule_df


    expected_columns = ['TEAM', 'DefRtg', 'season_defense']

    if all(col in defense_df.columns for col in expected_columns):
        df_defense = defense_df[expected_columns].drop_duplicates()
    else:
        print(f"Missing {expected_columns} columns in {player} dataframe, skipping this file.")

    #df_defense = defense_df[['TEAM', 'DefRtg', 'season_defense']].drop_duplicates()  # Keep only relevant columns
    #defense_df = defense_df[['TEAM', 'DefRtg', 'season_defense']].drop_duplicates()


    # Merge player and defense data
    merged_df = pd.merge(
        player_dataframes[player], df_defense,
        how='inner',
        left_on=['Away', 'season'],  # Match on Away team and season
        right_on=['TEAM', 'season_defense']
    ).reset_index(drop=True)

    #display(merged_df.head(10))  # Display the first 10 rows of the merged DataFrame

     # Merge player and schedule data
    merged_df_one = pd.merge(
        player_dataframes[player], schedule_team_dataframes[schedule_team],
        how='inner',
        left_on='Team',
        right_on='home_team'
    ).drop_duplicates().reset_index(drop=True)

    df_unique = merged_df_one.drop_duplicates(subset=["Date", "DATE"], keep="first")  # Deduplicate based on "Date" column

    # Get the current date
    current_date = datetime.now()

    # Ensure the 'Date' column is in datetime format
    df_unique['DATE'] = pd.to_datetime(df_unique['DATE'])

    # Calculate the absolute difference but preserve the original column
    df_unique['Date_Diff'] = abs(df_unique['DATE'] - current_date)

    # # Find the row with the closest date
    # closest_date_row = df_unique.loc[df_unique['Date_Diff'].idxmin()]  # Row with the closest date

    if not df_unique['Date_Diff'].empty:
        # Find the row with the closest date
        closest_date_row = df_unique.loc[df_unique['Date_Diff'].idxmin()]  # Row with the closest date
        print("Closest date:", closest_date_row['DATE'])
        # print("Closest row details:\n", closest_date_row)
    else:
        print(f"No valid dates to compare {player} check players Team in map as a start")

    print("Closest date:", closest_date_row['DATE'], closest_date_row['schedule_team'])

    # Ensure Date is a datetime type and sort by date
    merged_df['Date'] = pd.to_datetime(merged_df['Date'])
    merged_df = merged_df.sort_values(by="Date").reset_index(drop=True)
    # Turn Home/Away_game into a binary indicator or 1 for Home and 0 for Away
    merged_df['is_home_game'] = (merged_df['Home/Away_game'] == 'Home').astype(int)

    #display(merged_df.head(10))  # Display the first 10 rows of the merged DataFrame

    # Filter for recent games (last 10 games)
    recent_games = 10
    merged_df = merged_df.tail(recent_games).reset_index(drop=True)


    # Rolling averages for FGA, FG%, and FTA
    rolling_windows = [3, 5, 10]
    for stat in ['FGA', 'FG%', 'FTA']:
        for window in rolling_windows:
            merged_df[f'{stat}_rolling_{window}'] =  (merged_df[stat].rolling(window).mean().round(1))

    #display(merged_df.head(10))  # Display the first 10 rows of the merged DataFrame


    # Prepare features and target for prediction
    X = merged_df[['FGA_rolling_3', 'FGA_rolling_5', 'FG%_rolling_3', 'is_home_game', 'DefRtg']]
    y_fga = merged_df['FGA']  # Target for FGA prediction
    y_fg_percentage = merged_df['FG%']  # Target for FG% prediction
    y_fta = merged_df['FTA']  # Target for FTA prediction

    # Train-test split (chronological split)
    train_size = int(0.8 * len(merged_df))
    X_train, X_test = X[:train_size], X[train_size:]
    y_fga_train, y_fga_test = y_fga[:train_size], y_fga[train_size:]
    y_fg_percentage_train, y_fg_percentage_test = y_fg_percentage[:train_size], y_fg_percentage[train_size:]
    y_fta_train, y_fta_test = y_fta[:train_size], y_fta[train_size:]


    # Initialize RandomForest models for FGA, FG%, and FTA prediction
    model_fga = RandomForestRegressor(n_estimators=100, random_state=42)
    model_fg_percentage = RandomForestRegressor(n_estimators=100, random_state=42)
    model_fta = RandomForestRegressor(n_estimators=100, random_state=42)


    # Train the models
    model_fga.fit(X_train, y_fga_train)
    model_fg_percentage.fit(X_train, y_fg_percentage_train)
    model_fta.fit(X_train, y_fta_train)

    # Make predictions
    y_fga_pred = model_fga.predict(X_test)
    y_fg_percentage_pred = model_fg_percentage.predict(X_test)
    y_fta_pred = model_fta.predict(X_test)


    # Evaluate the models
    mae_fga = mean_absolute_error(y_fga_test, y_fga_pred)
    rmse_fga = np.sqrt(mean_squared_error(y_fga_test, y_fga_pred))
    r2_fga = r2_score(y_fga_test, y_fga_pred)


    mae_fg_percentage = mean_absolute_error(y_fg_percentage_test, y_fg_percentage_pred)
    rmse_fg_percentage = np.sqrt(mean_squared_error(y_fg_percentage_test, y_fg_percentage_pred))
    r2_fg_percentage = r2_score(y_fg_percentage_test, y_fg_percentage_pred)

    mae_fta = mean_absolute_error(y_fta_test, y_fta_pred)
    rmse_fta = np.sqrt(mean_squared_error(y_fta_test, y_fta_pred))
    r2_fta = r2_score(y_fta_test, y_fta_pred)

    # Display the evaluation metrics
    print(f"FGA Model Evaluation: MAE: {mae_fga}, RMSE: {rmse_fga}, R²: {r2_fga}")
    print(f"FG% Model Evaluation: MAE: {mae_fg_percentage}, RMSE: {rmse_fg_percentage}, R²: {r2_fg_percentage}")
    print(f"FTA Model Evaluation: MAE: {mae_fta}, RMSE: {rmse_fta}, R²: {r2_fta}")

    # Get the most recent game data for prediction of the upcoming game
    latest_game = merged_df.iloc[-1]

    # display(latest_game)

    # Filter for a specific team (e.g., 'TeamX') 
    opponent = closest_date_row['schedule_team']
    df_opponent = df_defense[df_defense['TEAM'] == opponent]

    # If opponent team exists in the defense data, get their defensive rating
    if not df_opponent.empty:
        opponent_defense_rating = df_opponent['DefRtg'].values[0]
    else:
        print(f"Opponent {opponent} not found in defense data!")
        opponent_defense_rating = 110  # Use a default value (or handle it differently)

    # Use the rolling averages for the most recent game
    upcoming_game_features = pd.DataFrame({
        'FGA_rolling_3': [latest_game['FGA_rolling_3']],
        'FGA_rolling_5': [latest_game['FGA_rolling_5']],
        'FG%_rolling_3': [latest_game['FG%_rolling_3']],
        'is_home_game': [latest_game['is_home_game']],
        'DefRtg': [opponent_defense_rating]  # Use the opponent's defensive rating
    })

    # Predict for upcoming game
    predicted_fga = model_fga.predict(upcoming_game_features)
    predicted_fg_percentage = model_fg_percentage.predict(upcoming_game_features)
    predicted_fta = model_fta.predict(upcoming_game_features)

    print(f"################### upcoming feature stats for {player} ########################################")

    print(f"Predicted FGA for upcoming game against {opponent}: {predicted_fga[0]}")
    print(f"Predicted FG% for upcoming game against {opponent}: {predicted_fg_percentage[0]}")
    print(f"Predicted FTA for upcoming game against {opponent}: {predicted_fta[0]}")

    print("###########################################################################")



    

