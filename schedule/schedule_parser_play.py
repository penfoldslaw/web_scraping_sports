import os
from bs4 import BeautifulSoup
import pandas
from datetime import datetime
import sys


year = "2024-25"

folder_path = f"D:/nba_schedules_play/nba_html_{year}"  #f"schedule/nba_schedules/nba_html_{year}"            #nba_html_2019-20 

log_file_path = "current_logs/schedule_parser.log"
sys.stdout = open(log_file_path, "w")
sys.stderr = open(log_file_path, "w")

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


        espn_date = soup.find('div', class_='Table__Title').get_text(strip=True)
        # Convert to a datetime object
        espn_date = datetime.strptime(espn_date, "%A, %B %d, %Y")


        print(espn_date)

        header = soup.find_all('tr', class_="Table__TR Table__even")
        threads = header[0].find_all('th')
        threads_text = [thread.get_text().strip() for thread in threads]
        del threads_text[-1]  # Remove the first element if it's not needed
        threads_text.insert(0, 'DATE')  # Insert the date at the beginning of the list
        print(threads_text)

        rows = soup.find("tbody", class_="Table__TBODY").find_all("tr")        

        extracted_data = []
        for row in rows:
            spans = row.find_all('span')
            row_text = [span.get_text().strip() for span in spans]
            extracted_data.append(row_text)
            extracted_data[-1].insert(0, espn_date)  # Insert the date at the beginning of each row
        
        print(extracted_data)



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







    import pandas as pd
    df = pd.DataFrame(extracted_data , columns=threads_text)
    # print(df)

    df['home_team'] = df['TV']
    df['schedule_team'] = df['MATCHUP']
    df['schedule_matchup'] = df['schedule_team'] + ' ' + df['home_team']
    #print(df) #shows how espn has it 
    # df['schedule_team'] = df['TV']
    # df = df.drop(['TIME', 'TV', 'OPPONENT'], axis=1)
    # df = df.rename(columns={'tickets': 'TIME'})

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
    df["home_team"] = df['home_team'].map(schedule_team_abbreviations)

    df = df[['home_team', 'schedule_team', 'schedule_matchup', 'DATE','TIME']]
    print(df)


    path = f'D:/nba_scheduled_play_csv/schedule_csv_{year}'
    csv_path = path
    os.makedirs(csv_path, exist_ok=True)
    df.to_csv(f"{csv_path}/{modified_filename}.csv", index=False)

    print(len(df))

