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
    "Mark Williams",
    "Miles Bridges",
    "Jimmy Butler",
    "LaMelo Ball",
    "Stephen Curry",
    "Brandin Podziemski",
    "Nick Smith Jr.",
    "Josh Green",
    "Moses Moody",
    "Draymond Green",
    "Paul George",
    "Tyrese Maxey",
    "Kelly Oubre Jr.",
    "Andre Drummond",
    "Shaedon Sharpe",
    "Quentin Grimes",
    "Deni Avdija",
    "Anfernee Simons",
    "Toumani Camara",
    "Donovan Clingan",
    "Bam Adebayo",
    "Tyler Herro",
    "Andrew Wiggins",
    "Bilal Coulibaly",
    "Alexandre Sarr",
    "Khris Middleton",
    "Carlton Carrington",
    "Davion Mitchell",
    "Kyshawn George",
    "Haywood Highsmith"
    ]

    seasons = ["2024-25"]
    main_folder = "D:/nba_player_current"
    years = ["2024-25"] #old logic was to use the same year for all seasons keeping it because it is not clear if the year is used for anything else
    
    for player in players:
        for season, year in zip(seasons, years):
            run_script(player, season, main_folder, year)
    
    print("All scripts have finished executing.")
