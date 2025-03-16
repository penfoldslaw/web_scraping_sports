import subprocess
import sys
from pathlib import Path

def run_script(http,matchup,main_folder,date_of_match):
    path = Path(__file__).resolve().parent
    # print("this is what you are looking for",path / "box_scraper.py")
    subprocess.run([sys.executable,path / "box_scraper.py",http, matchup, main_folder, date_of_match]) 


if __name__ == "__main__":
    https = [
        "https://www.nba.com/game/bos-vs-mia-0022400958/box-score",
        "https://www.nba.com/game/lac-vs-atl-0022400960/box-score",
        "https://www.nba.com/game/cha-vs-sas-0022400964/box-score"
    ]
    
    matchups = ["bos-mia", "lac-atl", "cha-sas"]
    main_folder = "D:/box_score_data/box_score_html"  # Changed to string
    date_of_match = "3-14-25"  # Changed to string

    # for http in https:
    #     for matchup in matchups:
    #         run_script(http, matchup, main_folder, date_of_match)

    for http, matchup in zip(https, matchups):
        run_script(http, matchup, main_folder, date_of_match)

    
    print("All scripts have finished executing.")



