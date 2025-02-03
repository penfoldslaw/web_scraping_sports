# from pathlib import Path
# from current_usage_scraper import scrape_data  # Assuming this function exists

# def run_script(season, main_folder, year):
#     # Directly call the function instead of using subprocess
#     scrape_data(season, main_folder, year)

# if __name__ == "__main__":
#     seasons = ["2024-25"]
#     main_folder = "D:/nba_usage_current"
#     years = ["2024-25"]  # Keeping this as is in case it's used elsewhere

#     for season, year in zip(seasons, years):
#         run_script(season, main_folder, year)

#     print("All scripts have finished executing.")


import subprocess
import sys
from pathlib import Path

def run_script(season, main_folder, year):
    path = Path(__file__).resolve().parent
    subprocess.run([sys.executable,path / "current_usage_scraper.py",season, main_folder, year])

if __name__ == "__main__":
    

    seasons = ["2024-25"]
    main_folder = "D:/nba_usage_current"
    years = ["2024-25"] #old logic was to use the same year for all seasons keeping it because it is not clear if the year is used for anything else
    
    for season, year in zip(seasons, years):
        run_script(season, main_folder, year)
    
    print("All scripts have finished executing.")