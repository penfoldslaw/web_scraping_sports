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
    "Duncan Robinson",
    "Andrew Wiggins",
    "Tyler Herro",
    "Bam Adebayo",
    "Kel'el Ware",
    "Mikal Bridges",
    "Josh Hart",
    "Miles McBride",
    "OG Anunoby",
    "Karl-Anthony Towns",
    "Quentin Grimes",
    "Ricky Council IV",
    "Jared Butler",
    "Justin Edwards",
    "Guerschon Yabusele",
    "Jalen Green",
    "Dillon Brooks",
    "Fred VanVleet",
    "Tari Eason",
    "Alperen Sengun",
    "Andrew Nembhard",
    "Bennedict Mathurin",
    "Tyrese Haliburton",
    "Aaron Nesmith",
    "Myles Turner",
    "Anthony Edwards",
    "Jaden McDaniels",
    "Mike Conley",
    "Julius Randle",
    "Rudy Gobert",
    "Tim Hardaway Jr.",
    "Ausar Thompson",
    "Cade Cunningham",
    "Tobias Harris",
    "Jalen Duren",
    "Trey Murphy III",
    "Zion Williamson",
    "CJ McCollum",
    "Kelly Olynyk",
    "Yves Missi",
    "Coby White",
    "Kevin Huerter",
    "Tre Jones",
    "Matas Buzelis",
    "Nikola Vucevic",
    "Johnny Juzang",
    "Cody Williams",
    "Isaiah Collier",
    "Lauri Markkanen",
    "Walker Kessler",
    "Moses Moody",
    "Jimmy Butler III",
    "Stephen Curry",
    "Gui Santos",
    "Draymond Green",
    "RJ Barrett",
    "Ochai Agbaji",
    "Immanuel Quickley",
    "Scottie Barnes",
    "Jakob Poeltl",
    "Devin Booker",
    "Ryan Dunn",
    "Tyus Jones",
    "Kevin Durant",
    "Nick Richards",
    "Desmond Bane",
    "Jaylen Wells",
    "Luke Kennard",
    "Jaren Jackson Jr.",
    "Zach Edey",
    "Zach LaVine",
    "DeMar DeRozan",
    "Malik Monk",
    "Keegan Murray",
    "Domantas Sabonis",
    "Khris Middleton",
    "Justin Champagnie",
    "Jordan Poole",
    "Kyshawn George",
    "Alex Sarr",
    "Shaedon Sharpe",
    "Toumani Camara",
    "Anfernee Simons",
    "Deni Avdija",
    "Donovan Clingan",
    "Stephon Castle",
    "Devin Vassell",
    "Chris Paul",
    "Harrison Barnes",
    "Bismack Biyombo",
    "Austin Reaves",
    "Jordan Goodwin",
    "Luka Doncic",
    "Dorian Finney-Smith",
    "Jaxson Hayes"
]




    seasons = ["2024-25"]
    main_folder = "D:/nba_player_current"
    years = ["2024-25"] #old logic was to use the same year for all seasons keeping it because it is not clear if the year is used for anything else
    
    for player in players:
        for season, year in zip(seasons, years):
            run_script(player, season, main_folder, year)
    
    print("All scripts have finished executing.")
