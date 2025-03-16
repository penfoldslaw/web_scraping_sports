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
    # "Jaylen Brown",
    # "Sam Hauser",
    # "Jrue Holiday",
    # "Jayson Tatum",
    # "Kristaps Porziņģis",
    # "Keon Johnson",
    # "Ziaire Williams",
    # "D'Angelo Russell",
    # "Cameron Johnson",
    # "Day'Ron Sharpe",
    # "Cason Wallace",
    # "Luguentz Dort",
    # "Shai Gilgeous-Alexander",
    # "Aaron Wiggins",
    # "Isaiah Hartenstein",
    # "Tim Hardaway Jr.",
    # "Ausar Thompson",
    # "Cade Cunningham",
    # "Tobias Harris",
    # "Jalen Duren",
    # "Coby White",
    # "Kevin Huerter",
    # "Tre Jones",
    # "Matas Buzelis",
    # "Nikola Vucevic",
    # "Jalen Green",
    # "Dillon Brooks",
    # "Fred VanVleet",
    # "Jabari Smith Jr.",
    # "Alperen Sengun",
    # "Duncan Robinson",
    # "Jaime Jaquez Jr.",
    # "Tyler Herro",
    # "Andrew Wiggins",
    # "Bam Adebayo",
    # "Desmond Bane",
    # "Jaylen Wells",
    # "Ja Morant",
    # "Jaren Jackson Jr.",
    # "Zach Edey",
    # "Andrew Nembhard",
    # "Aaron Nesmith",
    # "Tyrese Haliburton",
    # "Pascal Siakam",
    # "Myles Turner",
    # "Taurean Prince",
    # "Kyle Kuzma",
    # "Damian Lillard",
    # "Giannis Antetokounmpo",
    # "Brook Lopez",
    # "Mikal Bridges",
    # "Josh Hart",
    # "Miles McBride",
    # "OG Anunoby",
    # "Karl-Anthony Towns",
    # "Moses Moody",
    # "Jimmy Butler III",
    # "Stephen Curry",
    # "Draymond Green",
    # "Quinten Post",
    # "Khris Middleton",
    # "Justin Champagnie",
    # "Jordan Poole",
    # "Kyshawn George",
    # "Alex Sarr",
    # "Christian Braun",
    # "Michael Porter Jr.",
    # "Jamal Murray",
    # "Aaron Gordon",
    "Nikola Jokic"
    ]



    seasons = ["2024-25"]
    main_folder = "D:/nba_player_current"
    years = ["2024-25"] #old logic was to use the same year for all seasons keeping it because it is not clear if the year is used for anything else
    
    for player in players:
        for season, year in zip(seasons, years):
            run_script(player, season, main_folder, year)
    
    print("All scripts have finished executing.")
