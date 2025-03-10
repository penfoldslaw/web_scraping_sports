import sys
import subprocess
from pathlib import Path
def run_script(sub_folder, csv_sub_folder):
    path = Path(__file__).resolve().parent
    subprocess.run([sys.executable,path / "tracking_parser.py", sub_folder, csv_sub_folder])

if __name__ == "__main__":
    
    sub_folder = ["D:/nba_tracking_html_history/nba_html_2022-23","D:/nba_tracking_html_history/nba_html_2023-24"] 
    csv_sub_folder=["D:/nba_tracking_data_csv/nba_csv_2022-23","D:/nba_tracking_data_csv/nba_csv_2023-24"]
    
    for c_folder, csv_s_folder in zip(sub_folder, csv_sub_folder):
        run_script(c_folder, csv_s_folder)
    
    print("All scripts have finished executing.")