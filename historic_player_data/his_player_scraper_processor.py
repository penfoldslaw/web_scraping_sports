import subprocess
import sys
from pathlib import Path
import os
import pandas as pd
import configparser as cp
import ast 
# Move up one level to reach web_scraping_sports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from get_matchup import fetch_matchup_list  

def run_script(player, season, main_folder, year, quarter_data):
    path = Path(__file__).resolve().parent
    subprocess.run([sys.executable,path / "his_player_scraper.py", player, season, main_folder, year, quarter_data])

if __name__ == "__main__":
    import os
    import pandas as pd
    import configparser as cp
    import ast 

    

    # Only input you need to make get the teams playing or you want
    matchup = fetch_matchup_list()
    df_list = []  # List to store dataframes
    for team in matchup:
        # gets roster data from all teams
        roster_path = f"D:\\roster_folder\\2024\\{team}_roster_file.csv"  # Construct the file path



        # Iterate through all files in the directory
        if os.path.exists(roster_path):  # Check if file exists
            df = pd.read_csv(roster_path)  # Read CSV file
            df_list.append(df)  # Append DataFrame to the list




            # Concatenate all the box score dataframes into one
            df= pd.concat(df_list, ignore_index=True)
            
            #gets all of the players names uni stand for unicode names gets weird
            df =df['PLAYER_uni'].tolist()

    # a new variable to hold all of the list of names
    list_of_names = df

    unavaliable_names = []
    for name in list_of_names:
        file_path = f"D:/nba_player_historic/nba_html_2023-24/{name}_content.html"
        # print(file_path)

        if os.path.exists(file_path):
            print("File exists! ")
        else:
            print("File does not exist.")
            unavaliable_names.append(name)

    # just to say the players needed and error checking
    print(unavaliable_names)


    players = unavaliable_names

    seasons = [ "2022-23", "2023-24"]
    main_folder = "D:/nba_player_historic"
    years = ["2022-23", "2023-24"] #old logic was to use the same year for all seasons keeping it because it is not clear if the year is used for anything else
    
    for player in players:
        for season, year in zip(seasons, years):
            # run_script(player, season, main_folder, year,'yes')
            run_script(player, season, main_folder, year,'no')
    
    print("All scripts have finished executing.")