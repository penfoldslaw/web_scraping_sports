# import subprocess
# import sys
# from pathlib import Path


# def run_script(main_folder, folder_season, data_season):
#     # Pass arguments to defense_scraper.py
#     subprocess.run(
#         [sys.executable, "current_defense_scraper.py", main_folder, folder_season, data_season],
#         check=True
#     )

# if __name__ == "__main__":
#     main_folder = "D:/nba_defense_current"
#     folder_season = ["2024-25"]
#     data_season = ["2024-25"]

#     for folder, data in zip(folder_season, data_season):
#         print(f"Running script for: folder_season={folder}, data_season={data}")
#         run_script(main_folder, folder, data)
    
#     print("All scripts have finished executing.")





from pathlib import Path
from current_defense_scraper import defense_scraper  # Assuming this is the function inside the script

def run_script(main_folder, folder_season, data_season):
    # Directly call the function from the other script
    defense_scraper(main_folder, folder_season, data_season)

if __name__ == "__main__":
    main_folder = "D:/nba_defense_current"
    folder_season = ["2024-25"]
    data_season = ["2024-25"]

    for folder, data in zip(folder_season, data_season):
        print(f"Running script for: folder_season={folder}, data_season={data}")
        run_script(main_folder, folder, data)
    
    print("All scripts have finished executing.")
