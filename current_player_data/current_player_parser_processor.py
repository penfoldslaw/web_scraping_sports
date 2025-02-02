# import threading
# import subprocess
# import sys
# from pathlib import Path


# def run_script(relative_path, csv_path):
#     path = Path().resolve()
#     subprocess.run([sys.executable,path / "current_player_parser.py", relative_path, csv_path])

# if __name__ == "__main__":

#     seasons = ["2024-25"]
#     for season in seasons:
#         relative_path = [
#             r"D:\nba_player_current\nba_html_{season}".format(season=season), 
#             r"D:\nba_player_current\nba_html_{season}\quarter_data\q1".format(season=season), 
#             r"D:\nba_player_current\nba_html_{season}\quarter_data\q2".format(season=season), 
#             r"D:\nba_player_current\nba_html_{season}\quarter_data\q3".format(season=season), 
#             r"D:\nba_player_current\nba_html_{season}\quarter_data\q4".format(season=season)]
        
#         csv_path = [
#             r"D:\nba_ph_csv_current\season_{season}\all_quarters".format(season=season), 
#             r"D:\nba_ph_csv_current\season_{season}\quarter_data\q1".format(season=season), 
#             r"D:\nba_ph_csv_current\season_{season}\quarter_data\q2".format(season=season), 
#             r"D:\nba_ph_csv_current\season_{season}\quarter_data\q3".format(season=season), 
#             r"D:\nba_ph_csv_current\season_{season}\quarter_data\q4".format(season=season)]
    
#         threads = []
#         for r_folder, csv__folder in zip(relative_path, csv_path):
#             #run_script(r_folder, csv__folder)

#             thread = threading.Thread(target=run_script, args=(r_folder, csv__folder))
#             threads.append(thread)
#             thread.start()
#         #print(r_folder, csv__folder)
        
#         for thread in threads:
#             thread.join()
        
#         print(f"{season} script have finished executing.")



import threading
from pathlib import Path
from current_player_parser import create_dataframe  # Assuming this function exists

def run_script(relative_path, csv_path):
    # Directly call the function from current_player_parser.py
    create_dataframe(relative_path, csv_path)

if __name__ == "__main__":
    seasons = ["2024-25"]
    
    for season in seasons:
        relative_path = [
            rf"D:\nba_player_current\nba_html_{season}", 
            rf"D:\nba_player_current\nba_html_{season}\quarter_data\q1", 
            rf"D:\nba_player_current\nba_html_{season}\quarter_data\q2", 
            rf"D:\nba_player_current\nba_html_{season}\quarter_data\q3", 
            rf"D:\nba_player_current\nba_html_{season}\quarter_data\q4"
        ]
        
        csv_path = [
            rf"D:\nba_player_csv_current\season_{season}\all_quarters", 
            rf"D:\nba_player_csv_current\season_{season}\quarter_data\q1", 
            rf"D:\nba_player_csv_current\season_{season}\quarter_data\q2", 
            rf"D:\nba_player_csv_current\season_{season}\quarter_data\q3", 
            rf"D:\nba_player_csv_current\season_{season}\quarter_data\q4"
        ]
    
        threads = []
        for r_folder, csv_folder in zip(relative_path, csv_path):
            thread = threading.Thread(target=run_script, args=(r_folder, csv_folder))
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()
        
        print(f"{season} script has finished executing.")
