from his_url_usage_scraper import usage_scraper, replace_regular_w_playin_or_playoff
import os
import sys
import datetime

os.makedirs("history_logs", exist_ok=True)
log_file_path = "history_logs/his_usage_url.log"
sys.stdout = open(log_file_path, "w")
sys.stderr = open(log_file_path, "w")

def log_with_timestamp(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp} - {message}")
    print(f"{timestamp} - {message}", file=sys.stderr)

log_with_timestamp(f"Scraping usage data...") 


# seasons = ["2023-24", "2022-23"]
# base_dir = "D:/nba_usage_csv_historic"

season_1 = "2022-23"
season_2 = "2023-24"


usage_scraper("Regular Season", season_1,"D:/nnba_usage_csv_historic" ,f"usage_csv_{season_1}") # "D:\nba_usage_csv_historic"
usage_scraper("PlayIn", season_1,"D:/nba_usage_csv_historic/PlayIn" ,f"usage_csv_{season_1}/nba_csv_{season_1}")
usage_scraper("Playoffs", season_1,"D:/nba_usage_csv_historic/Playoffs" ,f"usage_csv_{season_1}/nba_csv_{season_1}")


replace_regular_w_playin_or_playoff(rf"D:\nba_usage_csv_historic\usage_csv_{season_1}", rf"D:\nba_usage_csv_historic\PlayIn\usgae_csv_{season_1}",season_1)
replace_regular_w_playin_or_playoff(rf"D:\nba_usage_csv_historic\usage_csv_{season_1}", rf"D:\nba_usage_csv_historic\Playoffs\usage_csv_{season_1}",season_1)


usage_scraper("Regular Season", season_2,"D:/nba_usage_csv_historic" ,f"usage_csv_{season_2}")
usage_scraper("PlayIn", season_2,"D:/nba_usage_csv_historic/PlayIn" ,f"usage_csv_{season_2}/nba_csv_{season_2}")
usage_scraper("Playoffs", season_2,"D:/nba_usage_csv_historic/Playoffs" ,f"usage_csv_{season_2}/nba_csv_{season_2}")

replace_regular_w_playin_or_playoff(rf"D:\nba_usage_csv_historic\usage_csv_{season_2}", rf"D:\nba_usage_csv_historic\PlayIn\usage_csv_{season_2}",season_2)
replace_regular_w_playin_or_playoff(rf"D:\nba_usage_csv_historic\usage_csv_{season_2}", rf"D:\nba_usage_csv_historic\Playoffs\usage_csv_{season_2}",season_2) 



# usage_scraper("Regular Season", "2024-25","D:/nba_usage_csv_current" ,"usage_csv_2024-25")
# usage_scraper("PlayIn", "2024-25","D:/nba_usage_csv_current/PlayIn" ,"usage_csv_2024-25/nba_csv_2024-25")
# usage_scraper("Playoffs", "2024-25","D:/nba_usage_csv_current/Playoffs" ,"usage_csv_2024-25/nba_csv_2024-25")


# replace_regular_w_playin_or_playoff(r"D:\nba_usage_csv_current\usage_csv_2024-25", r"D:\nba_usage_csv_current\PlayIn\usage_csv_2024-25")
# replace_regular_w_playin_or_playoff(r"D:\nba_usage_csv_current\usage_csv_2024-25", r"D:\nba_usage_csv_current\Playoffs\usage_csv_2024-25")



# Processing: D:\nba_usage_csv_historic\PlayIn\usage_csv_2023-24\nba_csv_2022-23\2023-24_content.csv
# Play-In/Playoff file not found for 2023-24_content.csv. Skipping.
# Processing: D:\nba_usage_csv_historic\Playoffs\usage_csv_2023-24\nba_csv_2022-23\2023-24_content.csv
# Play-In/Playoff file not found for 2023-24_content.csv. Skipping.



# for season in seasons:
#     regular_path = f"{base_dir}/usage_csv_{season}"
#     playin_path = f"{base_dir}/PlayIn/usage_csv_{season}"
#     playoffs_path = f"{base_dir}/Playoffs/usage_csv_{season}"

#     try:
#         usage_scraper("Regular Season", season, base_dir, f"usage_csv_{season}")
#         usage_scraper("PlayIn", season, f"{base_dir}\PlayIn", rf"usage_csv_{season}\nba_csv_{season}")
#         usage_scraper("Playoffs", season, f"{base_dir}\layoffs", rf"usage_csv_{season}\nba_csv_{season}")
#     except Exception as e:
#         print(f"Error scraping usage for season {season}: {e}")

#     try:
#         replace_regular_w_playin_or_playoff(regular_path, playin_path,season)
#         replace_regular_w_playin_or_playoff(regular_path, playoffs_path,season)
#     except Exception as e:
#         print(f"Error replacing regular with PlayIn/Playoffs for season {season}: {e}")



# Processing: D:/nba_usage_csv_historic/PlayIn/usage_csv_2022-23\nba_csv_2024-25\2022-23_content.csv
# Play-In/Playoff file not found for 2022-23_content.csv. Skipping.
# Processing: D:/nba_usage_csv_historic/Playoffs/usage_csv_2022-23\nba_csv_2024-25\2022-23_content.csv
# Play-In/Playoff file not found for 2022-23_content.csv. Skipping.




# usage_scraper("Regular Season", "2024-25","D:/nba_usage_csv_historic" ,"usage_csv_2024-25")
# usage_scraper("PlayIn", "2024-25","D:/nba_usage_csv_historic/PlayIn" ,"usage_csv_2024-25")
# usage_scraper("Playoffs", "2024-25","D:/nba_usage_csv_historic/Playoffs" ,"usage_csv_2024-25")


# replace_regular_w_playin_or_playoff("D:/nba_usage_csv_historic/usage_csv_2024-25", "D:/nba_usage_csv_historic/PlayIn/usage_csv_2024-25")
# replace_regular_w_playin_or_playoff("D:/nba_usage_csv_historic/usage_csv_2024-25", "D:/nba_usage_csv_historic/Playoffs/usage_csv_2024-25")