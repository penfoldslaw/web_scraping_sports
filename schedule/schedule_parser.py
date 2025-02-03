from bs4 import BeautifulSoup
import os
from IPython.display import display
import sys

def schedule_parser(year, csv_sub_folder):
    log_file_path = "current_logs/schedule_parser.log"
    sys.stdout = open(log_file_path, "w")
    sys.stderr = open(log_file_path, "w")

    folder_path = f"D:/nba_schedules/nba_html_{year}"  #f"schedule/nba_schedules/nba_html_{year}"            #nba_html_2019-20 

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        #print(file_path)

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

            rows = soup.find_all('tr', class_="Table__TR Table__TR--sm Table__even")

            extracted_data = []
            for row in rows:
                spans = row.find_all('span')
                row_text = [span.get_text().strip() for span in spans]
                extracted_data.append(row_text)

            #print(extracted_data)

            search_string = 'TIME'

            # If you only want the first match:
            first_match = next((sublist for sublist in extracted_data if search_string in sublist), None)


            team_abbreviations = {
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

            #print("First match:", first_match)
            team_name = " ".join([span.get_text(strip=True) for span in soup.find_all('span', class_='db')])

            if team_name in team_abbreviations:
                team_name = team_abbreviations[team_name]


            # Get every list after the first match
            if first_match is not None:
                # Find the index of the first match
                match_index = extracted_data.index(first_match)
                # Slice to get lists after the match
                lists_after = extracted_data[match_index + 1:]
            else:
                lists_after = []  # No match found

            # print("Lists after the first match:", lists_after)
            #print(first_match)

            #print(lists_after)


            import pandas as pd
            df = pd.DataFrame(lists_after, columns=first_match)

            df['schedule_matchup'] = df['OPPONENT'] + ' ' + df['TV']
            df['schedule_team'] = df['TV']
            df = df.drop(['TIME', 'TV', 'OPPONENT'], axis=1)
            df = df.rename(columns={'tickets': 'TIME'})
            df["home_team"] = team_name

            schedule_team_abbreviations = {
                'Atlanta': 'ATL',
                'Boston': 'BOS',
                'Brooklyn': 'BKN',
                'Charlotte': 'CHA',
                'Chicago': 'CHI',
                'Cleveland': 'CLE',
                'Dallas': 'DAL',
                'Denver': 'DEN',
                'Detroit': 'DET',
                'Golden State': 'GSW',
                'Houston': 'HOU',
                'Indiana': 'IND',
                'LA': 'LAC',
                'Los Angeles': 'LAL',
                'Memphis': 'MEM',
                'Miami': 'MIA',
                'Milwaukee': 'MIL',
                'Minnesota': 'MIN',
                'New Orleans': 'NOP',
                'New York': 'NYK',
                'Oklahoma City': 'OKC',
                'Orlando': 'ORL',
                'Philadelphia': 'PHI',
                'Phoenix': 'PHX',
                'Portland': 'POR',
                'Sacramento': 'SAC',
                'San Antonio': 'SAS',
                'Toronto': 'TOR',
                'Utah': 'UTA',
                'Washington': 'WAS'
            }
            #This is renaming the teams to their abbreviations
            df['schedule_team'] = df['schedule_team'].map(schedule_team_abbreviations)

            df = df[['home_team', 'schedule_team', 'schedule_matchup', 'DATE','TIME']]

            from datetime import datetime
            current_year = datetime.now().year
            df['DATE'] = df['DATE'] + ' ' + str(current_year)

            df['DATE'] = pd.to_datetime(df['DATE'])

            df['location'] = df['schedule_matchup'].apply(lambda x: 'away' if '@' in x else 'home')

            #display(df.head(2))

            #save to csv
            path = f'D:/nba_scheduled_csv/{csv_sub_folder}'
            csv_path = path
            os.makedirs(csv_path, exist_ok=True)
            df.to_csv(f"{csv_path}/{modified_filename}.csv", index=False)

            print(len(df))


if __name__ == "__main__":
    # import sys
    # log_file_path = "schedule_parser.log"
    # sys.stdout = open(log_file_path, "w")
    # sys.stderr = open(log_file_path, "w")

    if len(sys.argv) != 3:
        print("Usage: python defense_parser.py <year> <csv_sub_folder>")
        sys.exit(1)


    sub_folder = sys.argv[1]
    csv_sub_folder = sys.argv[2]
    schedule_parser(sub_folder, csv_sub_folder)