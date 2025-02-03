# from pathlib import Path
# from current_usage_parser import create_dataframe  # Assuming this function exists

# def run_script(sub_folder, csv_sub_folder):
#     # Directly call the function instead of using subprocess
#     create_dataframe(sub_folder, csv_sub_folder)

# if __name__ == "__main__":
#     sub_folder = ["nba_html_2024-25"]
#     csv_sub_folder = ["usage_csv_2024-25"]

#     for c_folder, csv_s_folder in zip(sub_folder, csv_sub_folder):
#         run_script(c_folder, csv_s_folder)

#     print("All scripts have finished executing.")


import sys
import subprocess
from pathlib import Path
def run_script(sub_folder, csv_sub_folder):
    path = Path(__file__).resolve().parent
    subprocess.run([sys.executable,path / "current_usage_parser.py", sub_folder, csv_sub_folder])

if __name__ == "__main__":
    
    sub_folder = ["nba_html_2024-25"] 
    csv_sub_folder=["usage_csv_2024-25"]
    
    for c_folder, csv_s_folder in zip(sub_folder, csv_sub_folder):
        run_script(c_folder, csv_s_folder)
    
    print("All scripts have finished executing.")