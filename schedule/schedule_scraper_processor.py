import subprocess
import sys

def run_script(team, year):

    subprocess.run(
        [sys.executable, "schedule_scraper.py", team, year],
        check=True
    )

if __name__ == "__main__":
    teams = [ 
        'ATL', 'BOS', 'BKN', 'CHA', 'CHI', 'CLE', 'DAL', 'DEN', 'DET', 
        'GSW', 'HOU', 'IND', 'LAC', 'LAL', 'MEM', 'MIA', 'MIL', 'MIN', 
        'NO', 'NYK', 'OKC', 'ORL', 'PHI', 'PHX', 'POR', 'SAC', 'SAS', 
        'TOR', 'UTAH', 'WAS' ]
    
    year = "2025"

    for team in teams:
        print(f"Running script for: folder_season={team}, data_season={year}")
        run_script(team, year)
    
    print("All scripts have finished executing.")

