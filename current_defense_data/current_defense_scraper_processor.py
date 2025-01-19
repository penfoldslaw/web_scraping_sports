import subprocess
import sys

def run_script(main_folder, folder_season, data_season):
    # Pass arguments to defense_scraper.py
    subprocess.run(
        [sys.executable, "current_defense_scraper.py", main_folder, folder_season, data_season],
        check=True
    )

if __name__ == "__main__":
    main_folder = "nba_defense_current"
    folder_season = ["2024-25"]
    data_season = ["2024-25"]

    for folder, data in zip(folder_season, data_season):
        print(f"Running script for: folder_season={folder}, data_season={data}")
        run_script(main_folder, folder, data)
    
    print("All scripts have finished executing.")

