import sys
import subprocess
def run_script(year, csv_sub_folder):
    subprocess.run([sys.executable, "schedule_parser.py", year, csv_sub_folder])

if __name__ == "__main__":
    
    year = ["2025"] 
    csv_sub_folder = ["schedule_csv_2025",]
    
    for c_folder, csv_s_folder in zip(year, csv_sub_folder):
        run_script(c_folder, csv_s_folder)
    
    print("All scripts have finished executing.")

