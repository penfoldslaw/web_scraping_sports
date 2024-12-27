import threading
import subprocess
import sys

def run_script(player, season, year):
    subprocess.run([sys.executable, "scraper.py", player, season, year])

if __name__ == "__main__":
    players = ["Joel Embiid", "DAngelo Russell"]
    season = "'2019-20'"
    year = "2019"

    threads = []
    for player in players:
        thread = threading.Thread(target=run_script, args=(player, season, year))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Both scripts have finished executing.")

