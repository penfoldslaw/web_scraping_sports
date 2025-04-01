# from pathlib import Path
# from current_player_scraper import scrape_data  # Assuming this function exists

# def run_script(player, season, main_folder, year):
#     # Directly call the function instead of using subprocess
#     scrape_data(player, season, main_folder, year)

# if __name__ == "__main__":
#     players = ['Shai Gilgeous-Alexander', 'Cason Wallace', 'Alex Caruso', 'Jalen Williams', 'Isaiah Hartenstein']
#     seasons = ["2024-25"]
#     main_folder = "D:/nba_player_current"
#     years = ["2024-25"]  # Keeping this as is in case it's used elsewhere

#     for player in players:
#         for season, year in zip(seasons, years):
#             run_script(player, season, main_folder, year)

#     print("All scripts have finished executing.")


import subprocess
import sys
from pathlib import Path

def run_script(player, season, main_folder, year):
    path = Path(__file__).resolve().parent
    subprocess.run([sys.executable,path / "current_player_scraper.py", player, season, main_folder, year])

if __name__ == "__main__":
    import pandas as pd
    import os 


    matchup = ["PHX","MIL", "PHI", "NYK", "POR", "ATL", "GSW", "MEM", "TOR", "CHI", "ORL", "SAS", "MIN","DEN"]
    df_list = []  # List to store dataframes
    for team in matchup:
        roster_path = f"D:\\roster_folder\\2024\\{team}_roster_file.csv"  # Construct the file path



        # Iterate through all files in the directory
        if os.path.exists(roster_path):  # Check if file exists
            df = pd.read_csv(roster_path)  # Read CSV file
            df_list.append(df)  # Append DataFrame to the list




            # Concatenate all the box score dataframes into one
            df= pd.concat(df_list, ignore_index=True)
            


            df =df['PLAYER_uni'].tolist()

    list_of_names = df

    print(list_of_names) # check history for all comments on what this is doing

    players = list_of_names



    seasons = ["2024-25"]
    main_folder = "D:/nba_player_current"
    years = ["2024-25"] #old logic was to use the same year for all seasons keeping it because it is not clear if the year is used for anything else
    
    for player in players:
        for season, year in zip(seasons, years):
            run_script(player, season, main_folder, year)
    
    print("All scripts have finished executing.")
