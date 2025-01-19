from bs4 import BeautifulSoup
import os

def create_dataframe(relative_path, csv_path):

    # Specify the directory containing the files
    folder_path = relative_path      #r'nba_historic\nba_html_2019'

    # Loop through each file in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Check if it's a file (and not a subfolder)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                # Read the content of the file
                html_content = file.read()
                #removing the .html from the file name so I can .csv when it comes time to save
                original_filename = filename
                remove_string_in_filename = ".html"
                modified_filename = original_filename.replace(remove_string_in_filename,"") 
                print(f"Contents of {modified_filename}")

            # Parse the HTML content
            soup = BeautifulSoup(html_content, 'html.parser')

            # Find the table header row
            header_row = soup.find('tr', class_='Crom_headers__mzI_m')

            # Extract the text from each <th> element
            if header_row:
                headers = [th.text.strip() for th in header_row.find_all('th')]
                #print(headers)
            else:
                print(f"Header {modified_filename} {relative_path} row not found.")

            rows = soup.find_all('tr')

            # Loop through rows and extract data
            list = []
            
            #check to see if the html holds any data if not it is skipped
            if soup.find('tbody', class_='Crom_body__UYOcU') is None:
                print(f"Contents of {modified_filename} {relative_path} is empty, skipping this file.")
                continue

            tbody = soup.find('tbody', class_='Crom_body__UYOcU')

            # Extract the rows and their data
            rows = tbody.find_all('tr')
            
            for row in rows:
                cells = row.find_all('td')
                row_data = [cell.get_text(strip=True) for cell in cells]
                #print(row_data)
                list.append(row_data)
            #print(list)

            import pandas as pd 
            df = pd.DataFrame(list, columns=headers)
            #print(df.head(1))


            df[['Date', 'Matchup']] = df['Match Up'].str.split(' - ', expand=True)

            #splitting the match to get the team names
            df[['Team', 'Away']] = df['Matchup'].str.split(r' vs\. | @ ', expand=True)
            df[['Away_game', 'Home/Away_game']] = df['Matchup'].str.split(' @ ', expand=True)

            # Turns every none n/a value in this column into Away
            df[['Home/Away_game']] = df[['Home/Away_game']].map(lambda x: 'Away' if pd.notna(x) else x)
            # Turns every n/a value in this column into Home
            df[['Home/Away_game']] = df[['Home/Away_game']].fillna('Home')

            df['Date'] = pd.to_datetime(df['Date'], format='%b %d, %Y')
            df['Matchup'] = df['Matchup'].astype('string')
            df['Team'] = df['Team'].astype('string')
            df['Away'] = df['Away'].astype('string')
            df['Home/Away_game'] = df['Home/Away_game'].astype('string')
            df['W/L'] = df['W/L'].astype('string')
            #convert mins to float
            df['MIN'] = df['MIN'].str.replace(':', '.').astype(float)
            

            columns_to_convert = [
                'PTS', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', 
                'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', '+/-'
            ]

            # Converting selected columns to float
            df[columns_to_convert] = df[columns_to_convert].apply(pd.to_numeric, errors='coerce')


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

            df_total_counts = df.isna().sum() + df.count()
            print(len(df))
            csv_path = csv_path
            os.makedirs(csv_path, exist_ok=True)
            df.to_csv(f'{csv_path}\{modified_filename}.csv', index=False)

if __name__ == "__main__":
    import sys
    log_file_path = "his_player_parser.log"
    sys.stdout = open(log_file_path, "a")
    sys.stderr = open(log_file_path, "a")

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
    sys.stdout.close()
    sys.stderr.close()