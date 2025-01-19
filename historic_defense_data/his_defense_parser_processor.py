import sys
import subprocess
def run_script(sub_folder, csv_sub_folder):
    subprocess.run([sys.executable, "his_defense_parser.py", sub_folder, csv_sub_folder])

if __name__ == "__main__":
    
    sub_folder = ["nba_html_2019-20", "nba_html_2020-21", "nba_html_2021-22", "nba_html_2022-23", "nba_html_2023-24"] 
    csv_sub_folder = ["defense_csv_2019-20", "defense_csv_2020-21", "defense_csv_2021-22", "defense_csv_2022-23", "defense_csv_2023-24"]
    
    for c_folder, csv_s_folder in zip(sub_folder, csv_sub_folder):
        run_script(c_folder, csv_s_folder)
    
    print("All scripts have finished executing.")