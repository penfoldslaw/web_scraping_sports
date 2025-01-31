from bs4 import BeautifulSoup
import os
import sys

def defense_parser(sub_folder, csv_sub_folder):
    log_file_path = "defense_parser.log"
    sys.stdout = open(log_file_path, "a")
    sys.stderr = open(log_file_path, "a")


    folder_path = f"D:/nba_defense_current/{sub_folder}"                #nba_html_2019-20 

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

            # Find the table header row
            header_row = soup.find('tr', class_='Crom_headers__mzI_m')

            # Extract the text from each <th> element
            if header_row:
                headers = [th.text.strip() for th in header_row.find_all('th')]
                del headers[21:]
                #print(headers)
            else:
                print("Header row not found.")

            rows = soup.find_all('tr')

            list = []
            tbody = soup.find('tbody', class_='Crom_body__UYOcU')

            # Extract the rows and their data
            rows = tbody.find_all('tr')
            for row in rows:
                cells = row.find_all('td')
                row_data = [cell.get_text(strip=True) for cell in cells]
                del row_data[21:]
                #print(row_data)
                list.append(row_data)
            #print(list)

            import pandas as pd
            df = pd.DataFrame(list, columns=headers)
            #print(df.columns)
            df.rename(columns={df.columns[0]: "RANK"}, inplace=True)

            rename_header = {
                'DEF\xa0RTG': 'DEF RTG',
                'OPP\xa0PTSOFF\xa0TOV': 'OPP PTSOFF TOV',
                'OPP\xa0PTS2ND\xa0CHANCE': 'OPP PTS2ND CHANCE',
                'OPP\xa0PTSFB': 'OPP PTSFB',
                'OPP\xa0PTSPAINT': 'OPP PTSPAINT'
            }

            df.rename(columns=rename_header, inplace=True)

            df['TEAM'] = df['TEAM'].astype('string')

            rename_team = {
                'Atlanta Hawks': 'ATL',
                'Boston Celtics': 'BOS',
                'Brooklyn Nets': 'BKN',
                'Charlotte Hornets': 'CHA',
                'Chicago Bulls': 'CHI',
                'Cleveland Cavaliers': 'CLE',
                'Dallas Mavericks': 'DAL',
                'Denver Nuggets': 'DEN',
                'Detroit Pistons': 'DET',
                'Golden State Warriors': 'GSW',
                'Houston Rockets': 'HOU',
                'Indiana Pacers': 'IND',
                'LA Clippers': 'LAC',
                'Los Angeles Lakers': 'LAL',
                'Memphis Grizzlies': 'MEM',
                'Miami Heat': 'MIA',
                'Milwaukee Bucks': 'MIL',
                'Minnesota Timberwolves': 'MIN',
                'New Orleans Pelicans': 'NOP',
                'New York Knicks': 'NYK',
                'Oklahoma City Thunder': 'OKC',
                'Orlando Magic': 'ORL',
                'Philadelphia 76ers': 'PHI',
                'Phoenix Suns': 'PHX',
                'Portland Trail Blazers': 'POR',
                'Sacramento Kings': 'SAC',
                'San Antonio Spurs': 'SAS',
                'Toronto Raptors': 'TOR',
                'Utah Jazz': 'UTA',
                'Washington Wizards': 'WAS'
                }
            
            df['TEAM'] = df['TEAM'].map(rename_team)

            columns_to_convert = [
               'OffRtg', 'DefRtg', 'NetRtg', 'AST%', 'AST/TO', 'ASTRatio', 'OREB%', 'DREB%', 'REB%', 'TOV%', 'eFG%', 'TS%', 'PACE', 'PIE', 'POSS']
            
             # Converting selected columns to float
            df[columns_to_convert] = df[columns_to_convert].apply(pd.to_numeric, errors='coerce')

            #save to csv
            path = f'D:/nba_dh_csv_current/{csv_sub_folder}'
            csv_path = path
            os.makedirs(csv_path, exist_ok=True)
            df.to_csv(f"{csv_path}/{modified_filename}.csv", index=False)

            
            # df.info()

            print(len(df))

            

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python defense_parser.py <sub_folder> <csv_sub_folder>")
        sys.exit(1)


    sub_folder = sys.argv[1]
    csv_sub_folder = sys.argv[2]
    defense_parser(sub_folder, csv_sub_folder)

    #defense_parser("nba_html_2019-20", "defense_csv_2019-20")


                              

            
        