import subprocess
import sys
from pathlib import Path

def run_script(http,matchup,main_folder,date_of_match):
    path = Path(__file__).resolve().parent
    # print("this is what you are looking for",path / "box_scraper.py")
    subprocess.run([sys.executable,path / "box_scraper.py",http, matchup, main_folder, date_of_match]) 


if __name__ == "__main__":
    https = [
        "https://www.nba.com/game/nyk-vs-gsw-0022400974/box-score",
        "https://www.nba.com/game/ind-vs-mil-0022400972/box-score",
        "https://www.nba.com/game/okc-vs-det-0022400969/box-score",
        "https://www.nba.com/game/mia-vs-mem-0022400971/box-score",
        "https://www.nba.com/game/chi-vs-hou-0022400970/box-score",
        "https://www.nba.com/game/was-vs-den-0022400975/box-score"
    ]
    
    matchups = ["nyk-vs-gsw", "ind-vs-mil", "okc-vs-det","mia-vs-mem","chi-vs-hou", "was-vs-den"]
    main_folder = "D:/box_score_data/box_score_html"  # Changed to string
    date_of_match = "3-15-25"  # Changed to string

    # for http in https:
    #     for matchup in matchups:
    #         run_script(http, matchup, main_folder, date_of_match)

    for http, matchup in zip(https, matchups):
        run_script(http, matchup, main_folder, date_of_match)

    
    print("All scripts have finished executing.")



