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
    "Jrue Holiday",
    "Derrick White",
    "Jaylen Brown",
    "Jayson Tatum",
    "Kristaps Porzingis",
    "Al Horford",
    "Payton Pritchard",
    "Sam Hauser",
    "Luke Kornet",
    "Torrey Craig",
    "Xavier Tillman",
    "Neemias Queta",
    "Baylor Scheierman",
    "Davion Mitchell",
    "Tyler Herro",
    "Andrew Wiggins",
    "Bam Adebayo",
    "Kel'el Ware",
    "Terry Rozier",
    "Duncan Robinson",
    "Haywood Highsmith",
    "Jaime Jaquez",
    "Pelle Larsson",
    "Kyle Anderson",
    "Kevin Love",
    "Keshad Johnson",
    "James Harden",
    "Kris Dunn",
    "Bogdan Bogdanovic",
    "Kawhi Leonard",
    "Ivica Zubac",
    "Nicolas Batum",
    "Derrick Jones Jr.",
    "Amir Coffey",
    "Ben Simmons",
    "Drew Eubanks",
    "Patty Mills",
    "Jordan Miller",
    "Kobe Brown",
    "Trae Young",
    "Dyson Daniels",
    "Mouhamed Gueye",
    "Zaccharie Risacher",
    "Onyeka Okongwu",
    "Caris LeVert",
    "Georges Niang",
    "Clint Capela",
    "Terance Mann",
    "Garrison Mathews",
    "Vit Krejci",
    "Dominick Barlow",
    "LaMelo Ball",
    "DaQuan Jeffries",
    "Josh Green",
    "Miles Bridges",
    "Mark Williams",
    "Jusuf Nurkic",
    "Nick Smith",
    "Moussa Diabate",
    "Damion Baugh",
    "Marcus Garrett",
    "Seth Curry",
    "Taj Gibson",
    "Wendell Moore",
    "Malachi Flynn",
    "Chris Paul",
    "Stephon Castle",
    "Devin Vassell",
    "Harrison Barnes",
    "Bismack Biyombo",
    "Jeremy Sochan",
    "Keldon Johnson",
    "Blake Wesley",
    "Malaki Branham",
    "Julian Champagnie",
    "Sandro Mamukelashvili",
    "Jordan McLaughlin"
    ]


    seasons = ["2024-25"]
    main_folder = "D:/nba_player_current"
    years = ["2024-25"] #old logic was to use the same year for all seasons keeping it because it is not clear if the year is used for anything else
    
    for player in players:
        for season, year in zip(seasons, years):
            run_script(player, season, main_folder, year)
    
    print("All scripts have finished executing.")
