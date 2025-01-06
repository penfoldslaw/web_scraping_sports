import sys
import subprocess
def run_script(relative_path, csv_path):
    subprocess.run([sys.executable, "player_parser.py", relative_path, csv_path])

if __name__ == "__main__":

    season = "2021-22"
    relative_path = [
        r"nba_player_historic\nba_html_{season}".format(season=season), 
        r"nba_player_historic\nba_html_{season}\quarter_data\q1".format(season=season), 
        r"nba_player_historic\nba_html_{season}\quarter_data\q2".format(season=season), 
        r"nba_player_historic\nba_html_{season}\quarter_data\q3".format(season=season), 
        r"nba_player_historic\nba_html_{season}\quarter_data\q4".format(season=season)]
     
    csv_path = [
       r"nba_ph_csv\season_{season}\all_quarters".format(season=season), 
        r"nba_ph_csv\season_{season}\quarter_data\q1".format(season=season), 
        r"nba_ph_csv\season_{season}\quarter_data\q2".format(season=season), 
        r"nba_ph_csv\season_{season}\quarter_data\q3".format(season=season), 
        r"nba_ph_csv\season_{season}\quarter_data\q4".format(season=season)]
    
    for r_folder, csv__folder in zip(relative_path, csv_path):
        #print(r_folder, csv__folder)
        run_script(r_folder, csv__folder)
    
    print("All scripts have finished executing.")