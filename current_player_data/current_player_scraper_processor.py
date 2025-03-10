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
    # "Scottie Barnes",
    # "Jordan Poole",
    # "RJ Barrett",
    # "Jakob Poeltl",
    # "Khris Middleton",
    # "Bilal Coulibaly",
    # "Alexandre Sarr",
    # "Jamal Shead",
    # "Kyshawn George",
    # "Corey Kispert",
    # "Marcus Smart",
    # "Carlton Carrington",
    # "Richaun Holmes",
    # "Orlando Robinson",
    "Damian Lillard",
    "Giannis Antetokounmpo",
    "Franz Wagner",
    "Paolo Banchero",
    "Kyle Kuzma",
    "Brook Lopez",
    "Cole Anthony",
    "Wendell Carter Jr.",
    "Taurean Prince",
    "Kentavious Caldwell-Pope",
    "Anthony Black",
    "Jonathan Isaac",
    "Goga Bitadze",
    "Tristan da Silva"
    # "LeBron James",
    # "Luka Doncic",
    # "Jayson Tatum",
    # "Jaylen Brown",
    # "Kristaps Porzingis",
    # "Austin Reaves",
    # "Derrick White",
    # "Payton Pritchard",
    # "Jrue Holiday",
    # "Dorian Finney-Smith",
    # "Dalton Knecht",
    # "Gabe Vincent"
    ]

    seasons = ["2024-25"]
    main_folder = "D:/nba_player_current"
    years = ["2024-25"] #old logic was to use the same year for all seasons keeping it because it is not clear if the year is used for anything else
    
    for player in players:
        for season, year in zip(seasons, years):
            run_script(player, season, main_folder, year)
    
    print("All scripts have finished executing.")
