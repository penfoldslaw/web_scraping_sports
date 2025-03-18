import threading
import subprocess
import sys
from pathlib import Path

def run_script(relative_path, csv_path):
    path = Path(__file__).resolve().parent

    subprocess.run([sys.executable, path / "his_player_parser.py", relative_path, csv_path])

if __name__ == "__main__":

    seasons = ["2022-23", "2023-24"]
    for season in seasons:
        relative_path = [
            r"D:\nba_player_historic\nba_html_{season}".format(season=season)
            # r"D:\nba_player_historic\nba_html_{season}\quarter_data\q1".format(season=season), 
            # r"D:\nba_player_historic\nba_html_{season}\quarter_data\q2".format(season=season), 
            # r"D:\nba_player_historic\nba_html_{season}\quarter_data\q3".format(season=season), 
            # r"D:\nba_player_historic\nba_html_{season}\quarter_data\q4".format(season=season)
            ]
        
        csv_path = [
            r"D:\nba_player_csv_historic\season_{season}\all_quarters".format(season=season)
            # r"D:\nba_player_csv_historic\season_{season}\quarter_data\q1".format(season=season), 
            # r"D:\nba_player_csv_historic\season_{season}\quarter_data\q2".format(season=season), 
            # r"D:\nba_player_csv_historic\season_{season}\quarter_data\q3".format(season=season), 
            # r"D:\nba_player_csv_historic\season_{season}\quarter_data\q4".format(season=season)
            ]
    
        threads = []
        for r_folder, csv__folder in zip(relative_path, csv_path):
            #run_script(r_folder, csv__folder)

            thread = threading.Thread(target=run_script, args=(r_folder, csv__folder))
            threads.append(thread)
            thread.start()
        #print(r_folder, csv__folder)
        
        for thread in threads:
            thread.join()
        
        print(f"{season} script have finished executing.")





# import threading
# import subprocess
# import sys

# def run_script(player, season, year):
#     subprocess.run([sys.executable, "scraper.py", player, season, year])

# if __name__ == "__main__":
#     players = [
#     'James Harden',
#     'Giannis Antetokounmpo',
#     'Luka Doncic',
#     'LeBron James',
#     'Damian Lillard',
#     'Karl-Anthony Towns',
#     'Trae Young',
#     'Anthony Davis',
#     'Russell Westbrook',
#     'Bradley Beal',
#     'Kyrie Irving',
#     'Kawhi Leonard',
#     'Nikola Jokic',
#     'Devin Booker',
#     'Joel Embiid',
#     'John Collins',
#     'Domantas Sabonis',
#     'Andre Drummond',
#     'Nikola Vucevic',
#     'DeMar DeRozan',
#     'Jusuf Nurkic',
#     'Zach LaVine',
#     'Ben Simmons',
#     'Brandon Ingram',
#     'Jayson Tatum',
#     'Jimmy Butler',
#     'Pascal Siakam',
#     'Hassan Whiteside',
#     'DAngelo Russell',
#     'Deandre Ayton',
#     'Kyle Lowry',
#     'Bam Adebayo',
#     'Stephen Curry',
#     'Khris Middleton',
#     'Kristaps Porzingis',
#     'Donovan Mitchell',
#     'Rudy Gobert',
#     'DeAaron Fox',
#     'Jrue Holiday',
#     'Paul George',
#     'Chris Paul',
#     'CJ McCollum',
#     'Clint Capela',
#     'Zion Williamson',
#     'LaMarcus Aldridge',
#     'Julius Randle',
#     'Andrew Wiggins',
#     'Tobias Harris',
#     'Kevin Love',
#     'Spencer Dinwiddie'
# ]

#     season = "'2019-20'"
#     year = "2019"

#     threads = []
#     for player in players:
#         thread = threading.Thread(target=run_script, args=(player, season, year))
#         threads.append(thread)
#         thread.start()

#     for thread in threads:
#         thread.join()

#     print("scripts have finished executing.")