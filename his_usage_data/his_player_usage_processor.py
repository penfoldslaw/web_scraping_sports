








import subprocess
import sys

def run_script(season, main_folder, year):
    subprocess.run([sys.executable, "his_usage_scraper.py",season, main_folder, year])

if __name__ == "__main__":
    

    seasons = ["2019-20", "2020-21", "2021-22", "2022-23", "2023-24"]
    main_folder = "nba_usage_historic"
    years = ["2019-20", "2020-21", "2021-22", "2022-23", "2023-24"] #old logic was to use the same year for all seasons keeping it because it is not clear if the year is used for anything else
    
    for season, year in zip(seasons, years):
        run_script(season, main_folder, year)
    
    print("All scripts have finished executing.")