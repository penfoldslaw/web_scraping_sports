import threading
import subprocess
import sys

def run_script(relative_path, csv_path):
    subprocess.run([sys.executable, "his_player_parser.py", relative_path, csv_path])

if __name__ == "__main__":

    seasons = ["2024-25"]
    for season in seasons:
        relative_path = [
            r"nba_player_current\nba_html_{season}".format(season=season), 
            r"nba_player_current\nba_html_{season}\quarter_data\q1".format(season=season), 
            r"nba_player_current\nba_html_{season}\quarter_data\q2".format(season=season), 
            r"nba_player_current\nba_html_{season}\quarter_data\q3".format(season=season), 
            r"nba_player_current\nba_html_{season}\quarter_data\q4".format(season=season)]
        
        csv_path = [
            r"nba_ph_csv\season_{season}\all_quarters".format(season=season), 
            r"nba_ph_csv\season_{season}\quarter_data\q1".format(season=season), 
            r"nba_ph_csv\season_{season}\quarter_data\q2".format(season=season), 
            r"nba_ph_csv\season_{season}\quarter_data\q3".format(season=season), 
            r"nba_ph_csv\season_{season}\quarter_data\q4".format(season=season)]
    
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