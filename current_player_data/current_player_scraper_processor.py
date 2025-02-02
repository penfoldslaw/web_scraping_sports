from pathlib import Path
from current_player_scraper import scrape_data  # Assuming this function exists

def run_script(player, season, main_folder, year):
    # Directly call the function instead of using subprocess
    scrape_data(player, season, main_folder, year)

if __name__ == "__main__":
    players = ['Shai Gilgeous-Alexander', 'Cason Wallace', 'Alex Caruso', 'Jalen Williams', 'Isaiah Hartenstein']
    seasons = ["2024-25"]
    main_folder = "D:/nba_player_current"
    years = ["2024-25"]  # Keeping this as is in case it's used elsewhere

    for player in players:
        for season, year in zip(seasons, years):
            run_script(player, season, main_folder, year)

    print("All scripts have finished executing.")
