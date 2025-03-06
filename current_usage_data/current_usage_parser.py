from bs4 import BeautifulSoup
import os
from IPython.display import display
import sys
from unidecode import unidecode

def create_dataframe(relative_path, csv_sub_folder):
    log_file_path = "current_logs/current_usage_parser.log"
    sys.stdout = open(log_file_path, "a")
    sys.stderr = open(log_file_path, "a")

    folder_path = f"D:/nba_usage_current/{relative_path}"  #f"schedule/nba_schedules/nba_html_{year}"            #nba_html_2019-20 

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

            # Find the table header row
            header_row = soup.find('tr', class_='Crom_headers__mzI_m')

            # Extract the text from each <th> element
            if header_row:
                headers = [th.text.strip() for th in header_row.find_all('th')]
                del headers[26:]
                #print(headers)
                #print(len(headers))
            else:
                print(f"Header {modified_filename} row not found.")

            # rows = soup.find_all('tr')


            rows = soup.find_all('tbody', class_="Crom_body__UYOcU")

            extracted_data = []
            for row in rows:
                spans = row.find_all('td')
                row_text = [span.get_text().strip() for span in spans]
                for i in range (0, len(row_text), 26):
                    sublist = row_text[i:i+26]
                    extracted_data.append(sublist)

            #print(extracted_data)



            import pandas as pd
            df = pd.DataFrame(extracted_data, columns=headers)
            pd.set_option('display.max_rows', 1000)  # Maximum number of rows to display
            pd.set_option('display.max_columns', None)  # Show all columns
            pd.set_option('display.width', 1000)  # Adjust column width for better readability

            df = df.rename(columns={'': 'RANK'})
            int_columns = ['RANK','AGE','GP','W','L']
            float_columns = [
                'MIN',  'USG%', '%FGM', '%FGA', '%3PM', 
                '%3PA', '%FTM', '%FTA', '%OREB', '%DREB', '%REB', 
                '%AST', '%TOV', '%STL', '%BLK', '%BLKA', '%PF', '%PFD', '%PTS']

            df[int_columns] = df[int_columns].astype(int)
            df[float_columns] = df[float_columns].astype(float)
            df['Player'] = df['Player'].apply(unidecode)


            #df.info()


            #save to csv
            path = f'D:/nba_usage_csv_current/{csv_sub_folder}'
            csv_path = path
            os.makedirs(csv_path, exist_ok=True)
            df.to_csv(f"{csv_path}/{modified_filename}.csv", index=False)

            print(len(df))


if __name__ == "__main__":
    # import sys
    # log_file_path = "current_usage_parser.log"
    # sys.stdout = open(log_file_path, "a")
    # sys.stderr = open(log_file_path, "a")

    if len(sys.argv) != 3:
        print("Usage: python his_usage_parser.py <sub_folder> <csv_sub_folder>")
        sys.exit(1)


    sub_folder = sys.argv[1]
    csv_sub_folder = sys.argv[2]
    create_dataframe(sub_folder, csv_sub_folder)

