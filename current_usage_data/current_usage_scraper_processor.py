








import subprocess
import sys
from pathlib import Path


def run_script(season, main_folder, year):
    path = Path().resolve()
    subprocess.run([sys.executable,path / "current_usage_scraper.py",season, main_folder, year])

if __name__ == "__main__":
    

    seasons = ["2024-25"]
    main_folder = "D:/nba_usage_current"
    years = ["2024-25"] #old logic was to use the same year for all seasons keeping it because it is not clear if the year is used for anything else
    
    for season, year in zip(seasons, years):
        run_script(season, main_folder, year)
    
    print("All scripts have finished executing.")