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
    "Donovan Mitchell",
    "Sam Merrill",
    "Darius Garland",
    "Evan Mobley",
    "Jarrett Allen",
    "Tim Hardaway Jr.",
    "Ausar Thompson",
    "Dennis Schroder",
    "Tobias Harris",
    "Jalen Duren",
    "Kris Dunn",
    "Norman Powell",
    "James Harden",
    "Kawhi Leonard",
    "Ivica Zubac",
    "Keon Johnson",
    "Ziaire Williams",
    "D'Angelo Russell",
    "Cameron Johnson",
    "Nic Claxton",
    "Josh Green",
    "DaQuan Jeffries",
    "KJ Simpson",
    "Miles Bridges",
    "Mark Williams",
    "Ja'Kobe Walter",
    "Jamison Battle",
    "Immanuel Quickley",
    "Scottie Barnes",
    "Jakob Poeltl",
    "Mikal Bridges",
    "Josh Hart",
    "Tyler Kolek",
    "OG Anunoby",
    "Karl-Anthony Towns",
    "Devin Booker",
    "Ryan Dunn",
    "Collin Gillespie",
    "Kevin Durant",
    "Nick Richards",
    "Anthony Edwards",
    "Jaden McDaniels",
    "Mike Conley",
    "Julius Randle",
    "Rudy Gobert",
    "Brandin Podziemski",
    "Moses Moody",
    "Stephen Curry",
    "Jimmy Butler III",
    "Draymond Green",
    "Jordan Hawkins",
    "Bruce Brown",
    "Jose Alvarado",
    "Kelly Olynyk",
    "Yves Missi",
    "Collin Sexton",
    "Cody Williams",
    "Isaiah Collier",
    "Kyle Filipowski",
    "Walker Kessler",
    "Christian Braun",
    "Michael Porter Jr.",
    "Jamal Murray",
    "Aaron Gordon",
    "Nikola Jokic"
]




    seasons = ["2024-25"]
    main_folder = "D:/nba_player_current"
    years = ["2024-25"] #old logic was to use the same year for all seasons keeping it because it is not clear if the year is used for anything else
    
    for player in players:
        for season, year in zip(seasons, years):
            run_script(player, season, main_folder, year)
    
    print("All scripts have finished executing.")
