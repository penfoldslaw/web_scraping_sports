import requests
import pandas as pd
from unidecode import unidecode
import os
from IPython.display import display
from unidecode import unidecode



def tracking_scrape(measuretype, season, seasontype, csv_folder_path):

    url = "https://stats.nba.com/stats/leaguedashptstats"

    params = {
        "College": "",
        "Conference": "",
        "Country": "",
        "DateFrom": "",
        "DateTo": "",
        "Division": "",
        "DraftPick": "",
        "DraftYear": "",
        "GameScope": "",
        "Height": "",
        "ISTRound": "",
        "LastNGames": "0",
        "LeagueID": "00",
        "Location": "",
        "Month": "0",
        "OpponentTeamID": "0",
        "Outcome": "",
        "PORound": "0",
        "PerMode": "PerGame",
        "PlayerExperience": "",
        "PlayerOrTeam": "Player",
        "PlayerPosition": "",
        "PtMeasureType":  measuretype,      #"PostTouch",  # You can also use: Passing, Defense, Rebounding, etc.
        "Season": season,  #"2024-25",
        "SeasonSegment": "",
        "SeasonType":  seasontype , #"Regular Season",
        "StarterBench": "",
        "TeamID": "0",
        "VsConference": "",
        "VsDivision": "",
        "Weight": ""
    }

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://www.nba.com/stats/",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Host": "stats.nba.com",
        "Origin": "https://www.nba.com"
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    # Convert to DataFrame
    df = pd.DataFrame(data["resultSets"][0]["rowSet"], columns=data["resultSets"][0]["headers"])
    # print(df.columns)

    for measure in params.items():
        if measure[0] == "PtMeasureType":
            measure_type = measure[1]


    if measure_type == "CatchShoot":
        rename_map = {
        'PLAYER_NAME': 'PLAYER',
        'TEAM_ABBREVIATION': 'TEAM',
        'GP': 'GP',
        'MIN': 'MIN',
        'CATCH_SHOOT_PTS': 'PTS',
        'CATCH_SHOOT_FGM': 'FGM',
        'CATCH_SHOOT_FGA': 'FGA',
        'CATCH_SHOOT_FG_PCT': 'FG%',
        'CATCH_SHOOT_FG3M': '3PM',
        'CATCH_SHOOT_FG3A': '3PA',
        'CATCH_SHOOT_FG3_PCT': '3P%',
        'CATCH_SHOOT_EFG_PCT': 'eFG%'}

        df = df.rename(columns=rename_map)

        df = df[['PLAYER', 'TEAM', 'GP', 'MIN', 'PTS', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'eFG%']]

        float_columns = [
            'MIN',  'PTS', 'FGM', 'FGA', 
            'FG%', '3PM', 'eFG%', '3PA', '3P%']
        
        int_columns = ['GP']
        df[int_columns] = df[int_columns].astype(int)
        df[float_columns] = df[float_columns].replace('-', 0).astype(float)
        df[float_columns] = df[float_columns].fillna(0)
        df['PLAYER'] = df['PLAYER'].apply(unidecode)

        df.columns = [col + '_catch_shoot' for col in df.columns]


            
        #save to csv
        file_path_csv = csv_folder_path
        path = file_path_csv
        csv_path = path
        os.makedirs(csv_path, exist_ok=True)
        df.to_csv(f"{csv_path}/catch_shoot_content.csv", index=False)
        display(df)


    if measure_type == "Drives":
        rename_map = {
        'PLAYER_NAME': 'PLAYER',
        'TEAM_ABBREVIATION': 'TEAM',
        'GP': 'GP',
        'W': 'W',
        'L': 'L',
        'MIN': 'MIN',
        'DRIVES': 'DRIVES',
        'DRIVE_FGM': 'FGM',
        'DRIVE_FGA': 'FGA',
        'DRIVE_FG_PCT': 'FG%',
        'DRIVE_FTM': 'FTM',
        'DRIVE_FTA': 'FTA',
        'DRIVE_FT_PCT': 'FT%',
        'DRIVE_PTS': 'PTS',
        'DRIVE_PTS_PCT': 'PTS%',
        'DRIVE_PASSES': 'PASS',
        'DRIVE_PASSES_PCT': 'PASS%',
        'DRIVE_AST': 'AST',
        'DRIVE_AST_PCT': 'AST%',
        'DRIVE_TOV': 'TO',
        'DRIVE_TOV_PCT': 'TOV%',
        'DRIVE_PF': 'PF',
        'DRIVE_PF_PCT': 'PF%'}


        df = df.rename(columns=rename_map)[list(rename_map.values())]


        df = df.rename(columns={'AST\xa0PTSCreated': 'ASTPTSCreated'})
        int_columns = ['GP', 'W', 'L']
        float_columns = [
            'MIN', 'DRIVES', 'FGM', 'FGA', 'FG%', 'FTM', 'FTA', 'FT%', 'PTS', 'PTS%', 'PASS', 'PASS%', 'AST', 'AST%', 'TO', 'TOV%', 'PF', 'PF%']

        df[int_columns] = df[int_columns].replace('-', 0).astype(int)
        df[float_columns] = df[float_columns].replace('-', 0).astype(float)
        df[float_columns] = df[float_columns].fillna(0)

        df['PLAYER'] = df['PLAYER'].apply(unidecode)

        df.columns = [col + '_drive' for col in df.columns]




        #save to csv
        file_path_csv = csv_folder_path #f"nba_tracking/tracking_csv_2024-25"
        path = file_path_csv
        csv_path = path
        os.makedirs(csv_path, exist_ok=True)
        df.to_csv(f"{csv_path}/drives_content.csv", index=False) # "D:\nba_tracking_data_csv\nba_csv_2024-25\drives_content.csv"
        display(df)



    if measure_type == "ElbowTouch":
        rename_map = {
        'PLAYER_NAME': 'PLAYER',
        'TEAM_ABBREVIATION': 'TEAM',
        'GP': 'GP',
        'W': 'W',
        'L': 'L',
        'MIN': 'MIN',
        'TOUCHES': 'Touches',
        'ELBOW_TOUCHES': 'ElbowTouches',
        'ELBOW_TOUCH_FGM': 'FGM',
        'ELBOW_TOUCH_FGA': 'FGA',
        'ELBOW_TOUCH_FG_PCT': 'FG%',
        'ELBOW_TOUCH_FTM': 'FTM',
        'ELBOW_TOUCH_FTA': 'FTA',
        'ELBOW_TOUCH_FT_PCT': 'FT%',
        'ELBOW_TOUCH_PTS': 'PTS',
        'ELBOW_TOUCH_PTS_PCT': 'PTS%',
        'ELBOW_TOUCH_PASSES': 'PASS',
        'ELBOW_TOUCH_PASSES_PCT': 'PASS%',
        'ELBOW_TOUCH_AST': 'AST',
        'ELBOW_TOUCH_AST_PCT': 'AST%',
        'ELBOW_TOUCH_TOV': 'TO',
        'ELBOW_TOUCH_TOV_PCT': 'TOV%',
        'ELBOW_TOUCH_FOULS': 'PF',
        'ELBOW_TOUCH_FOULS_PCT': 'PF%'}

        df = df.rename(columns=rename_map)[list(rename_map.values())]


        int_columns = ['GP', 'W', 'L']
        float_columns = [
            'MIN', 'Touches', 'ElbowTouches', 'FGM', 'FGA', 'FG%', 'FTM', 'FTA', 'FT%', 'PTS', 'PTS%', 'PASS', 'PASS%', 'AST', 'AST%', 'TO', 'TOV%', 'PF', 'PF%']

        df[int_columns] = df[int_columns].replace('-', 0).astype(int)
        df[float_columns] = df[float_columns].replace('-', 0).astype(float)
        df[float_columns] = df[float_columns].fillna(0)
        df['PLAYER'] = df['PLAYER'].apply(unidecode)

        df.columns = [col + '_elbow' for col in df.columns]


        
        # #save to csv
        file_path_csv = csv_folder_path #f"nba_tracking/tracking_csv_2024-25"
        path = file_path_csv
        csv_path = path
        os.makedirs(csv_path, exist_ok=True)
        df.to_csv(f"{csv_path}/elbow_touch_content.csv", index=False) # "D:\nba_tracking_data_csv\nba_csv_2024-25\elbow_touch_content.csv"

        display(df)


    if measure_type == "PaintTouch":
        rename_map = {
        'PLAYER_NAME': 'PLAYER',
        'TEAM_ABBREVIATION': 'TEAM',
        'GP': 'GP',
        'W': 'W',
        'L': 'L',
        'MIN': 'MIN',
        'TOUCHES': 'Touches',
        'PAINT_TOUCHES': 'PaintTouches',
        'PAINT_TOUCH_FGM': 'FGM',
        'PAINT_TOUCH_FGA': 'FGA',
        'PAINT_TOUCH_FG_PCT': 'FG%',
        'PAINT_TOUCH_FTM': 'FTM',
        'PAINT_TOUCH_FTA': 'FTA',
        'PAINT_TOUCH_FT_PCT': 'FT%',
        'PAINT_TOUCH_PTS': 'PTS',
        'PAINT_TOUCH_PTS_PCT': 'PTS%',
        'PAINT_TOUCH_PASSES': 'Pass',
        'PAINT_TOUCH_PASSES_PCT': 'Pass%',
        'PAINT_TOUCH_AST': 'AST',
        'PAINT_TOUCH_AST_PCT': 'AST%',
        'PAINT_TOUCH_TOV': 'TO',
        'PAINT_TOUCH_TOV_PCT': 'TOV%',
        'PAINT_TOUCH_FOULS': 'PF',
        'PAINT_TOUCH_FOULS_PCT': 'PF%'}

        df = df.rename(columns=rename_map)[list(rename_map.values())]

        # df = df.rename(columns={'AST\xa0PTSCreated': 'ASTPTSCreated'})
        int_columns = ['GP', 'W', 'L']
        float_columns = [
            'MIN', 'Touches', 'PaintTouches', 'FGM', 'FGA', 'FG%', 'FTM', 'FTA', 'FT%', 'PTS', 'PTS%', 'Pass', 'Pass%', 'AST', 'AST%', 'TO', 'TOV%', 'PF', 'PF%']

        df[int_columns] = df[int_columns].replace('-', 0).astype(int)
        df[float_columns] = df[float_columns].replace('-', 0).astype(float)
        df[float_columns] = df[float_columns].fillna(0)
        df['PLAYER'] = df['PLAYER'].apply(unidecode)

        df.columns = [col + '_paint' for col in df.columns]


        
        #save to csv
        file_path_csv = csv_folder_path   #f"nba_tracking/tracking_csv_2024-25"
        path = file_path_csv
        csv_path = path
        os.makedirs(csv_path, exist_ok=True)
        df.to_csv(f"{csv_path}/paint_touch_content.csv", index=False) # "D:\nba_tracking_data_csv\nba_csv_2024-25\paint_touch_content.csv"

        display(df)


    if measure_type == "Passing":
        rename_map = {
        'PLAYER_NAME': 'PLAYER',
        'TEAM_ABBREVIATION': 'TEAM',
        'GP': 'GP',
        'W': 'W',
        'L': 'L',
        'MIN': 'MIN',
        'PASSES_MADE': 'PassesMade',
        'PASSES_RECEIVED': 'PassesReceived',
        'AST': 'AST',
        'SECONDARY_AST': 'SecondaryAST',
        'POTENTIAL_AST': 'PotentialAST',
        'AST_POINTS_CREATED': 'ASTPTSCreated',
        'AST_ADJ': 'ASTAdj',
        'AST_TO_PASS_PCT': 'Assist_to_Pass',
        'AST_TO_PASS_PCT_ADJ': 'Assist_to_Pass_Percentage_Adj'}

        df = df.rename(columns=rename_map)[list(rename_map.values())]


        int_columns = ['GP','W','L']
        float_columns = [
            'MIN',  'PassesMade', 'PassesReceived', 'AST', 'SecondaryAST', 
            'PotentialAST', 'ASTPTSCreated', 'ASTAdj', 'Assist_to_Pass', 'Assist_to_Pass_Percentage_Adj']

        df[int_columns] = df[int_columns].astype(int)
        df[float_columns] = df[float_columns].astype(float)
        df[float_columns] = df[float_columns].fillna(0)
        df[float_columns] = df[float_columns] / 100


        df['PLAYER'] = df['PLAYER'].apply(unidecode)

        df.columns = [col + '_passing' for col in df.columns]



        
        #save to csv
        file_path_csv = csv_folder_path   #f"nba_tracking/tracking_csv_2024-25"
        # path = file_path_csv
        csv_path = file_path_csv
        os.makedirs(csv_path, exist_ok=True)
        df.to_csv(f"{csv_path}/passing_content.csv", index=False) # "D:\nba_tracking_data_csv\nba_csv_2024-25\passing_content.csv"

        display(df)

    if measure_type == "PullUpShot":
        rename_map = {
        'PLAYER_NAME': 'PLAYER',
        'TEAM_ABBREVIATION': 'TEAM',
        'GP': 'GP',
        'W': 'W',
        'L': 'L',
        'MIN': 'MIN',
        'PULL_UP_PTS': 'PTS',
        'PULL_UP_FGM': 'FGM',
        'PULL_UP_FGA': 'FGA',
        'PULL_UP_FG_PCT': 'FG%',
        'PULL_UP_FG3M': '3PM',
        'PULL_UP_FG3A': '3PA',
        'PULL_UP_FG3_PCT': '3P%',
        'PULL_UP_EFG_PCT': 'eFG%'}

        df = df.rename(columns=rename_map)[list(rename_map.values())]


        int_columns = ['GP', 'W', 'L']
        float_columns = [
            'MIN', 'PTS', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'eFG%']

        df[int_columns] = df[int_columns].replace('-', 0).astype(int)
        df[float_columns] = df[float_columns].replace('-', 0).astype(float)
        df[float_columns] = df[float_columns].fillna(0)
        df['PLAYER'] = df['PLAYER'].apply(unidecode)

        df.columns = [col + '_pullup' for col in df.columns]


        
        #save to csv
        file_path_csv = csv_folder_path #f"nba_tracking/tracking_csv_2024-25"
        path = file_path_csv
        csv_path = path
        os.makedirs(csv_path, exist_ok=True)
        df.to_csv(f"{csv_path}/pullup_content.csv", index=False) # "D:\nba_tracking_data_csv\nba_csv_2024-25\pullup_content.csv"

        display(df)


    if measure_type == "Efficiency":
        rename_map = {
        'PLAYER_NAME': 'PLAYER',
        'TEAM_ABBREVIATION': 'TEAM',
        'GP': 'GP',
        'W': 'W',
        'L': 'L',
        'MIN': 'MIN',
        'POINTS': 'PTS',
        'DRIVE_PTS': 'DrivePTS',
        'DRIVE_FG_PCT': 'DriveFG%',
        'CATCH_SHOOT_PTS': 'C&SPTS',
        'CATCH_SHOOT_FG_PCT': 'C&SFG%',
        'PULL_UP_PTS': 'Pull UpPTS',
        'PULL_UP_FG_PCT': 'Pull UpFG%',
        'PAINT_TOUCH_PTS': 'PaintTouch PTS',
        'PAINT_TOUCH_FG_PCT': 'PaintTouch FG%',
        'POST_TOUCH_PTS': 'PostTouch PTS',
        'POST_TOUCH_FG_PCT': 'PostTouch FG%',
        'ELBOW_TOUCH_PTS': 'ElbowTouch PTS',
        'ELBOW_TOUCH_FG_PCT': 'ElbowTouch FG%',
        'EFF_FG_PCT': 'eFG%'}

        df = df.rename(columns=rename_map)[list(rename_map.values())]

        int_columns = ['GP', 'W', 'L']
        float_columns = [
            'MIN','PTS', 'DrivePTS', 'DriveFG%', 'C&SPTS', 'C&SFG%', 'Pull UpPTS', 'Pull UpFG%', 'PaintTouch PTS', 'PaintTouch FG%', 
            'PostTouch PTS', 'PostTouch FG%', 'ElbowTouch PTS', 'ElbowTouch FG%', 'eFG%']

        df[int_columns] = df[int_columns].replace('-', 0).astype(int)
        df[float_columns] = df[float_columns].replace('-', 0).astype(float)
        df[float_columns] = df[float_columns].fillna(0)
        df['PLAYER'] = df['PLAYER'].apply(unidecode)

        df.columns = [col + '_shot_efg' for col in df.columns]


        
        #save to csv
        file_path_csv = csv_folder_path #f"nba_tracking/tracking_csv_2024-25"
        path = file_path_csv
        csv_path = path
        os.makedirs(csv_path, exist_ok=True)
        df.to_csv(f"{csv_path}/shooting_efficiency_content.csv", index=False) #"D:\nba_tracking_data_csv\nba_csv_2024-25\shooting_efficiency_content.csv"

        display(df)


    if measure_type == "Possessions":
        rename_map = {
        'PLAYER_NAME': 'Player',
        'TEAM_ABBREVIATION': 'Team',
        'GP': 'GP',
        'W': 'W',
        'L': 'L',
        'MIN': 'MIN',
        'POINTS': 'PTS',
        'TOUCHES': 'TOUCHES',
        'FRONT_CT_TOUCHES': 'Front CTTouches',
        'TIME_OF_POSS': 'Time OfPoss',
        'AVG_SEC_PER_TOUCH': 'Avg Sec PerTouch',
        'AVG_DRIB_PER_TOUCH': 'Avg Drib PerTouch',
        'PTS_PER_TOUCH': 'PTS PerTouch',
        'ELBOW_TOUCHES': 'ElbowTouches',
        'POST_TOUCHES': 'PostUps',
        'PAINT_TOUCHES': 'PaintTouches',
        'PTS_PER_ELBOW_TOUCH': 'PTS PerElbow Touch',
        'PTS_PER_POST_TOUCH': 'PTS PerPost Touch',
        'PTS_PER_PAINT_TOUCH': 'PTS PerPaint Touch'}

        df = df.rename(columns=rename_map)[list(rename_map.values())]

        int_columns = ['GP', 'W', 'L']
        float_columns = [
            'MIN', 'PTS', 'TOUCHES', 'Front CTTouches', 'Time OfPoss', 'Avg Sec PerTouch', 
            'Avg Drib PerTouch', 'PTS PerTouch', 'ElbowTouches', 'PostUps', 'PaintTouches', 
            'PTS PerElbow Touch', 'PTS PerPost Touch', 'PTS PerPaint Touch'
            ]

        df[int_columns] = df[int_columns].replace('-', 0).astype(int)
        df[float_columns] = df[float_columns].replace('-', 0).astype(float)
        df[float_columns] = df[float_columns].fillna(0)
        df['Player'] = df['Player'].apply(unidecode)

        df.columns = [col + '_touches' for col in df.columns]


        
        #save to csv
        file_path_csv = csv_folder_path #f"nba_tracking/tracking_csv_2024-25"
        path = file_path_csv
        csv_path = path
        os.makedirs(csv_path, exist_ok=True)
        df.to_csv(f"{csv_path}/touches_content.csv", index=False) # "D:\nba_tracking_data_csv\nba_csv_2024-25\touches_content.csv"

        display(df)




    if measure_type == "PostTouch":
        rename_map = {
        'PLAYER_NAME': 'PLAYER',
        'TEAM_ABBREVIATION': 'TEAM',
        'GP': 'GP',
        'W': 'W',
        'L': 'L',
        'MIN': 'MIN',
        'TOUCHES': 'Touches',
        'POST_TOUCHES': 'PostUps',
        'POST_TOUCH_FGM': 'FGM',
        'POST_TOUCH_FGA': 'FGA',
        'POST_TOUCH_FG_PCT': 'FG%',
        'POST_TOUCH_FTM': 'FTM',
        'POST_TOUCH_FTA': 'FTA',
        'POST_TOUCH_FT_PCT': 'FT%',
        'POST_TOUCH_PTS': 'PTS',
        'POST_TOUCH_PTS_PCT': 'PTS%',
        'POST_TOUCH_PASSES': 'PASS',
        'POST_TOUCH_PASSES_PCT': 'PASS%',
        'POST_TOUCH_AST': 'AST',
        'POST_TOUCH_AST_PCT': 'AST%',
        'POST_TOUCH_TOV': 'TO',
        'POST_TOUCH_TOV_PCT': 'TOV%',
        'POST_TOUCH_FOULS': 'PF',
        'POST_TOUCH_FOULS_PCT': 'PF%'}

        df = df.rename(columns=rename_map)[list(rename_map.values())]

        int_columns = ['GP', 'W', 'L']
        float_columns = [
            'MIN', 'Touches', 'PostUps', 'FGM', 'FGA', 'FG%', 'FTM', 'FTA', 'FT%', 'PTS', 'PTS%', 'PASS', 'PASS%', 'AST', 'AST%', 'TO', 'TOV%', 'PF', 'PF%'
            ]

        df[int_columns] = df[int_columns].replace('-', 0).astype(int)
        df[float_columns] = df[float_columns].replace('-', 0).astype(float)
        df[float_columns] = df[float_columns].fillna(0)
        df['PLAYER'] = df['PLAYER'].apply(unidecode)

        df.columns = [col + '_post_ups' for col in df.columns]


        
        #save to csv
        file_path_csv = csv_folder_path #f"nba_tracking/tracking_csv_2024-25"
        path = file_path_csv
        csv_path = path
        os.makedirs(csv_path, exist_ok=True)
        df.to_csv(f"{csv_path}/tracking_post_ups_content.csv", index=False) # "D:\nba_tracking_data_csv\nba_csv_2024-25\tracking_post_ups_content.csv"

        display(df)

