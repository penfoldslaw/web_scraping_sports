import pandas as pd
from bs4 import BeautifulSoup
from IPython.display import display
from unidecode import unidecode
import os
import sys
import re

def box_parser(folder_path_html,folder_path_csv,date_of_match):
    directory = "box_score_log"
    os.makedirs(directory, exist_ok= True)
    log_file_path = "box_score_log/box_score_parser.log"
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

            cleaned_rows = []
            for row in rows:
                # First regex to capture the full name with apostrophes, hyphens, and special characters
                player_name_match = re.match(r"([\wÀ-ÿ]+(?:[\s'-][\wÀ-ÿ]+)*)", row[0])

                if player_name_match:
                    player_name = player_name_match.group(1).strip()  # Get the full name part
                    
                    # Check if the name ends with an unnecessary capital letter (e.g., "WareK")
                    if player_name[-1].isupper() and not re.search(r"['-]", player_name):
                        player_name = player_name[:-1]  # Remove the last character (capital letter)

                    row[0] = player_name  # Assign the cleaned name to the row

                cleaned_rows.append(row)  # Append the cleaned row

            # Now, cleaned_rows contains the correctly formatted names
            # print(cleaned_rows)


            # Convert to Pandas DataFrame
            df = pd.DataFrame(cleaned_rows, columns=columns)


            # Extract table headers
            all_theads = soup.find_all("thead", class_="StatsTableHead_thead__omZuF")
            all_tbodys = soup.find_all("tbody", class_="StatsTableBody_tbody__uvj_P")

            if len(all_theads) >= 2 and len(all_tbodys) >= 2:
                second_thead = all_theads[1]  # Get the second table header
                second_tbody = all_tbodys[1]  # Get the second table body

                # Extract column headers from the second thead
                headers = [th.text.strip() for th in second_thead.find_all("th")]
                
                # Extract rows from the second tbody
                rows = []
                for tr in second_tbody.find_all("tr"):
                    row_data = [td.text.strip() for td in tr.find_all("td")]
                    rows.append(row_data)

                cleaned_rows = []
                for row in rows:
                    # First regex to capture the full name with apostrophes, hyphens, and special characters
                    player_name_match = re.match(r"([\wÀ-ÿ]+(?:[\s'-][\wÀ-ÿ]+)*)", row[0])

                    if player_name_match:
                        player_name = player_name_match.group(1).strip()  # Get the full name part
                        
                        # Check if the name ends with an unnecessary capital letter (e.g., "WareK")
                        if player_name[-1].isupper() and not re.search(r"['-]", player_name):
                            player_name = player_name[:-1]  # Remove the last character (capital letter)

                        row[0] = player_name  # Assign the cleaned name to the row

                    cleaned_rows.append(row)  # Append the cleaned row

                # Now cleaned_rows should contain the correctly formatted names
                # print(cleaned_rows)


                # # Print results
                # print("Headers:", headers)
                # print("Rows:", rows)

            else:
                print("Second table not found.")
                        
            # Convert to Pandas DataFrame
            df_2 = pd.DataFrame(cleaned_rows, columns=columns)


            # Apply the function to the PLAYER column
            df['PLAYER'] = df['PLAYER'].apply(lambda x: re.sub(r'[A-Z]$', '', x)).apply(unidecode)

            df_2['PLAYER'] = df_2['PLAYER'].apply(lambda x: re.sub(r'[A-Z]$', '', x)).apply(unidecode)


            pd.set_option('display.max_rows', 1000)  # Maximum number of rows to display
            pd.set_option('display.max_columns', None)  # Show all columns
            pd.set_option('display.width', 1000)  # Adjust column width for better readability

            result = pd.concat([df, df_2], ignore_index=True)




            # Display DataFrame
            # display(result)
            date = date_of_match
            # display(df)
            os.makedirs(folder_path_csv,exist_ok=True)
            result.to_csv(f'{folder_path_csv}/{modified_filename}_{date}.csv', index=False)

if __name__ == "__main__":


    if len(sys.argv) != 4:
        print("Usage: python box_parser.py <folder_path_html> <folder_path_csv> <date_of_match>")
        sys.exit(1)

    folder_path_html = sys.argv[1]
    folder_path_csv = sys.argv[2]
    date_of_match = sys.argv[3]
    
    box_parser(folder_path_html, folder_path_csv, date_of_match)


