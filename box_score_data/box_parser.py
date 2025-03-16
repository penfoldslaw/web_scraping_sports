import pandas as pd
from bs4 import BeautifulSoup
from IPython.display import display
import os
import sys
import re

def box_parser(folder_path_html,folder_path_csv,date_of_match):
    directory = "box_score_data/box_score_log"
    os.makedirs(directory, exist_ok= True)
    log_file_path = "box_score_data/box_score_log/box_score_parser.log"
    sys.stdout = open(log_file_path, "a")
    sys.stderr = open(log_file_path, "a")

    folder_path = folder_path_html    #r"box_score/nba_html_3-14-25"

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Check if it's a file (and not a subfolder)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                # Read the content of the file
                html_content = file.read()
                # removing the .html from the file name so I can .csv when it comes time to save
                original_filename = filename
                remove_string_in_filename = ".html"
                modified_filename = original_filename.replace(remove_string_in_filename, "")
                print(f"Contents of {modified_filename}")

            # Parse the HTML content
            soup = BeautifulSoup(html_content, 'html.parser')

            # Extract table headers
            thead = soup.find("thead", class_="StatsTableHead_thead__omZuF")
            columns = [th.text.strip() for th in thead.find_all("th")]

            # Extract table data
            tbody = soup.find("tbody")  # Locate table body
            rows = []
            for tr in tbody.find_all("tr"):  # Loop through each row
                cells = [td.text.strip() for td in tr.find_all("td")]
                if cells:  # Ensure the row is not empty
                    rows.append(cells)

            # Convert to Pandas DataFrame
            df = pd.DataFrame(rows, columns=columns)

            # Function to clean player names
            def clean_player_name(player):
                # Use regex to remove duplicate short names and position letters
                cleaned_name = re.sub(r'([A-Za-z\s]+)[A-Z]\.\s\w+\s?[FGC]?$', r'\1', player).strip()
                return cleaned_name.strip()

            # Apply the function to the PLAYER column
            df["PLAYER"] = df["PLAYER"].apply(clean_player_name)



            pd.set_option('display.max_rows', 1000)  # Maximum number of rows to display
            pd.set_option('display.max_columns', None)  # Show all columns
            pd.set_option('display.width', 1000)  # Adjust column width for better readability

            # Display DataFrame
            # display(df)
            date = date_of_match
            # display(df)
            os.makedirs(folder_path_csv,exist_ok=True)
            df.to_csv(f'{folder_path_csv}/{modified_filename}_{date}.csv', index=False)

if __name__ == "__main__":


    if len(sys.argv) != 4:
        print("Usage: python box_parser.py <folder_path_html> <folder_path_csv> <date_of_match>")
        sys.exit(1)

    folder_path_html = sys.argv[1]
    folder_path_csv = sys.argv[2]
    date_of_match = sys.argv[3]
    
    box_parser(folder_path_html, folder_path_csv, date_of_match)
    # sys.stdout.close()
    # sys.stderr.close()