import os
import pandas as pd

def replace_regular_w_playin_or_playoff(regular_season_csv_path, playin_or_playoff_csv_path):
    """
    Updates regular season CSV files with Play-In or Playoff data for matching players.
    Reports whether any updates were made to each file.
    """
    # List all CSV files in the regular season directory
    csv_files = [f for f in os.listdir(regular_season_csv_path) if f.endswith('.csv')]

    # Process each CSV file
    for filename in csv_files:
        regular_csv_path = os.path.join(regular_season_csv_path, filename)
        
        # Construct the corresponding Play-In or Playoff file path
        playin_csv_path = os.path.join(playin_or_playoff_csv_path, 'nba_csv_2024-25', filename)
        print(f"Processing: {playin_csv_path}")
        
        # Check if the corresponding Play-In or Playoff file exists
        if not os.path.exists(playin_csv_path):
            print(f"Play-In/Playoff file not found for {filename}. Skipping.")
            continue

        # Read the regular season and Play-In/Playoff data
        df_regular = pd.read_csv(regular_csv_path)
        df_playin = pd.read_csv(playin_csv_path)

        # Determine the player name column (assumes it starts with 'PLAYER_' or 'Player_')
        player_columns = [col for col in df_regular.columns if col.startswith('PLAYER_') or col.startswith('Player_')]
        if not player_columns:
            print(f"No player column found in {filename}. Skipping.")
            continue
        player_column = player_columns[0]

        # Set the player name column as the index for both DataFrames
        df_regular.set_index(player_column, inplace=True)
        df_playin.set_index(player_column, inplace=True)

        # Create a copy of the regular DataFrame before the update
        df_regular_before = df_regular.copy()

        # Update the regular season data with Play-In/Playoff data for matching players
        df_regular.update(df_playin)

        # Compare the DataFrames to check for any changes
        df_diff = df_regular.compare(df_regular_before)

        if not df_diff.empty:
            # Reset the index to turn the player name back into a column
            df_regular.reset_index(inplace=True)

            # Save the updated DataFrame back to the original regular season CSV file
            df_regular.to_csv(regular_csv_path, index=False)

            print(f"Updated {filename} in {regular_csv_path}.")
        else:
            print(f"No updates made to {filename}.")

