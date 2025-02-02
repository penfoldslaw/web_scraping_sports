# import subprocess
# import sys

# def run_script(main_folder, folder_season, data_season):
#     # Pass arguments to defense_scraper.py
#     subprocess.run(
#         [sys.executable, "defense_scraper.py", main_folder, folder_season, data_season],
#         check=True
#     )

# if __name__ == "__main__":
#     main_folder = "D:/nba_defense_historic"
#     folder_season = ["2019-20", "2020-21", "2021-22", "2022-23", "2023-24"]
#     data_season = ["2019-20", "2020-21", "2021-22", "2022-23", "2023-24"]

#     for folder, data in zip(folder_season, data_season):
#         print(f"Running script for: folder_season={folder}, data_season={data}")
#         run_script(main_folder, folder, data)
    
#     print("All scripts have finished executing.")




from pathlib import Path
from his_defense_scraper import defense_scraper  # Assuming this is the function inside the script

def run_script(main_folder, folder_season, data_season):
    # Directly call the function from the other script
    defense_scraper(main_folder, folder_season, data_season)

if __name__ == "__main__":
    main_folder = "D:/nba_defense_historic"
    folder_season = ["2022-23", "2023-24"]
    data_season = ["2022-23", "2023-24"]

    for folder, data in zip(folder_season, data_season):
        print(f"Running script for: folder_season={folder}, data_season={data}")
        run_script(main_folder, folder, data)
    
    print("All scripts have finished executing.")

