import os
import datetime
import requests
import pandas as pd
from IPython.display import display
from unidecode import unidecode


def nba_player_scraper(player_id,season,season_type,stat_category,csv_path):


    # Display up to 10,000 rows
    pd.set_option('display.max_rows', 10000)

    # Display up to 10,000 columns
    pd.set_option('display.max_columns', 10000)

    # Optional: Don't truncate column width
    pd.set_option('display.max_colwidth', None)

    columns_to_keep = [
        "PLAYER_NAME","GAME_DATE", "MATCHUP", "WL", "MIN", "PTS", "FGM", "FGA", "FG_PCT",
        "FG3M", "FG3A", "FG3_PCT", "FTM", "FTA", "FT_PCT",
        "OREB", "DREB", "REB", "AST", "STL", "BLK", "TOV", "PF", "PLUS_MINUS"
    ]



    url = "https://stats.nba.com/stats/playergamelogs"

    params = {
        "PlayerID": player_id,
        "Season": season,
        "SeasonType": season_type,
        "StatCategory": stat_category
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
    df = pd.DataFrame(data['resultSets'][0]['rowSet'], columns=data['resultSets'][0]['headers'])
    # print(df.columns)
    df = df[columns_to_keep]


    # Convert the column to datetime format
    df['GAME_DATE'] = pd.to_datetime(df['GAME_DATE'])
    df['MIN']= round(df['MIN'],2)
    df['PLAYER_NAME'] = df['PLAYER_NAME'].apply(unidecode)
    player_name = df['PLAYER_NAME'].iloc[0]


    rename_map = {
        "GAME_DATE": "Date",
        "MATCHUP": "Matchup",
        "WL": "W/L",
        "MIN": "MIN",
        "PTS": "PTS",
        "FGM": "FGM",
        "FGA": "FGA",
        "FG_PCT": "FG%",
        "FG3M": "3PM",
        "FG3A": "3PA",
        "FG3_PCT": "3P%",
        "FTM": "FTM",
        "FTA": "FTA",
        "FT_PCT": "FT%",
        "OREB": "OREB",
        "DREB": "DREB",
        "REB": "REB",
        "AST": "AST",
        "STL": "STL",
        "BLK": "BLK",
        "TOV": "TOV",
        "PF": "PF",
        "PLUS_MINUS": "+/-"
    }

    # Apply the renaming
    df = df.rename(columns=rename_map)


    # Attempt to split and extract team names and home/away game status
    try:
        # First, try the safer .str.extract approach
        df[['Team', 'Away']] = df['Matchup'].str.extract(r'^(.*?)(?: vs\. | @ )(.*)$')
        df['Home/Away_game'] = df['Matchup'].apply(lambda x: 'Away' if ' @ ' in str(x) else 'Home')

    except Exception as first_error:
        try:
            # Fallback to original .str.split approach
            df[['Team', 'Away']] = df['Matchup'].str.split(r' vs\. | @ ', expand=True)
            df[['Away_game', 'Home/Away_game']] = df['Matchup'].str.split(' @ ', expand=True)

            # Fix the .map issue by using single bracket
            df['Home/Away_game'] = df['Home/Away_game'].map(lambda x: 'Away' if pd.notna(x) else x)
            df['Home/Away_game'] = df['Home/Away_game'].fillna('Home')

        except Exception as fallback_error:
            print(f"Error occurred while processing 'Matchup' column in {player_name}: {fallback_error}")


    # Convert data types for columns
    df['Date'] = pd.to_datetime(df['Date'], format='%b %d, %Y')
    df['Matchup'] = df['Matchup'].astype('string')
    df['Team'] = df['Team'].astype('string')
    df['Away'] = df['Away'].astype('string')
    df['Home/Away_game'] = df['Home/Away_game'].astype('string')
    df['W/L'] = df['W/L'].astype('string')


    columns_to_convert = [
        'PTS', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', 
        'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', '+/-'
    ]

    # Convert selected columns to numeric
    df[columns_to_convert] = df[columns_to_convert].apply(pd.to_numeric, errors='coerce')

    columns_to_convert = ['FG%', '3P%','FT%']
    df[columns_to_convert] = df[columns_to_convert].apply(lambda x: (x * 100).astype(float))






    # print(df.columns)

    # Reorder columns for final output
    df = df[['Date', 
            'Matchup', 
            'Team',
            'Away',
            'Home/Away_game',
            'W/L', 
            'MIN', 
            'PTS', 
            'FGM', 
            'FGA',
            'FG%', 
            '3PM', 
            '3PA', 
            '3P%', 
            'FTM', 
            'FTA', 
            'FT%', 
            'OREB', 
            'DREB', 
            'REB', 
            'AST', 
            'STL', 
            'BLK', 
            'TOV', 
            'PF', 
            '+/-']]
    
    
    

    # Save the dataframe to CSV
    # r"D:\nba_player_csv_current\season_{season}\all_quarters"
    os.makedirs(csv_path, exist_ok=True)
    df.to_csv(f'{csv_path}/{player_name}_content.csv', index=False)
    print(f"Successfully processed and saved {player_name}.csv")

    display(df.head(5))

    


    return df



import csv
def prepend_csv_files(folder1, folder2):
    # Get all CSV files in folder2
    csv_files = [f for f in folder2.iterdir() if f.suffix.lower() == '.csv']
    print(f"Found {len(csv_files)} CSV files in folder2.")

    for file2 in csv_files:
        file_name = file2.name
        file1 = folder1 / file_name

        print(f"\nProcessing: {file_name}")

        if not file1.exists():
            print(f"Skipping {file_name} (no matching file in folder1)")
            continue

        # Load header + all existing rows from file1
        with open(file1, 'r', newline='', encoding='utf-8') as f1:
            reader1 = csv.reader(f1)
            header = next(reader1, None)
            existing_rows = list(reader1)
            existing_row_set = set(tuple(row) for row in existing_rows)

        # Load new rows from file2 (skip header), filter out duplicates
        with open(file2, 'r', newline='', encoding='utf-8') as f2:
            reader2 = csv.reader(f2)
            next(reader2, None)  # skip header
            new_rows = [row for row in reader2 if tuple(row) not in existing_row_set]

        if not new_rows:
            print(f"No new rows to prepend in {file_name}")
            continue

        # Prepend new rows just after header
        combined_rows = new_rows + existing_rows

        # Overwrite file1 with header + combined rows
        with open(file1, 'w', newline='', encoding='utf-8') as f1:
            writer = csv.writer(f1)
            writer.writerow(header)
            writer.writerows(combined_rows)

        print(f"Prepended {len(new_rows)} new rows to {file_name}, filepath: {file2}")


if __name__ == "__main__":
    raise ImportError("This script is intended to be imported as a module, not executed directly.")