if __name__ == "__main__":
    raise ImportError("This script is intended to be imported as a module, not executed directly.")




# # tracking_list = [
# #     "PostTouch", "CatchShoot", "Drives", "ElbowTouch", "PaintTouch", "Passing",
# #     "PullUpShot", "Efficiency", "Possessions"
# # ]

# # season = "2024-25"
# # seasontype = "Regular Season"
# # csv_folder_path = r"D:\nba_tracking_data_csv\nba_csv_2024-25"

# # for measuretype in tracking_list:
# #     try:
# #         tracking_scrape(measuretype, season, seasontype, csv_folder_path)
# #     except Exception as e:
# #         print(f"Error for measure type {measuretype}: {e}")


# # season = "2024-25"
# # seasontype = "PlayIn"
# # csv_folder_path = r"D:\nba_tracking_data_csv\PlayIn\nba_csv_2024-25"

# # for measuretype in tracking_list:
# #     try:
# #         tracking_scrape(measuretype, season, seasontype, csv_folder_path)
# #     except Exception as e:
# #         print(f"Error for measure type {measuretype}: {e}")


# # season = "2024-25"
# # seasontype = "Playoffs"
# # csv_folder_path = r"D:\nba_tracking_data_csv\Playoffs\nba_csv_2024-25"

