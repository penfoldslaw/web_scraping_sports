import subprocess
import sys

def run_script(main_folder, folder_season, data_season):
    subprocess.run([sys.executable, "defense_scraper.py", main_folder, folder_season, data_season])

if __name__ == "__main__":
    
    main_folder = "nba_defense_historic"
    folder_season = ["2019-20", "2020-21", "2021-22", "2022-23", "2023-24"]
    data_season = ["2019-20", "2020-21", "2021-22", "2022-23", "2023-24"]
    
    for folder, data in zip(folder_season, data_season):
        run_script(main_folder, folder, data)
    
    print("All scripts have finished executing.")