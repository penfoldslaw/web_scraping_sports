from schedule_scraper import schedule_scraper  # Assuming this function exists

def run_script(team, year):
    # Directly call the function instead of using subprocess
    schedule_scraper(team, year)

if __name__ == "__main__":
    teams = [
        'ATL', 'BOS', 'BKN', 'CHA', 'CHI', 'CLE', 'DAL', 'DEN', 'DET', 
        'GSW', 'HOU', 'IND', 'LAC', 'LAL', 'MEM', 'MIA', 'MIL', 'MIN', 
        'NO', 'NYK', 'OKC', 'ORL', 'PHI', 'PHX', 'POR', 'SAC', 'SAS', 
        'TOR', 'UTAH', 'WAS'
    ]
    
    year = "2025"

    for team in teams:
        print(f"Running script for: team={team}, year={year}")
        run_script(team, year)

    print("All scripts have finished executing.")