# # for measuretype in tracking_list:
# #     try:
# #         tracking_scrape(measuretype, season, seasontype, csv_folder_path)
# #     except Exception as e:
# #         print(f"Error for measure type {measuretype}: {e}")




# import os
# import pandas as pd

# # Define the directory containing both regular season and Play-In CSV files
# csv_directory = r"D:\nba_tracking_data_csv\nba_csv_2024-25"
# csv_directory_playin = r"D:\nba_tracking_data_csv\PlayIn"
# csv_directory_playoff = r"D:\nba_tracking_data_csv\Playoffs"



# replace_regular_w_playin_or_playoff(csv_directory, csv_directory_playin)
# replace_regular_w_playin_or_playoff(csv_directory, csv_directory_playoff)

# # season = "2023-24"
# # seasontype = "Regular Season"
# # csv_folder_path = r"D:\nba_tracking_data_csv\nba_csv_2023-24"

# # for measuretype in tracking_list:
# #     try:
# #         tracking_scrape(measuretype, season, seasontype, csv_folder_path)
# #     except Exception as e:
# #         print(f"Error for measure type {measuretype}: {e}")


# # season = "2022-23"
# # seasontype = "Regular Season"
# # csv_folder_path = r"D:\nba_tracking_data_csv\nba_csv_2022-23"

# # for measuretype in tracking_list:
# #     try:
# #         tracking_scrape(measuretype, season, seasontype, csv_folder_path)
# #     except Exception as e:
# #         print(f"Error for measure type {measuretype}: {e}")





