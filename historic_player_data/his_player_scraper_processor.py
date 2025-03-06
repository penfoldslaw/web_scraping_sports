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



# import asyncio
# import sys

# async def run_script(player, season, year):
#     process = await asyncio.create_subprocess_exec(
#         sys.executable, "scraper.py", player, season, year,
#         stdout=asyncio.subprocess.PIPE,
#         stderr=asyncio.subprocess.PIPE
#     )
#     stdout, stderr = await process.communicate()
#     if process.returncode == 0:
#         print(f"{player}: Completed successfully")
#     else:
#         print(f"{player}: Error occurred: {stderr.decode()}")

# async def main():
#     players =[
#         'James Harden',
#         'Giannis Antetokounmpo',
#         'Luka Doncic',
#         'LeBron James',
#         'Damian Lillard',
#         'Karl-Anthony Towns',
#         'Trae Young',
#         'Anthony Davis',
#         'Russell Westbrook',
#         'Bradley Beal',
#         'Kyrie Irving',
#         'Kawhi Leonard',
#         'Nikola Jokic',
#         'Devin Booker',
#         'Joel Embiid',
#         'John Collins',
#         'Domantas Sabonis',
#         'Andre Drummond',
#         'Nikola Vucevic',
#         'DeMar DeRozan',
#         'Jusuf Nurkic',
#         'Zach LaVine',
#         'Ben Simmons',
#         'Brandon Ingram',
#         'Jayson Tatum',
#         'Jimmy Butler',
#         'Pascal Siakam',
#         'Hassan Whiteside',
#         'DAngelo Russell',
#         'Deandre Ayton',
#         'Kyle Lowry',
#         'Bam Adebayo',
#         'Stephen Curry',
#         'Khris Middleton',
#         'Kristaps Porzingis',
#         'Donovan Mitchell',
#         'Rudy Gobert',
#         'DeAaron Fox',
#         'Jrue Holiday',
#         'Paul George',
#         'Chris Paul',
#         'CJ McCollum',
#         'Clint Capela',
#         'Zion Williamson',
#         'LaMarcus Aldridge',
#         'Julius Randle',
#         'Andrew Wiggins',
#         'Tobias Harris',
#         'Kevin Love',
#         'Spencer Dinwiddie'
# ]

#     season = "'2019-20'"
#     year = "2019"
    
#     tasks = [run_script(player, season, year) for player in players]
#     await asyncio.gather(*tasks)

# if __name__ == "__main__":
#     asyncio.run(main())


BYK = ['Cam Thomas', 'Cameron Johnson', "D'Angelo Russell"]
NYK = ['Jalen Brunson', 'Karl-Anthony Towns', 'Mikal Bridges']

POR = ['Shaedon Sharpe', 'Anfernee Simons', 'Jerami Grant']
MIA = ['Tyler Herro', 'Jimmy Butler', 'Bam Adebayo']

TOR = ['RJ Barrett', 'Scottie Barnes', 'Immanuel Quickely']
ORL = ['Paolo Banchero', 'Franz Wagner', 'Jalen Suggs']

PHI = ['Tyrese Maxey', 'Joel Embiid', 'Paul Geroge']
DEN = ['Nikola Jokic', 'Jamal Murray', 'Michael Porter Jr']

WAS = ['Jordan Poole', 'Kyle Kuzma', 'Malcolm Brogdon']
LAL = ['Anthony Davis', 'LeBron James', 'Austin Reaves']

OKC = ['Shai Gilgeous-Alexander', 'Cason Wallace', 'Alex Caruso', 'Jalen Williams', 'Isaiah Hartenstein']

bos = ['Derrick White', 'Jayson Tatum', 'Kristaps Porzingis']

sas = ['Chris Paul',"De'Aaron Fox", "Devin Vassell","Harrison Barnes", "Victor Wembanyama"]

players_past = [
    "Giannis Antetokounmpo",
    "Trae Young",
    "Damian Lillard",
    "Dyson Daniels",
    "Brook Lopez",
    "Taurean Prince",
    "Onyeka Okongwu",
    "Jalen Brunson",
    "Karl-Anthony Towns",
    "Mikal Bridges",
    "Moses Moody",
    "Stephen Curry",
    "Josh Hart",
    "Brandin Podziemski",
    "OG Anunoby",
    "Draymond Green",
    "Paolo Banchero",
    "Franz Wagner",
    "Jakob Poeltl",
    "Immanuel Quickley",
    "Scottie Barnes",
    "RJ Barrett",
    "Wendell Carter Jr.",
    "Cole Anthony",
    "Kentavious Caldwell-Pope",
    "Ja'Kobe Walter",
    "Donovan Mitchell",
    "Darius Garland",
    "Jarrett Allen",
    "Josh Giddey",
    "Coby White",
    "Matas Buzelis",
    "Max Strus",
    "Dean Wade",
    "Zach Collins",
    "Lonzo Ball"]





import subprocess
import sys
from pathlib import Path

def run_script(player, season, main_folder, year, quarter_data):
    path = Path(__file__).resolve().parent
    subprocess.run([sys.executable,path / "his_player_scraper.py", player, season, main_folder, year, quarter_data])

if __name__ == "__main__":
    players = [
    "Jonas Valanciunas",
    "Jamal Murray",
    "DeMar DeRozan",
    "Michael Porter Jr.",
    "Christian Braun",
    "Keegan Murray",
    "Aaron Gordon",
    "Russell Westbrook",
    "Keon Ellis",
    "Trey Lyles",
    "Markelle Fultz",
    "Jake LaRavia",
    "Shai Gilgeous-Alexander",
    "Desmond Bane",
    "Jalen Williams",
    "Ja Morant",
    "Santi Aldama",
    "Jaylen Wells",
    "Aaron Wiggins",
    "Isaiah Hartenstein",
    "Cason Wallace",
    "Brandon Clarke",
    "Luguentz Dort",
    "Isaiah Joe",
    "Zach Edey",
    "Kenrich Williams",
    "James Harden",
    "Malik Beasley",
    "Ivica Zubac",
    "Bogdan Bogdanovic",
    "Ausar Thompson",
    "Jalen Duren",
    "Amir Coffey",
    "Tim Hardaway Jr.",
    "Dennis Schroder",
    "Kris Dunn",
    "Ron Holland II",
    "Isaiah Stewart"
                        ]




    

    seasons = [ "2022-23", "2023-24"]
    main_folder = "D:/nba_player_historic"
    years = ["2022-23", "2023-24"] #old logic was to use the same year for all seasons keeping it because it is not clear if the year is used for anything else
    
    for player in players:
        for season, year in zip(seasons, years):
            # run_script(player, season, main_folder, year,'yes')
            run_script(player, season, main_folder, year,'no')
    
    print("All scripts have finished executing.")