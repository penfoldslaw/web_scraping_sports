import requests
import pandas as pd
from unidecode import unidecode
import os
from IPython.display import display
from unidecode import unidecode

def defense_scraper(seasontype,season, csv_main_folder, csv_sub_folder):
    """
    Scrapes NBA team defense statistics for the specified season and saves them to a CSV file.
    """
    # Define the URL and parameters for the API request

    url = "https://stats.nba.com/stats/leaguedashteamstats"
    params = {
        "Conference": "",
        "DateFrom": "",
        "DateTo": "",
        "Division": "",
        "GameScope": "",
        "GameSegment": "",
        "Height": "",
        "ISTRound": "",
        "LastNGames": "0",
        "LeagueID": "00",
        "Location": "",
        "MeasureType": "Advanced",  # <== Defense Stats
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
        "Season": season,#"2024-25",
        "SeasonSegment": "",
        "SeasonType": seasontype ,#"Regular Season",
        "ShotClockRange": "",
        "StarterBench": "",
        "TeamID": "0",
        "TwoWay": "0",
        "VsConference": "",
        "VsDivision": ""
    }

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://www.nba.com/stats/",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Host": "stats.nba.com",
        "Origin": "https://www.nba.com"
    }

    response = requests.get(url, headers=headers, params=params, timeout=10)
    data = response.json()

    # Convert to DataFrame
    df = pd.DataFrame(data['resultSets'][0]['rowSet'], columns=data['resultSets'][0]['headers'])
    # display(df)
    print(df.columns)

    # Rename map: from NBA API column names to your simplified column names
    rename_map = {
        'TEAM_NAME': 'TEAM',
        'GP': 'GP',
        'W': 'W',
        'L': 'L',
        'MIN': 'MIN',
        'OFF_RATING': 'OffRtg',
        'DEF_RATING': 'DefRtg',
        'NET_RATING': 'NetRtg',
        'AST_PCT': 'AST%',
        'AST_TO': 'AST/TO',
        'AST_RATIO': 'ASTRatio',
        'OREB_PCT': 'OREB%',
        'DREB_PCT': 'DREB%',
        'REB_PCT': 'REB%',
        'TM_TOV_PCT': 'TOV%',
        'EFG_PCT': 'eFG%',
        'TS_PCT': 'TS%',
        'PACE': 'PACE',
        'PIE': 'PIE',
        'POSS': 'POSS'
    }

    df = df.rename(columns=rename_map)[list(rename_map.values())]  # Keep only relevant/renamed columns



    df['RANK'] = df.reset_index().index + 1
    df['TEAM'] = df['TEAM'].astype('string')

    rename_team = {
        'Atlanta Hawks': 'ATL',
        'Boston Celtics': 'BOS',
        'Brooklyn Nets': 'BKN',
        'Charlotte Hornets': 'CHA',
        'Chicago Bulls': 'CHI',
        'Cleveland Cavaliers': 'CLE',
        'Dallas Mavericks': 'DAL',
        'Denver Nuggets': 'DEN',
        'Detroit Pistons': 'DET',
        'Golden State Warriors': 'GSW',
        'Houston Rockets': 'HOU',
        'Indiana Pacers': 'IND',
        'LA Clippers': 'LAC',
        'Los Angeles Lakers': 'LAL',
        'Memphis Grizzlies': 'MEM',
        'Miami Heat': 'MIA',
        'Milwaukee Bucks': 'MIL',
        'Minnesota Timberwolves': 'MIN',
        'New Orleans Pelicans': 'NOP',
        'New York Knicks': 'NYK',
        'Oklahoma City Thunder': 'OKC',
        'Orlando Magic': 'ORL',
        'Philadelphia 76ers': 'PHI',
        'Phoenix Suns': 'PHX',
        'Portland Trail Blazers': 'POR',
        'Sacramento Kings': 'SAC',
        'San Antonio Spurs': 'SAS',
        'Toronto Raptors': 'TOR',
        'Utah Jazz': 'UTA',
        'Washington Wizards': 'WAS'
        }

    df['TEAM'] = df['TEAM'].map(rename_team)

    df['POSS'] = df['POSS']

    columns_to_convert = [
        'OffRtg', 'DefRtg', 'NetRtg', 'AST%', 'AST/TO', 'ASTRatio', 'OREB%', 'DREB%', 'REB%', 'TOV%', 'eFG%', 'TS%', 'PACE', 'PIE', 'POSS']

        # Converting selected columns to float
    df[columns_to_convert] = df[columns_to_convert].apply(pd.to_numeric, errors='coerce')
    headers = [
        "RANK", "TEAM", "GP", "W", "L", "MIN", "OffRtg", "DefRtg", "NetRtg", 
        "AST%", "AST/TO", "ASTRatio", "OREB%", "DREB%", "REB%", "TOV%", 
        "eFG%", "TS%", "PACE", "PIE", "POSS"
    ]

    df = df[headers]

    print(df.dtypes)

    # Show a preview
    # path = f'D:/nba_defense_csv_current/{csv_sub_folder}' 
    path = f'{csv_main_folder}/{csv_sub_folder}' 

    csv_path = path
    os.makedirs(csv_path, exist_ok=True)
    df.to_csv(f"{csv_path}/all_quarter_defense_content.csv", index=False)


    # df.info()

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
        player_columns = [col for col in df_regular.columns if col.startswith('TEAM') or col.startswith('team')]
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