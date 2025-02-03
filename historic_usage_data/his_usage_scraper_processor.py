


import subprocess
import sys
from pathlib import Path

def run_script(season, main_folder, year):
    path = Path(__file__).resolve().parent

    subprocess.run([sys.executable,path / "his_usage_scraper.py",season, main_folder, year])

if __name__ == "__main__":
    

    seasons = ["2022-23", "2023-24"]
    main_folder = "D:/nba_usage_historic"
    years = ["2022-23", "2023-24"] #old logic was to use the same year for all seasons keeping it because it is not clear if the year is used for anything else
    
    for season, year in zip(seasons, years):
        run_script(season, main_folder, year)
    
    print("All scripts have finished executing.")