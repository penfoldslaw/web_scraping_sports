from url_usage_scraper import usage_scraper, replace_regular_w_playin_or_playoff
import os
import sys
import datetime

os.makedirs("current_logs", exist_ok=True)
log_file_path = "current_logs/current_usage_url.log"
sys.stdout = open(log_file_path, "w")
sys.stderr = open(log_file_path, "w")

def log_with_timestamp(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp} - {message}")
    print(f"{timestamp} - {message}", file=sys.stderr)

log_with_timestamp(f"Scraping usage data...") 




usage_scraper("Regular Season", "2024-25","D:/nba_usage_csv_current" ,"usage_csv_2024-25")
usage_scraper("PlayIn", "2024-25","D:/nba_usage_csv_current/PlayIn" ,"usage_csv_2024-25/nba_csv_2024-25")
usage_scraper("Playoffs", "2024-25","D:/nba_usage_csv_current/Playoffs" ,"usage_csv_2024-25/nba_csv_2024-25")


replace_regular_w_playin_or_playoff(r"D:\nba_usage_csv_current\usage_csv_2024-25", r"D:\nba_usage_csv_current\PlayIn\usage_csv_2024-25")
replace_regular_w_playin_or_playoff(r"D:\nba_usage_csv_current\usage_csv_2024-25", r"D:\nba_usage_csv_current\Playoffs\usage_csv_2024-25")

#"D:\nba_usage_csv_current\PlayIn\usage_csv_2024-25\2024-25_content.csv"