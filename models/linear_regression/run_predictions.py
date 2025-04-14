from prediction import prediction
import pandas as pd
import os
import pandas as pd
import sys
import logging
# Move up one level to reach web_scraping_sports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from get_matchup import fetch_matchup_list  


log_file_path = "models\linear_regression\prediction.log"

import time

start_time = time.time()





# Open the log file in append mode ("a")
sys.stdout = open(log_file_path, "w")
sys.stderr = open(log_file_path, "w")

matchup = fetch_matchup_list()  # Only input you need to make get the teams playing or you want

df_list = []  # List to store DataFrames

# Loop through each team's roster file
for team in matchup:
    roster_path = f"D:\\roster_folder\\2024\\{team}_roster_file.csv"  # Construct the file path

    if os.path.exists(roster_path):  # Check if file exists
        df = pd.read_csv(roster_path)  # Read CSV file
        df_list.append(df)  # Store DataFrame in list
    else:
        print(f"File not found: {roster_path}")  # Debugging message

# Combine all DataFrames if any were found
if df_list:
    df_combined = pd.concat(df_list, ignore_index=True)

    # Extract two columns as a dictionary
    player_dict = dict(zip(df_combined['PLAYER_uni'], df_combined['api_team_name']))

    print(player_dict)  # Display dictionary
else:
    print("No valid roster files found.")





# remember to run mover
# remember to check schedule csv
date_list = ["2023-24","2024-25"]
stats_path = {
    'usage_path':'D:/nba_usage_csv_historic/usage_csv_{date}/{date}_content.csv',
    'catch_shoot':"D:/nba_tracking_data_csv/nba_csv_{date}/catch_shoot_content.csv",
    'drives':"D:/nba_tracking_data_csv/nba_csv_{date}/drives_content.csv",
    'elbow_touches':"D:/nba_tracking_data_csv/nba_csv_{date}/elbow_touch_content.csv",
    'paint_touches':"D:/nba_tracking_data_csv/nba_csv_{date}/paint_touch_content.csv",
    'passing':"D:/nba_tracking_data_csv/nba_csv_{date}/passing_content.csv",
    'pullup':"D:/nba_tracking_data_csv/nba_csv_{date}/pullup_content.csv",
    'shooting_efficiency':"D:/nba_tracking_data_csv/nba_csv_{date}/shooting_efficiency_content.csv",
    'touches':"D:/nba_tracking_data_csv/nba_csv_{date}/touches_content.csv",
    'tracking_post_ups_content':"D:/nba_tracking_data_csv/nba_csv_{date}/tracking_post_ups_content.csv"
}

schedule_base_path = "D:/nba_scheduled_play_csv/schedule_csv_2024-25/schedule_content.csv"
player_base_path = "D:/nba_player_csv_historic/season_{date}/all_quarters/{player}_content.csv"
defense_base_path = "D:/nba_defense_history_csv/defense_csv_{date}/all_quarter_defense_content.csv"


results_reb = prediction(player_dict, date_list, stats_path, player_base_path, defense_base_path, schedule_base_path,'REB','REB')
results_ast = prediction(player_dict, date_list, stats_path, player_base_path, defense_base_path, schedule_base_path,'AST','AST')
results_pts = prediction(player_dict, date_list, stats_path, player_base_path, defense_base_path, schedule_base_path,'PTS','PTS')
results_3pm = prediction(player_dict, date_list, stats_path, player_base_path, defense_base_path, schedule_base_path,'3PM','3PM')
results_pts = results_pts.rename(columns={'FGA': 'PTS'})


end_time = time.time()
elapsed_time = end_time - start_time

print(f"Execution time: {elapsed_time:.2f} seconds")