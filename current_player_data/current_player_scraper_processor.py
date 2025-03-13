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
    players = [
    "Cade Cunningham",
    "Jordan Poole",
    "Malik Beasley",
    "Jalen Duren",
    "Tobias Harris",
    "Alexandre Sarr",
    "Corey Kispert",
    "Khris Middleton",
    "Ausar Thompson",
    "Dennis Schroder",
    "Kyshawn George",
    "Tim Hardaway Jr.",
    "Richaun Holmes",
    "Marcus Smart",
    "Isaiah Stewart",
    "Luka Doncic",
    "Giannis Antetokounmpo",
    "Damian Lillard",
    "Austin Reaves",
    "Kyle Kuzma",
    "Dalton Knecht",
    "Brook Lopez",
    "Gabe Vincent",
    "Dorian Finney-Smith",
    "Taurean Prince",
    "Jarred Vanderbilt",
    "Paolo Banchero",
    "Franz Wagner",
    "Zion Williamson",
    "CJ McCollum",
    "Trey Murphy III",
    "Cole Anthony",
    "Wendell Carter Jr.",
    "Kentavious Caldwell-Pope",
    "Yves Missi",
    "Cameron Thomas",
    "Coby White",
    "Cameron Johnson",
    "Kevin Huerter",
    "Matas Buzelis",
    "D'Angelo Russell",
    "Nikola Vucevic",
    "Tre Jones",
    "Zach Collins",
    "Nicolas Claxton",
    "Ziaire Williams",
    "Keon Johnson",
    "Day'Ron Sharpe",
    "Stephen Curry",
    "Zach LaVine",
    "DeMar DeRozan",
    "Jimmy Butler",
    "Malik Monk",
    "Domantas Sabonis",
    "Keegan Murray",
    "Moses Moody",
    "Buddy Hield",
    "Quinten Post",
    "Draymond Green",
    "Keon Ellis"]


    seasons = ["2024-25"]
    main_folder = "D:/nba_player_current"
    years = ["2024-25"] #old logic was to use the same year for all seasons keeping it because it is not clear if the year is used for anything else
    
    for player in players:
        for season, year in zip(seasons, years):
            run_script(player, season, main_folder, year)
    
    print("All scripts have finished executing.")
