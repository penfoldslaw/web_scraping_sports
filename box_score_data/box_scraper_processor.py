import subprocess
import sys
from pathlib import Path

def run_script(http,matchup,main_folder,date_of_match):
    path = Path(__file__).resolve().parent
    # print("this is what you are looking for",path / "box_scraper.py")
    subprocess.run([sys.executable,path / "box_scraper.py",http, matchup, main_folder, date_of_match]) 


if __name__ == "__main__":
    import re

    https = [

        "https://www.nba.com/game/hou-vs-lal-0022401096/box-score"

    ]

    matchups = []
    pattern = re.compile(r"/game/([a-z]{3}-vs-[a-z]{3})")

    for http in https:
        match = pattern.search(http)
        if match:
            matchups.append(match.group(1))


    main_folder = "D:/box_score_data/box_score_html"  # Changed to string
    date_of_match = "3-31-25"  # Changed to string

    # for http in https:
    #     for matchup in matchups:
    #         run_script(http, matchup, main_folder, date_of_match)

    for http, matchup in zip(https, matchups):
        run_script(http, matchup, main_folder, date_of_match)

    
    print("All scripts have finished executing.")



