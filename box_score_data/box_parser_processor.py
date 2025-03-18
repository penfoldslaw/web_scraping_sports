import sys
import subprocess
from pathlib import Path

def run_script(folder_path_html, folder_path_csv, date_of_match):
    path = Path(__file__).resolve().parent
    print("This is the second thing",path)
    subprocess.run([sys.executable, path / "box_parser.py", folder_path_html, folder_path_csv, date_of_match])

if __name__ == "__main__":
    
    folder_path_html = "box_score_data/box_score/nba_html_3-14-25"
    folder_path_csv = "box_score_data/box_score_csv"
    date_of_match = "3-14-25"
    
    # for c_folder, csv_s_folder in zip(folder_path_html, folder_path_csv):
    #     run_script(c_folder, csv_s_folder, date_of_match)

    run_script(folder_path_html,folder_path_csv,date_of_match)
    
    print("All scripts have finished executing.")



# if __name__ == "__main__":


#     if len(sys.argv) != 4:
#         print("Usage: python box_parser.py <folder_path_html> <folder_path_csv> <date_of_match>")
#         sys.exit(1)

#     folder_path_html = sys.argv[1]
#     folder_path_csv = sys.argv[2]
#     date_of_match = sys.argv[3]
    
#     box_parser(folder_path_html, folder_path_csv, date_of_match)
#     # sys.stdout.close()
#     # sys.stderr.close()

