from url_his_scraper_function import nba_player_scraper, prepend_csv_files
import os
import subprocess
import sys
from pathlib import Path
import os
import pandas as pd
import configparser as cp
import ast 
import datetime
# Move up one level to reach web_scraping_sports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from get_matchup import fetch_matchup_list  


log_file_path = "history_logs/his_player_url.log"

# Open the log file in append mode ("a")
sys.stdout = open(log_file_path, "a")
sys.stderr = open(log_file_path, "a")

def log_with_timestamp(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp} - {message}", file=sys.stderr)

log_with_timestamp("Scraping player url data...")


matchup = fetch_matchup_list()  # Only input you need to make get the teams playing or you want
df_list = []  # List to store dataframes
for team in matchup:
    roster_path = f"D:\\roster_folder\\2024\\{team}_roster_file.csv"  # Construct the file path



    # Iterate through all files in the directory
    if os.path.exists(roster_path):  # Check if file exists
        df = pd.read_csv(roster_path)  # Read CSV file
        df_list.append(df)  # Append DataFrame to the list




        # Concatenate all the box score dataframes into one
        df= pd.concat(df_list, ignore_index=True)
        

        df_player_id = df['PLAYER_ID'].tolist()
        df =df['PLAYER_uni'].tolist()
        

list_of_names = df
list_of_ids = df_player_id

print(list_of_names) # check history for all comments on what this is doing

players = list_of_names

player_ids = list_of_ids

# for id in player_ids:
#     try:
#         nba_player_scraper(id, "2024-25", "Regular Season", "Traditional", r"D:\nba_player_csv_historic\season_2024-25\all_quarters")
#     except Exception as e:
#         print(f"Error for player {id} during Regular Season: {e}")

#     try:
#         nba_player_scraper(id, "2024-25", "PlayIn", "Traditional", r"D:\nba_player_csv_historic\season_2024-25\playin")
#     except Exception as e:
#         print(f"Error for player {id} during Play-In: {e}")

#     try:
#         nba_player_scraper(id, "2024-25", "Playoffs", "Traditional", r"D:\nba_player_csv_historic\season_2024-25\playoffs")
#     except Exception as e:
#         print(f"Error for player {id} during Playoffs: {e}")


seasons = ["2023-24", "2022-23"]
types = [
    ("Regular Season", "all_quarters"),
    ("PlayIn", "playin"),
    ("Playoffs", "playoffs")
]

for season in seasons:
    for id in player_ids:
        for season_type, folder in types:
            try:
                path = fr"D:\nba_player_csv_historic\season_{season}\{folder}"
                nba_player_scraper(id, season, season_type, "Traditional", path)
            except Exception as e:
                print(f"Error for player {id} during {season_type} ({season}): {e}")




import csv
from pathlib import Path

seasons = ["2023-24", "2022-23"]
base_dir = Path(r"D:/nba_player_csv_historic")

for season in seasons:
    folder1 = base_dir / f"season_{season}" / "all_quarters"
    folder2 = base_dir / f"season_{season}" / "playoffs"
    folder3 = base_dir / f"season_{season}" / "playin"

    try:
        prepend_csv_files(folder1, folder2)
        prepend_csv_files(folder1, folder3)
    except Exception as e:
        print(f"Error processing season {season}: {e}")
