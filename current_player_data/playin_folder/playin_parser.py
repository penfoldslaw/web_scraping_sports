from bs4 import BeautifulSoup
import pandas as pd
import os
import sys

def create_dataframe(relative_path, csv_path):

    log_file_path = "current_logs/current_parser.log"
    sys.stdout = open(log_file_path, "a")
    sys.stderr = open(log_file_path, "a")
    # Specify the directory containing the files
    folder_path = relative_path  # r'nba_historic\nba_html_2019'

    # Loop through each file in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Check if it's a file (and not a subfolder)
        if os.path.isfile(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    # Read the content of the file
                    html_content = file.read()
                    # Removing the .html from the file name to save as .csv
                    original_filename = filename
                    remove_string_in_filename = ".html"
                    modified_filename = original_filename.replace(remove_string_in_filename, "") 
                    print(f"Processing {modified_filename}")

                # Parse the HTML content
                soup = BeautifulSoup(html_content, 'html.parser')

                # Find the table header row
                header_row = soup.find('tr', class_='Crom_headers__mzI_m')

                # Extract the text from each <th> element
                if header_row:
                    headers = [th.text.strip() for th in header_row.find_all('th')]
                else:
                    print(f"Header row not found in {modified_filename}. Skipping this file.")
                    continue  # Skip this file

                # Check if the HTML content contains data
                if soup.find('tbody', class_='Crom_body__UYOcU') is None:
                    print(f"Contents of {modified_filename} is empty. Skipping this file.")
                    continue

                # Extract rows and data
                tbody = soup.find('tbody', class_='Crom_body__UYOcU')
                rows = tbody.find_all('tr')
                
                # Initialize list to hold row data
                data_list = []
                
                for row in rows:
                    cells = row.find_all('td')
                    row_data = [cell.get_text(strip=True) for cell in cells]
                    data_list.append(row_data)

                # Convert list into a pandas DataFrame
                df = pd.DataFrame(data_list, columns=headers)

                # Split the 'Match Up' column into 'Date' and 'Matchup'
                df[['Date', 'Matchup']] = df['Match Up'].str.split(' - ', expand=True)

                # Attempt to split and extract team names and home/away game status
                try:
                    df[['Team', 'Away']] = df['Matchup'].str.split(r' vs\. | @ ', expand=True)
                    df[['Away_game', 'Home/Away_game']] = df['Matchup'].str.split(' @ ', expand=True)

                    # Assign 'Away' or 'Home' based on NaN values
                    df[['Home/Away_game']] = df[['Home/Away_game']].map(lambda x: 'Away' if pd.notna(x) else x)
                    df[['Home/Away_game']] = df[['Home/Away_game']].fillna('Home')

                except ValueError as e:
                    print(f"Error occurred while processing 'Matchup' column in {modified_filename}: {e}")
                    continue  # Skip this file if error occurs

                # Convert data types for columns
                df['Date'] = pd.to_datetime(df['Date'], format='%b %d, %Y')
                df['Matchup'] = df['Matchup'].astype('string')
                df['Team'] = df['Team'].astype('string')
                df['Away'] = df['Away'].astype('string')
                df['Home/Away_game'] = df['Home/Away_game'].astype('string')
                df['W/L'] = df['W/L'].astype('string')

                # Convert minutes to float
                df['MIN'] = df['MIN'].str.replace(':', '.').astype(float)

                columns_to_convert = [
                    'PTS', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', 
                    'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', '+/-'
                ]

                # Convert selected columns to numeric
                df[columns_to_convert] = df[columns_to_convert].apply(pd.to_numeric, errors='coerce')

                # Reorder columns for final output
                df = df[['Date', 
                        'Matchup', 
                        'Team',
                        'Away',
                        'Home/Away_game',
                        'W/L', 
                        'MIN', 
                        'PTS', 
                        'FGM', 
                        'FGA',
                        'FG%', 
                        '3PM', 
                        '3PA', 
                        '3P%', 
                        'FTM', 
                        'FTA', 
                        'FT%', 
                        'OREB', 
                        'DREB', 
                        'REB', 
                        'AST', 
                        'STL', 
                        'BLK', 
                        'TOV', 
                        'PF', 
                        '+/-']]

                # Save the dataframe to CSV
                os.makedirs(csv_path, exist_ok=True)
                df.to_csv(f'{csv_path}/{modified_filename}.csv', index=False)
                print(f"Successfully processed and saved {modified_filename}.csv")

            except Exception as e:
                print(f"An error occurred while processing the file {filename}: {e}")
                continue  # Skip this file if any error occurs

    import csv
    from pathlib import Path

    folder1 = Path(r"D:\nba_player_csv_current\season_2024-25\all_quarters")
    folder2 = Path(r"D:\nba_player_csv_current\season_2024-25_playin\all_quarters") 



    csv_files = [f for f in folder2.iterdir() if f.suffix.lower() == '.csv']
    print(f"Found {len(csv_files)} CSV files in folder2.")

    for file2 in csv_files:
        file_name = file2.name
        file1 = folder1 / file_name

        print(f"\nProcessing: {file_name}")

        if not file1.exists():
            print(f"Skipping {file_name} (no matching file in folder1)")
            continue

        # Load all existing rows from file1 into a set (as tuples)
        with open(file1, 'r', newline='', encoding='utf-8') as f1:
            reader1 = csv.reader(f1)
            next(reader1, None)  # skip header
            existing_rows = set(tuple(row) for row in reader1)

        # Load new rows from file2 (skip header)
        with open(file2, 'r', newline='', encoding='utf-8') as f2:
            reader2 = csv.reader(f2)
            next(reader2, None)
            new_rows = [row for row in reader2 if tuple(row) not in existing_rows]

        if not new_rows:
            print(f"No new rows to append in {file_name}")
            continue

        # Check if file1 ends with newline
        with open(file1, 'rb') as f1_check:
            try:
                f1_check.seek(-2, 2)
                ends_with_newline = f1_check.read().endswith(b'\n')
            except OSError:
                ends_with_newline = False  # file is too small

        with open(file1, 'a', newline='', encoding='utf-8') as f1:
            if not ends_with_newline:
                f1.write('\n')
            writer = csv.writer(f1)
            writer.writerows(new_rows)

        print(f"Appended {len(new_rows)} new rows to {file_name}")


if __name__ == "__main__":
    # import sys
    # log_file_path = "current_parser.log"
    # sys.stdout = open(log_file_path, "a")
    # sys.stderr = open(log_file_path, "a")

    # create_dataframe(r'nba_historic\nba_html_2019', r'nba_historic_csv\all_quarters')
    # create_dataframe(r'nba_historic\nba_html_2019\quarter_data\q1', r'nba_historic_csv\quarter_data\q1' )
    # create_dataframe(r'nba_historic\nba_html_2019\quarter_data\q2', r'nba_historic_csv\quarter_data\q2')
    # create_dataframe(r'nba_historic\nba_html_2019\quarter_data\q3', r'nba_historic_csv\quarter_data\q3')
    # create_dataframe(r'nba_historic\nba_html_2019\quarter_data\q4', r'nba_historic_csv\quarter_data\q4')

    if len(sys.argv) != 3:
        print("Usage: python defense_parser.py <relative_path> <csv_path>")
        sys.exit(1)

    relative_path = sys.argv[1]
    csv_path = sys.argv[2]
    
    create_dataframe(relative_path, csv_path)
    # sys.stdout.close()
    # sys.stderr.close()