from bs4 import BeautifulSoup
import os


def defense_parser(sub_folder, csv_sub_folder):
    folder_path = f"nba_defense_historic/{sub_folder}"                #nba_html_2019-20 

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
                del headers[15:]
                # print(headers)
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
                del row_data[15:]
                # print(row_data)
                list.append(row_data)
            # print(list)

            import pandas as pd
            df = pd.DataFrame(list, columns=headers)

            df.rename(columns={df.columns[0]: "RANK"}, inplace=True)

            rename_map = {
                'DEF\xa0RTG': 'DEF RTG',
                'OPP\xa0PTSOFF\xa0TOV': 'OPP PTSOFF TOV',
                'OPP\xa0PTS2ND\xa0CHANCE': 'OPP PTS2ND CHANCE',
                'OPP\xa0PTSFB': 'OPP PTSFB',
                'OPP\xa0PTSPAINT': 'OPP PTSPAINT'
            }

            df.rename(columns=rename_map, inplace=True)

            df['TEAM'] = df['TEAM'].astype('string')

            columns_to_convert = [
                'RANK', 'GP', 'W', 'L', 'MIN','DEF RTG', 'DREB',
                'DREB%', 'STL', 'BLK', 'OPP PTSOFF TOV', 'OPP PTS2ND CHANCE', 'OPP PTSFB', 'OPP PTSPAINT']
            
             # Converting selected columns to float
            df[columns_to_convert] = df[columns_to_convert].apply(pd.to_numeric, errors='coerce')

            #save to csv
            path = f'nba_dh_csv/{csv_sub_folder}'
            csv_path = path
            os.makedirs(csv_path, exist_ok=True)
            df.to_csv(f"{csv_path}/{modified_filename}.csv", index=False)

            
            # df.info()

            print(len(df))

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python defense_parser.py <sub_folder> <csv_sub_folder>")
        sys.exit(1)


    sub_folder = sys.argv[1]
    csv_sub_folder = sys.argv[2]
    defense_parser(sub_folder, csv_sub_folder)

    #defense_parser("nba_html_2019-20", "defense_csv_2019-20")


                              

            
        