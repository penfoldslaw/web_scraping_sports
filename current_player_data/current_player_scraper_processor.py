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
    "Miles McBride",
    "Mikal Bridges",
    "Josh Hart",
    "O.G. Anunoby",
    "Karl-Anthony Towns",
    "Josh Green",
    "DaQuan Jeffries",
    "LaMelo Ball",
    "Miles Bridges",
    "Mark Williams",
    "Keon Johnson",
    "Ziaire Williams",
    "D'Angelo Russell",
    "Jalen Wilson",
    "Nic Claxton",
    "Andrew Nembhard",
    "Aaron Nesmith",
    "Tyrese Haliburton",
    "Pascal Siakam",
    "Myles Turner",
    "Jamison Battle",
    "Scottie Barnes",
    "Immanuel Quickley",
    "Jonathan Mogbo",
    "Jakob Poeltl",
    "Brandin Podziemski",
    "Moses Moody",
    "Stephen Curry",
    "Jimmy Butler III",
    "Draymond Green",
    "Coby White",
    "Kevin Huerter",
    "Tre Jones",
    "Matas Buzelis",
    "Nikola Vucevic",
    "Zach LaVine",
    "DeMar DeRozan",
    "Malik Monk",
    "Keegan Murray",
    "Jonas Valanciunas",
    "Taurean Prince",
    "Kyle Kuzma",
    "Damian Lillard",
    "Giannis Antetokounmpo",
    "Brook Lopez",
    "Gabe Vincent",
    "Jordan Goodwin",
    "Shake Milton",
    "Dalton Knecht",
    "Jaxson Hayes"
]







    seasons = ["2024-25"]
    main_folder = "D:/nba_player_current"
    years = ["2024-25"] #old logic was to use the same year for all seasons keeping it because it is not clear if the year is used for anything else
    
    for player in players:
        for season, year in zip(seasons, years):
            run_script(player, season, main_folder, year)
    
    print("All scripts have finished executing.")
