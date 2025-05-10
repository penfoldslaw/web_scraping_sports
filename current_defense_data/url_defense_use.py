from url_defense_scraper import defense_scraper, replace_regular_w_playin_or_playoff
import os

defense_scraper("Regular Season", "2024-25","D:/nba_defense_csv_current" ,"defense_csv_2024-25")
defense_scraper("PlayIn", "2024-25","D:/nba_defense_csv_current/PlayIn" ,"defense_csv_2024-25/nba_csv_2024-25")
defense_scraper("Playoffs", "2024-25","D:/nba_defense_csv_current/Playoffs" ,"defense_csv_2024-25/nba_csv_2024-25")

replace_regular_w_playin_or_playoff(r"D:\nba_defense_csv_current\defense_csv_2024-25", r"D:\nba_defense_csv_current\PlayIn\defense_csv_2024-25")
replace_regular_w_playin_or_playoff(r"D:\nba_defense_csv_current\defense_csv_2024-25", r"D:\nba_defense_csv_current\Playoffs\defense_csv_2024-25")

#"D:\nba_defense_csv_current\PlayIn\defense_csv_2024-25\all_quarter_defense_content.csv"
#"D:\nba_defense_csv_current\defense_csv_2024-25\all_quarter_defense_content.csv"
# D:\nba_defense_csv_current\PlayIn\defense_csv_2024-25\nba_csv_2024-25\all_quarter_defense_content.csv
