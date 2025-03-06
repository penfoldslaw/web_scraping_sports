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
    "Jonas Valanciunas",
    "Jamal Murray",
    "DeMar DeRozan",
    "Michael Porter Jr.",
    "Christian Braun",
    "Keegan Murray",
    "Aaron Gordon",
    "Russell Westbrook",
    "Keon Ellis",
    "Trey Lyles",
    "Markelle Fultz",
    "Jake LaRavia",
    "Shai Gilgeous-Alexander",
    "Desmond Bane",
    "Jalen Williams",
    "Ja Morant",
    "Santi Aldama",
    "Jaylen Wells",
    "Aaron Wiggins",
    "Isaiah Hartenstein",
    "Cason Wallace",
    "Brandon Clarke",
    "Luguentz Dort",
    "Isaiah Joe",
    "Zach Edey",
    "Kenrich Williams",
    "James Harden",
    "Malik Beasley",
    "Ivica Zubac",
    "Bogdan Bogdanovic",
    "Ausar Thompson",
    "Jalen Duren",
    "Amir Coffey",
    "Tim Hardaway Jr.",
    "Dennis Schroder",
    "Kris Dunn",
    "Ron Holland II",
    "Isaiah Stewart"
                        ]

    seasons = ["2024-25"]
    main_folder = "D:/nba_player_current"
    years = ["2024-25"] #old logic was to use the same year for all seasons keeping it because it is not clear if the year is used for anything else
    
    for player in players:
        for season, year in zip(seasons, years):
            run_script(player, season, main_folder, year)
    
    print("All scripts have finished executing.")
