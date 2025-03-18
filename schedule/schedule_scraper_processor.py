# from schedule_scraper import schedule_scraper  # Assuming this function exists

# def run_script(team, year):
#     # Directly call the function instead of using subprocess
#     schedule_scraper(team, year)

# if __name__ == "__main__":
#     teams = [
#         'ATL', 'BOS', 'BKN', 'CHA', 'CHI', 'CLE', 'DAL', 'DEN', 'DET', 
#         'GSW', 'HOU', 'IND', 'LAC', 'LAL', 'MEM', 'MIA', 'MIL', 'MIN', 
#         'NO', 'NYK', 'OKC', 'ORL', 'PHI', 'PHX', 'POR', 'SAC', 'SAS', 
#         'TOR', 'UTAH', 'WAS'
#     ]
    
#     year = "2025"

#     for team in teams:
#         print(f"Running script for: team={team}, year={year}")
#         run_script(team, year)

#     print("All scripts have finished executing.")


import subprocess
import sys
from pathlib import Path

def run_script(team, year):
    path = Path(__file__).resolve().parent

    subprocess.run([sys.executable,path / "schedule_scraper.py", team, year],check=True)

if __name__ == "__main__":
    teams = [ 
        'ATL', 'BOS', 'BKN', 'CHA', 'CHI', 'CLE', 'DAL', 'DEN', 'DET', 
        'GSW', 'HOU', 'IND', 'LAC', 'LAL', 'MEM', 'MIA', 'MIL', 'MIN', 
        'NO', 'NYK', 'OKC', 'ORL', 'PHI', 'PHX', 'POR', 'SAC', 'SAS', 
        'TOR', 'UTAH', 'WAS' ]
    
    year = "2025"

    for team in teams:
        # print(f"Running script for: folder_season={team}, data_season={year}")
        run_script(team, year)
    
    print("All scripts have finished executing.")


