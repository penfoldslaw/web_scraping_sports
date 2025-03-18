# from schedule_parser import schedule_parser  # Assuming this function exists

# def run_script(year, csv_sub_folder):
#     # Directly call the function instead of using subprocess
#     schedule_parser(year, csv_sub_folder)

# if __name__ == "__main__":
#     year = ["2025"]
#     csv_sub_folder = ["schedule_csv_2025"]

#     for c_folder, csv_s_folder in zip(year, csv_sub_folder):
#         run_script(c_folder, csv_s_folder)

#     print("All scripts have finished executing.")

import sys
import subprocess
from pathlib import Path
def run_script(year, csv_sub_folder):
    path = Path(__file__).resolve().parent
    subprocess.run([sys.executable,path / "schedule_parser.py", year, csv_sub_folder])

if __name__ == "__main__":
    
    year = ["2025"] 
    csv_sub_folder = ["schedule_csv_2025",]
    
    for c_folder, csv_s_folder in zip(year, csv_sub_folder):
        run_script(c_folder, csv_s_folder)
    
    print("All scripts have finished executing.")


