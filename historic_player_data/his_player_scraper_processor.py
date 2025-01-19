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



import subprocess
import sys

def run_script(player, season, main_folder, year):
    subprocess.run([sys.executable, "his_player_scraper.py", player, season, main_folder, year])

if __name__ == "__main__":
    players =[
        'James Harden','Giannis Antetokounmpo','Kawhi Leonard','Luka Doncic','LeBron James','Damian Lillard',
        'Karl-Anthony Towns','Trae Young','Anthony Davis','Russell Westbrook','Bradley Beal','Kyrie Irving','Nikola Jokic',
        'Devin Booker','Joel Embiid','John Collins','Domantas Sabonis','Andre Drummond','Nikola Vucevic','DeMar DeRozan',
        'Jusuf Nurkic','Zach LaVine','Ben Simmons','Brandon Ingram','Jayson Tatum','Jimmy Butler','Pascal Siakam','DAngelo Russell',
        'Deandre Ayton','Kyle Lowry','Bam Adebayo','Stephen Curry','Khris Middleton','Kristaps Porzingis','Donovan Mitchell',
        'Rudy Gobert','DeAaron Fox','Jrue Holiday','Paul George','Chris Paul','CJ McCollum','Clint Capela','Zion Williamson','LaMarcus Aldridge',
        'Julius Randle','Andrew Wiggins','Tobias Harris','Kevin Love','Spencer Dinwiddie' ]
    

    seasons = ["2019-20", "2020-21", "2021-22", "2022-23", "2023-24"]
    main_folder = "nba_player_historic"
    years = ["2019-20", "2020-21", "2021-22", "2022-23", "2023-24"] #old logic was to use the same year for all seasons keeping it because it is not clear if the year is used for anything else
    
    for player in players:
        for season, year in zip(seasons, years):
            run_script(player, season, main_folder, year)
    
    print("All scripts have finished executing.")