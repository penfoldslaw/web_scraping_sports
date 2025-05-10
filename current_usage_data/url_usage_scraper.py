import requests
import pandas as pd
from unidecode import unidecode
import os
from IPython.display import display
from unidecode import unidecode


import requests
import pandas as pd


def usage_scraper(seasontype,season,csv_main_folder ,csv_sub_folder):

    url = "https://stats.nba.com/stats/leaguedashplayerstats"

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
        "GameSegment": "",
        "Height": "",
        "ISTRound": "",
        "LastNGames": "0",
        "LeagueID": "00",
        "Location": "",
        "MeasureType": "Usage",  # This is the key param
        "Month": "0",
        "OpponentTeamID": "0",
        "Outcome": "",
        "PORound": "0",
        "PaceAdjust": "N",
        "PerMode": "PerGame",
        "Period": "0",
        "PlayerExperience": "",
        "PlayerPosition": "",
        "PlusMinus": "N",
        "Rank": "N",
        "Season": season, #"2024-25",
        "SeasonSegment": "",
        "SeasonType": seasontype, #"Regular Season",
        "ShotClockRange": "",
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
    df = pd.DataFrame(data['resultSets'][0]['rowSet'], columns=data['resultSets'][0]['headers'])
    df = df.sort_values(by='USG_PCT', ascending=False)

    # display(df)
    # print(df.columns)

    # print(df.head())


    columns_to_rename = {
        'PLAYER_NAME': 'Player',
        'TEAM_ABBREVIATION': 'TEAM',
        'AGE': 'AGE',
        'GP': 'GP',
        'W': 'W',
        'L': 'L',
        'MIN': 'MIN',
        'USG_PCT': 'USG%',
        'PCT_FGM': '%FGM',
        'PCT_FGA': '%FGA',
        'PCT_FG3M': '%3PM',
        'PCT_FG3A': '%3PA',
        'PCT_FTM': '%FTM',
        'PCT_FTA': '%FTA',
        'PCT_OREB': '%OREB',
        'PCT_DREB': '%DREB',
        'PCT_REB': '%REB',
        'PCT_AST': '%AST',
        'PCT_TOV': '%TOV',
        'PCT_STL': '%STL',
        'PCT_BLK': '%BLK',
        'PCT_BLKA': '%BLKA',
        'PCT_PF': '%PF',
        'PCT_PFD': '%PFD',
        'PCT_PTS': '%PTS'
    }

    # df = df.rename(columns=columns_to_rename)
    # print(df.columns)


    df = df.rename(columns=columns_to_rename)[list(columns_to_rename.values())]

    # print(df.columns)



    # df = df.rename(columns={'': 'RANK'})
    df['RANK'] = df.reset_index().index + 1
    int_columns = ['RANK','AGE','GP','W','L']
    float_columns = [
        'MIN',  'USG%', '%FGM', '%FGA', '%3PM', 
        '%3PA', '%FTM', '%FTA', '%OREB', '%DREB', '%REB', 
        '%AST', '%TOV', '%STL', '%BLK', '%BLKA', '%PF', '%PFD', '%PTS']

    df[int_columns] = df[int_columns].astype(int)
    df[float_columns] = df[float_columns].astype(float)
    df[float_columns] = df[float_columns].fillna(0)
    df['Player'] = df['Player'].apply(unidecode)
    df.columns = [col + '_usg' for col in df.columns]
    column_headers = [
        "RANK_usg", "Player_usg", "TEAM_usg", "AGE_usg", "GP_usg", "W_usg", "L_usg", 
        "MIN_usg", "USG%_usg", "%FGM_usg", "%FGA_usg", "%3PM_usg", "%3PA_usg", 
        "%FTM_usg", "%FTA_usg", "%OREB_usg", "%DREB_usg", "%REB_usg", "%AST_usg", 
        "%TOV_usg", "%STL_usg", "%BLK_usg", "%BLKA_usg", "%PF_usg", "%PFD_usg", 
        "%PTS_usg"
    ]
    df = df[column_headers]


    #save to csv
    # path = f'D:/nba_usage_csv_current/{csv_sub_folder}'
    path = f'{csv_main_folder}/{csv_sub_folder}'

    csv_path = path
    os.makedirs(csv_path, exist_ok=True)
    df.to_csv(f"{csv_path}/{season}_content.csv", index=False)

    print(len(df))


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


