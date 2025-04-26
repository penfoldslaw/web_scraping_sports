from url_track_scraper import tracking_scrape, replace_regular_w_playin_or_playoff
import sys
import datetime
import os

os.makedirs("current_logs", exist_ok=True)
log_file_path = "current_logs/current_track_url.log"
sys.stdout = open(log_file_path, "w")
sys.stderr = open(log_file_path, "w")

def log_with_timestamp(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp} - {message}")
    print(f"{timestamp} - {message}", file=sys.stderr)

log_with_timestamp(f"Scraping track data...") 


tracking_list = [
    "PostTouch", "CatchShoot", "Drives", "ElbowTouch", "PaintTouch", "Passing",
    "PullUpShot", "Efficiency", "Possessions"
]

season = "2024-25"
seasontype = "Regular Season"
csv_folder_path = r"D:\nba_tracking_data_csv\nba_csv_2024-25"

for measuretype in tracking_list:
    try:
        tracking_scrape(measuretype, season, seasontype, csv_folder_path)
    except Exception as e:
        print(f"Error for measure type {measuretype}: {e}")


season = "2024-25"
seasontype = "PlayIn"
csv_folder_path = r"D:\nba_tracking_data_csv\PlayIn\nba_csv_2024-25"

for measuretype in tracking_list:
    try:
        tracking_scrape(measuretype, season, seasontype, csv_folder_path)
    except Exception as e:
        print(f"Error for measure type {measuretype}: {e}")


season = "2024-25"
seasontype = "Playoffs"
csv_folder_path = r"D:\nba_tracking_data_csv\Playoffs\nba_csv_2024-25"

for measuretype in tracking_list:
    try:
        tracking_scrape(measuretype, season, seasontype, csv_folder_path)
    except Exception as e:
        print(f"Error for measure type {measuretype}: {e}")




import os
import pandas as pd

# Define the directory containing both regular season and Play-In CSV files
csv_directory = r"D:\nba_tracking_data_csv\nba_csv_2024-25"
csv_directory_playin = r"D:\nba_tracking_data_csv\PlayIn"
csv_directory_playoff = r"D:\nba_tracking_data_csv\Playoffs"



replace_regular_w_playin_or_playoff(csv_directory, csv_directory_playin)
replace_regular_w_playin_or_playoff(csv_directory, csv_directory_playoff)

# season = "2023-24"
# seasontype = "Regular Season"
# csv_folder_path = r"D:\nba_tracking_data_csv\nba_csv_2023-24"

# for measuretype in tracking_list:
#     try:
#         tracking_scrape(measuretype, season, seasontype, csv_folder_path)
#     except Exception as e:
#         print(f"Error for measure type {measuretype}: {e}")


# season = "2022-23"
# seasontype = "Regular Season"
# csv_folder_path = r"D:\nba_tracking_data_csv\nba_csv_2022-23"

# for measuretype in tracking_list:
#     try:
#         tracking_scrape(measuretype, season, seasontype, csv_folder_path)
#     except Exception as e:
#         print(f"Error for measure type {measuretype}: {e}")