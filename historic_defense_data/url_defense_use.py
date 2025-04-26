from url_his_defense_scraper import defense_scraper, replace_regular_w_playin_or_playoff
import os
import sys
import datetime

log_file_path = "history_logs/his_defense_url.log"

# Open the log file in append mode ("a")
sys.stdout = open(log_file_path, "a")
sys.stderr = open(log_file_path, "a")

def log_with_timestamp(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp} - {message}", file=sys.stderr)

log_with_timestamp("Scraping player url data...")


season_1 = "2022-23"
season_2 = "2023-24"


defense_scraper("Regular Season", season_1,"D:/nba_defense_csv_current" ,f"defense_csv_{season_1}")
defense_scraper("PlayIn", season_1,"D:/nba_defense_csv_current/PlayIn" ,f"defense_csv_{season_1}/nba_csv_{season_1}")
defense_scraper("Playoffs", season_1,"D:/nba_defense_csv_current/Playoffs" ,f"defense_csv_{season_1}/nba_csv_{season_1}")

replace_regular_w_playin_or_playoff(rf"D:\nba_defense_csv_current\defense_csv_{season_1}", rf"D:\nba_defense_csv_current\PlayIn\defense_csv_{season_1}",season_1)
replace_regular_w_playin_or_playoff(rf"D:\nba_defense_csv_current\defense_csv_{season_1}", rf"D:\nba_defense_csv_current\Playoffs\defense_csv_{season_1}",season_1)


defense_scraper("Regular Season", season_2,"D:/nba_defense_csv_current" ,f"defense_csv_{season_2}")
defense_scraper("PlayIn", season_2,"D:/nba_defense_csv_current/PlayIn" ,f"defense_csv_{season_2}/nba_csv_{season_2}")
defense_scraper("Playoffs", season_2,"D:/nba_defense_csv_current/Playoffs" ,f"defense_csv_{season_2}/nba_csv_{season_2}")

replace_regular_w_playin_or_playoff(rf"D:\nba_defense_csv_current\defense_csv_{season_2}", rf"D:\nba_defense_csv_current\PlayIn\defense_csv_{season_2}",season_2)
replace_regular_w_playin_or_playoff(rf"D:\nba_defense_csv_current\defense_csv_{season_2}", rf"D:\nba_defense_csv_current\Playoffs\defense_csv_{season_2}",season_2)



# defense_scraper("Regular Season", "2024-25","D:/nba_defense_csv_current" ,"defense_csv_2024-25")
# defense_scraper("PlayIn", "2024-25","D:/nba_defense_csv_current/PlayIn" ,"defense_csv_2024-25/nba_csv_2024-25")
# defense_scraper("Playoffs", "2024-25","D:/nba_defense_csv_current/Playoffs" ,"defense_csv_2024-25/nba_csv_2024-25")

# replace_regular_w_playin_or_playoff(r"D:\nba_defense_csv_current\defense_csv_2024-25", r"D:\nba_defense_csv_current\PlayIn\defense_csv_2024-25")
# replace_regular_w_playin_or_playoff(r"D:\nba_defense_csv_current\defense_csv_2024-25", r"D:\nba_defense_csv_current\Playoffs\defense_csv_2024-25")



# seasons = ["2022-23", "2023-24"]
# seasontypes = ["Regular Season", "PlayIn", "Playoffs"]

# for season, seasontype in zip(seasons, seasontypes):
#     print(f"Processing season: {season}, type: {seasontype}")
#     defense_scraper(seasontype, season, f"D:/nba_defense_history_csv/{seasontype}", f"defense_csv_{season}/nba_csv_{season}")
#     if seasontype != "Regular Season":
#         print(f"Replacing for season: {season}, type: {seasontype}")
#         replace_regular_w_playin_or_playoff(rf"D:\nba_defense_history_csv\defense_csv_{season}", rf"D:\nba_defense_history_csv\{seasontype}\defense_csv_{season}",season)






# seasons = ["2022-23", "2023-24"]
# seasontypes = ["Regular Season", "PlayIn", "Playoffs"]
# # secondseasontypes = ["PlayIn", "Playoffs"]
# for season, seasontype in zip(seasons, seasontypes):
#     defense_scraper(seasontype, season, f"D:/nba_defense_history_csv/{seasontype}", f"defense_csv_{season}/nba_csv_{season}")
#     if seasontype != "Regular Season":
#         replace_regular_w_playin_or_playoff(rf"D:\nba_defense_history_csv\defense_csv_{season}", rf"D:\nba_defense_history_csv\{seasontype}\defense_csv_{season}",season)



#Processing: D:/nba_defense_history_csv/PlayIn/defense_csv_2023-24/nba_csv_2023-24\nba_csv_2023-24\all_quarter_defense_content.csv
#Play-In/Playoff file not found for all_quarter_defense_content.csv. Skipping.

#["defense_csv_2022-23", "defense_csv_2023-24"]
# defense_scraper("Regular Season", "2024-25","D:/nba_defense_csv_current" ,"defense_csv_2024-25")
# defense_scraper("PlayIn", "2022-23","D:/nba_defense_history_csv/PlayIn" ,"defense_csv_2022-23")
# defense_scraper("Playoffs", "2022-23","D:/nba_defense_history_csv/Playoffs" ,"defense_csv_2022-23")

# # defense_scraper("Regular Season", "2024-25","D:/nba_defense_csv_current" ,"defense_csv_2024-25")
# defense_scraper("PlayIn", "2024-25","D:/nba_defense_history_csv/PlayIn" ,"defense_csv_2024-25")
# defense_scraper("Playoffs", "2024-25","D:/nba_defense_history_csv/Playoffs" ,"defense_csv_2024-25")

# replace_regular_w_playin_or_playoff("D:/nba_defense_history_csv/defense_csv_2024-25", "D:/nba_defense_history_csv/PlayIn/defense_csv_2024-25")
# replace_regular_w_playin_or_playoff("D:/nba_defense_history_csv/defense_csv_2024-25", "D:/nba_defense_history_csv/Playoffs/defense_csv_2024-25")


# from url_defense_scraper import defense_scraper, replace_regular_w_playin_or_playoff
# import os

# defense_scraper("Regular Season", "2024-25","D:/nba_defense_csv_current" ,"defense_csv_2024-25")
# defense_scraper("PlayIn", "2024-25","D:/nba_defense_csv_current/PlayIn" ,"defense_csv_2024-25/nba_csv_2024-25")
# defense_scraper("Playoffs", "2024-25","D:/nba_defense_csv_current/Playoffs" ,"defense_csv_2024-25/nba_csv_2024-25")

# replace_regular_w_playin_or_playoff(r"D:\nba_defense_csv_current\defense_csv_2024-25", r"D:\nba_defense_csv_current\PlayIn\defense_csv_2024-25")
# replace_regular_w_playin_or_playoff(r"D:\nba_defense_csv_current\defense_csv_2024-25", r"D:\nba_defense_csv_current\Playoffs\defense_csv_2024-25")

# #"D:\nba_defense_csv_current\PlayIn\defense_csv_2024-25\all_quarter_defense_content.csv"
# #"D:\nba_defense_csv_current\defense_csv_2024-25\all_quarter_defense_content.csv"
# # D:\nba_defense_csv_current\PlayIn\defense_csv_2024-25\nba_csv_2024-25\all_quarter_defense_content.csv