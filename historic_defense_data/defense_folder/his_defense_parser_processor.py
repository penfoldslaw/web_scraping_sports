import sys
import subprocess
from pathlib import Path
def run_script(sub_folder, csv_sub_folder):
    path = Path(__file__).resolve().parent
    subprocess.run([sys.executable,path / "his_defense_parser.py", sub_folder, csv_sub_folder])

if __name__ == "__main__":
    
    sub_folder = ["nba_html_2022-23", "nba_html_2023-24"] 
    csv_sub_folder = ["defense_csv_2022-23", "defense_csv_2023-24"]
    
    for c_folder, csv_s_folder in zip(sub_folder, csv_sub_folder):
        run_script(c_folder, csv_s_folder)
    
    print("All scripts have finished executing.")



# import sys
# from pathlib import Path
# from his_defense_parser import defense_parser # Assuming this is the function inside the script

# def run_script(sub_folder, csv_sub_folder):
#     # Define the path of the subfolder or any other required parameters.
#     #path = Path().resolve()
#     defense_parser(sub_folder, csv_sub_folder)  # Call the function directly

# if __name__ == "__main__":
#     sub_folder = ["nba_html_2022-23", "nba_html_2023-24"] 
#     csv_sub_folder = ["defense_csv_2022-23", "defense_csv_2023-24"]

#     for c_folder, csv_s_folder in zip(sub_folder, csv_sub_folder):
#         run_script(c_folder, csv_s_folder)
    
#     print("All scripts have finished executing.")