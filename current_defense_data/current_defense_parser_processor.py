import sys
import subprocess
from pathlib import Path

def run_script(sub_folder, csv_sub_folder):
    path = Path(__file__).resolve().parent
    print("This is the second thing",path)
    subprocess.run([sys.executable, path / "current_defense_parser.py", sub_folder, csv_sub_folder])

if __name__ == "__main__":
    
    sub_folder = ["nba_html_2024-25"] 
    csv_sub_folder = ["defense_csv_2024-25",]
    
    for c_folder, csv_s_folder in zip(sub_folder, csv_sub_folder):
        run_script(c_folder, csv_s_folder)
    
    print("All scripts have finished executing.")

