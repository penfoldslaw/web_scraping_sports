from bs4 import BeautifulSoup
import os
from IPython.display import display
from unidecode import unidecode
import datetime



def tracking_parser(html_folder_path,csv_folder_path):



    folder_path =   html_folder_path    #r"..\tracking_data\nba_html_2024-25"  

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        #print(file_path)


        os.makedirs("current_logs", exist_ok=True)
        log_file_path = "current_logs/current_track_parser.log"
        sys.stdout = open(log_file_path, "w")
        sys.stderr = open(log_file_path, "w")

        def log_with_timestamp(message):
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"{timestamp} - {message}")
            print(f"{timestamp} - {message}", file=sys.stderr)

        log_with_timestamp(f"Scraping {filename} data...") 

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





            if filename == "catch_shoot_content.html":
                if header_row:
                    headers = [th.text.strip() for th in header_row.find_all('th')]
                    del headers[26:]
                    print(headers)
                    print(repr(headers))
                    print(len(headers))
                    column_number = len(headers)
                else:
                    print(f"Header {modified_filename} row not found.")

                # rows = soup.find_all('tr')


                rows = soup.find_all('tbody', class_="Crom_body__UYOcU")




                extracted_data = []
                for row in rows:
                    spans = row.find_all('td')
                    row_text = [span.get_text().strip() for span in spans]
                    for i in range (0, len(row_text), column_number):
                        sublist = row_text[i:i+column_number]
                        extracted_data.append(sublist)

                # print(extracted_data)



                import pandas as pd
                df = pd.DataFrame(extracted_data, columns=headers)
                pd.set_option('display.max_rows', 1000)  # Maximum number of rows to display
                pd.set_option('display.max_columns', None)  # Show all columns
                pd.set_option('display.width', 1000)  # Adjust column width for better readability


                # df = df.rename(columns={'\\teFG%': 'eFG%'})
                int_columns = ['GP']
                float_columns = [
                    'MIN',  'PTS', 'FGM', 'FGA', 
                    'FG%', '3PM', 'eFG%', '3PA', '3P%']

                df[int_columns] = df[int_columns].astype(int)
                df[float_columns] = df[float_columns].replace('-', 0).astype(float)
                df['PLAYER'] = df['PLAYER'].apply(unidecode)

                df.columns = [col + '_catch_shoot' for col in df.columns]




                
                #save to csv
                file_path_csv = csv_folder_path
                path = file_path_csv
                csv_path = path
                os.makedirs(csv_path, exist_ok=True)
                df.to_csv(f"{csv_path}/{modified_filename}.csv", index=False)

                display(df)


            if filename == "passing_content.html":
                # Extract the text from each <th> element
                if header_row:
                    headers = [th.text.strip() for th in header_row.find_all('th')]
                    del headers[15:]
                    print(headers)
                    print(repr(headers))
                    print(len(headers))
                    column_number = len(headers)
                    headers[12] = 'ASTAdj'
                    headers[13] = 'Assist_to_Pass'
                    headers[14] = 'Assist_to_Pass_Percentage_Adj'
                    # headers[15] = 'Assist_to_Pass_Percentage_Adj'


                else:
                    print(f"Header {modified_filename} row not found.")

                # rows = soup.find_all('tr')


                rows = soup.find_all('tbody', class_="Crom_body__UYOcU")


                extracted_data = []
                for row in rows:
                    spans = row.find_all('td')
                    row_text = [span.get_text().strip() for span in spans]
                    for i in range (0, len(row_text), column_number):
                        sublist = row_text[i:i+column_number]
                        extracted_data.append(sublist)

                # print(extracted_data)



                import pandas as pd
                df = pd.DataFrame(extracted_data, columns=headers)
                pd.set_option('display.max_rows', 1000)  # Maximum number of rows to display
                pd.set_option('display.max_columns', None)  # Show all columns
                pd.set_option('display.width', 1000)  # Adjust column width for better readability


                # df = df.rename(columns={'': 'RANK'})
                df = df.rename(columns={'AST\xa0PTSCreated': 'ASTPTSCreated'})
                int_columns = ['GP','W','L']
                float_columns = [
                    'MIN',  'PassesMade', 'PassesReceived', 'AST', 'SecondaryAST', 
                    'PotentialAST', 'ASTPTSCreated', 'ASTAdj', 'Assist_to_Pass', 'Assist_to_Pass_Percentage_Adj']

                df[int_columns] = df[int_columns].astype(int)
                df[float_columns] = df[float_columns].astype(float)
                df['PLAYER'] = df['PLAYER'].apply(unidecode)

                df.columns = [col + '_passing' for col in df.columns]



                
                #save to csv
                file_path_csv = csv_folder_path   #f"nba_tracking/tracking_csv_2024-25"
                # path = file_path_csv
                csv_path = file_path_csv
                os.makedirs(csv_path, exist_ok=True)
                df.to_csv(f"{csv_path}/{modified_filename}.csv", index=False)

                display(df)


            if filename == "drives_content.html":
                if header_row:
                    headers = [th.text.strip() for th in header_row.find_all('th')]
                    del headers[26:]
                    print(headers)
                    print(len(headers))
                    column_number = len(headers)
                else:
                    print(f"Header {modified_filename} row not found.")

                # rows = soup.find_all('tr')


                rows = soup.find_all('tbody', class_="Crom_body__UYOcU")




                extracted_data = []
                for row in rows:
                    spans = row.find_all('td')
                    row_text = [span.get_text().strip() for span in spans]
                    for i in range (0, len(row_text), column_number):
                        sublist = row_text[i:i+column_number]
                        extracted_data.append(sublist)

                # print(extracted_data)



                import pandas as pd
                df = pd.DataFrame(extracted_data, columns=headers)
                pd.set_option('display.max_rows', 1000)  # Maximum number of rows to display
                pd.set_option('display.max_columns', None)  # Show all columns
                pd.set_option('display.width', 1000)  # Adjust column width for better readability


                df = df.rename(columns={'AST\xa0PTSCreated': 'ASTPTSCreated'})
                int_columns = ['GP', 'W', 'L']
                float_columns = [
                    'MIN', 'DRIVES', 'FGM', 'FGA', 'FG%', 'FTM', 'FTA', 'FT%', 'PTS', 'PTS%', 'PASS', 'PASS%', 'AST', 'AST%', 'TO', 'TOV%', 'PF', 'PF%']

                df[int_columns] = df[int_columns].replace('-', 0).astype(int)
                df[float_columns] = df[float_columns].replace('-', 0).astype(float)
                df['PLAYER'] = df['PLAYER'].apply(unidecode)

                df.columns = [col + '_drive' for col in df.columns]



                
                #save to csv
                file_path_csv = csv_folder_path #f"nba_tracking/tracking_csv_2024-25"
                path = file_path_csv
                csv_path = path
                os.makedirs(csv_path, exist_ok=True)
                df.to_csv(f"{csv_path}/{modified_filename}.csv", index=False)

                display(df)



            if filename == "elbow_touch_content.html":
                # Extract the text from each <th> element
                if header_row:
                    headers = [th.text.strip() for th in header_row.find_all('th')]
                    del headers[26:]
                    print(headers)
                    print(len(headers))
                    column_number = len(headers)
                else:
                    print(f"Header {modified_filename} row not found.")

                # rows = soup.find_all('tr')


                rows = soup.find_all('tbody', class_="Crom_body__UYOcU")




                extracted_data = []
                for row in rows:
                    spans = row.find_all('td')
                    row_text = [span.get_text().strip() for span in spans]
                    for i in range (0, len(row_text), column_number):
                        sublist = row_text[i:i+column_number]
                        extracted_data.append(sublist)

                # print(extracted_data)



                import pandas as pd
                df = pd.DataFrame(extracted_data, columns=headers)
                pd.set_option('display.max_rows', 1000)  # Maximum number of rows to display
                pd.set_option('display.max_columns', None)  # Show all columns
                pd.set_option('display.width', 1000)  # Adjust column width for better readability

                # df = df.rename(columns={'AST\xa0PTSCreated': 'ASTPTSCreated'})
                int_columns = ['GP', 'W', 'L']
                float_columns = [
                    'MIN', 'Touches', 'ElbowTouches', 'FGM', 'FGA', 'FG%', 'FTM', 'FTA', 'FT%', 'PTS', 'PTS%', 'PASS', 'PASS%', 'AST', 'AST%', 'TO', 'TOV%', 'PF', 'PF%']

                df[int_columns] = df[int_columns].replace('-', 0).astype(int)
                df[float_columns] = df[float_columns].replace('-', 0).astype(float)
                df['PLAYER'] = df['PLAYER'].apply(unidecode)

                df.columns = [col + '_elbow' for col in df.columns]


                
                #save to csv
                file_path_csv = csv_folder_path #f"nba_tracking/tracking_csv_2024-25"
                path = file_path_csv
                csv_path = path
                os.makedirs(csv_path, exist_ok=True)
                df.to_csv(f"{csv_path}/{modified_filename}.csv", index=False)

                display(df)


            if filename == "paint_touch_content.html":
                # Extract the text from each <th> element
                if header_row:
                    headers = [th.text.strip() for th in header_row.find_all('th')]
                    del headers[26:]
                    print(headers)
                    print(len(headers))
                    column_number = len(headers)
                else:
                    print(f"Header {modified_filename} row not found.")

                # rows = soup.find_all('tr')


                rows = soup.find_all('tbody', class_="Crom_body__UYOcU")




                extracted_data = []
                for row in rows:
                    spans = row.find_all('td')
                    row_text = [span.get_text().strip() for span in spans]
                    for i in range (0, len(row_text), column_number):
                        sublist = row_text[i:i+column_number]
                        extracted_data.append(sublist)

                # print(extracted_data)



                import pandas as pd
                df = pd.DataFrame(extracted_data, columns=headers)
                pd.set_option('display.max_rows', 1000)  # Maximum number of rows to display
                pd.set_option('display.max_columns', None)  # Show all columns
                pd.set_option('display.width', 1000)  # Adjust column width for better readability

                # df = df.rename(columns={'AST\xa0PTSCreated': 'ASTPTSCreated'})
                int_columns = ['GP', 'W', 'L']
                float_columns = [
                    'MIN', 'Touches', 'PaintTouches', 'FGM', 'FGA', 'FG%', 'FTM', 'FTA', 'FT%', 'PTS', 'PTS%', 'Pass', 'Pass%', 'AST', 'AST%', 'TO', 'TOV%', 'PF', 'PF%']

                df[int_columns] = df[int_columns].replace('-', 0).astype(int)
                df[float_columns] = df[float_columns].replace('-', 0).astype(float)
                df['PLAYER'] = df['PLAYER'].apply(unidecode)

                df.columns = [col + '_paint' for col in df.columns]


                
                #save to csv
                file_path_csv = csv_folder_path   #f"nba_tracking/tracking_csv_2024-25"
                path = file_path_csv
                csv_path = path
                os.makedirs(csv_path, exist_ok=True)
                df.to_csv(f"{csv_path}/{modified_filename}.csv", index=False)

                display(df)



            if filename == "pullup_content.html":
                # Extract the text from each <th> element
                if header_row:
                    headers = [th.text.strip() for th in header_row.find_all('th')]
                    del headers[26:]
                    print(headers)
                    print(len(headers))
                    column_number = len(headers)
                else:
                    print(f"Header {modified_filename} row not found.")

                # rows = soup.find_all('tr')


                rows = soup.find_all('tbody', class_="Crom_body__UYOcU")




                extracted_data = []
                for row in rows:
                    spans = row.find_all('td')
                    row_text = [span.get_text().strip() for span in spans]
                    for i in range (0, len(row_text), column_number):
                        sublist = row_text[i:i+column_number]
                        extracted_data.append(sublist)

                # print(extracted_data)



                import pandas as pd
                df = pd.DataFrame(extracted_data, columns=headers)
                pd.set_option('display.max_rows', 1000)  # Maximum number of rows to display
                pd.set_option('display.max_columns', None)  # Show all columns
                pd.set_option('display.width', 1000)  # Adjust column width for better readability

                # df = df.rename(columns={'AST\xa0PTSCreated': 'ASTPTSCreated'})
                int_columns = ['GP', 'W', 'L']
                float_columns = [
                    'MIN', 'PTS', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'eFG%']

                df[int_columns] = df[int_columns].replace('-', 0).astype(int)
                df[float_columns] = df[float_columns].replace('-', 0).astype(float)
                df['PLAYER'] = df['PLAYER'].apply(unidecode)

                df.columns = [col + '_pullup' for col in df.columns]


                
                #save to csv
                file_path_csv = csv_folder_path #f"nba_tracking/tracking_csv_2024-25"
                path = file_path_csv
                csv_path = path
                os.makedirs(csv_path, exist_ok=True)
                df.to_csv(f"{csv_path}/{modified_filename}.csv", index=False)

                display(df)


            if filename == "shooting_efficiency_content.html":
                # Extract the text from each <th> element
                if header_row:
                    headers = [th.text.strip() for th in header_row.find_all('th')]
                    del headers[26:]
                    headers = [header.strip().replace('\xa0', ' ') for header in headers]
                    print(headers)
                    print(len(headers))
                    column_number = len(headers) #column passed into the dataframe
                else:
                    print(f"Header {modified_filename} row not found.")

                # rows = soup.find_all('tr')


                rows = soup.find_all('tbody', class_="Crom_body__UYOcU")




                extracted_data = []
                for row in rows:
                    spans = row.find_all('td')
                    row_text = [span.get_text().strip() for span in spans]
                    for i in range (0, len(row_text), column_number):
                        sublist = row_text[i:i+column_number]
                        extracted_data.append(sublist)

                # print(extracted_data)



                import pandas as pd
                df = pd.DataFrame(extracted_data, columns=headers)
                pd.set_option('display.max_rows', 1000)  # Maximum number of rows to display
                pd.set_option('display.max_columns', None)  # Show all columns
                pd.set_option('display.width', 1000)  # Adjust column width for better readability

                # df = df.rename(columns={'AST\xa0PTSCreated': 'ASTPTSCreated'})
                int_columns = ['GP', 'W', 'L']
                float_columns = [
                    'MIN','PTS', 'DrivePTS', 'DriveFG%', 'C&SPTS', 'C&SFG%', 'Pull UpPTS', 'Pull UpFG%', 'PaintTouch PTS', 'PaintTouch FG%', 
                    'PostTouch PTS', 'PostTouch FG%', 'ElbowTouch PTS', 'ElbowTouch FG%', 'eFG%']

                df[int_columns] = df[int_columns].replace('-', 0).astype(int)
                df[float_columns] = df[float_columns].replace('-', 0).astype(float)
                df['PLAYER'] = df['PLAYER'].apply(unidecode)

                df.columns = [col + '_shot_efg' for col in df.columns]


                
                #save to csv
                file_path_csv = csv_folder_path #f"nba_tracking/tracking_csv_2024-25"
                path = file_path_csv
                csv_path = path
                os.makedirs(csv_path, exist_ok=True)
                df.to_csv(f"{csv_path}/{modified_filename}.csv", index=False)

                display(df)



            if filename == "tracking_post_ups_content.html":
                # Extract the text from each <th> element
                if header_row:
                    headers = [th.text.strip() for th in header_row.find_all('th')]
                    del headers[26:]
                    headers = [header.strip().replace('\xa0', ' ') for header in headers]
                    print(headers)
                    print(len(headers))
                    column_number = len(headers) #column passed into the dataframe
                else:
                    print(f"Header {modified_filename} row not found.")

                # rows = soup.find_all('tr')


                rows = soup.find_all('tbody', class_="Crom_body__UYOcU")




                extracted_data = []
                for row in rows:
                    spans = row.find_all('td')
                    row_text = [span.get_text().strip() for span in spans]
                    for i in range (0, len(row_text), column_number):
                        sublist = row_text[i:i+column_number]
                        extracted_data.append(sublist)

                # print(extracted_data)



                import pandas as pd
                df = pd.DataFrame(extracted_data, columns=headers)
                pd.set_option('display.max_rows', 1000)  # Maximum number of rows to display
                pd.set_option('display.max_columns', None)  # Show all columns
                pd.set_option('display.width', 1000)  # Adjust column width for better readability

                # df = df.rename(columns={'AST\xa0PTSCreated': 'ASTPTSCreated'})
                int_columns = ['GP', 'W', 'L']
                float_columns = [
                    'MIN', 'Touches', 'PostUps', 'FGM', 'FGA', 'FG%', 'FTM', 'FTA', 'FT%', 'PTS', 'PTS%', 'PASS', 'PASS%', 'AST', 'AST%', 'TO', 'TOV%', 'PF', 'PF%'
                    ]

                df[int_columns] = df[int_columns].replace('-', 0).astype(int)
                df[float_columns] = df[float_columns].replace('-', 0).astype(float)
                df['PLAYER'] = df['PLAYER'].apply(unidecode)

                df.columns = [col + '_post_ups' for col in df.columns]


                
                #save to csv
                file_path_csv = csv_folder_path #f"nba_tracking/tracking_csv_2024-25"
                path = file_path_csv
                csv_path = path
                os.makedirs(csv_path, exist_ok=True)
                df.to_csv(f"{csv_path}/{modified_filename}.csv", index=False)

                display(df)


            if filename == "touches_content.html":
                # Extract the text from each <th> element
                if header_row:
                    headers = [th.text.strip() for th in header_row.find_all('th')]
                    del headers[26:]
                    headers = [header.strip().replace('\xa0', ' ') for header in headers]
                    print(headers)
                    print(len(headers))
                    column_number = len(headers) #column passed into the dataframe
                else:
                    print(f"Header {modified_filename} row not found.")

                # rows = soup.find_all('tr')


                rows = soup.find_all('tbody', class_="Crom_body__UYOcU")




                extracted_data = []
                for row in rows:
                    spans = row.find_all('td')
                    row_text = [span.get_text().strip() for span in spans]
                    for i in range (0, len(row_text), column_number):
                        sublist = row_text[i:i+column_number]
                        extracted_data.append(sublist)

                # print(extracted_data)

                import pandas as pd
                df = pd.DataFrame(extracted_data, columns=headers)
                pd.set_option('display.max_rows', 1000)  # Maximum number of rows to display
                pd.set_option('display.max_columns', None)  # Show all columns
                pd.set_option('display.width', 1000)  # Adjust column width for better readability

                # df = df.rename(columns={'AST\xa0PTSCreated': 'ASTPTSCreated'})
                int_columns = ['GP', 'W', 'L']
                float_columns = [
                    'MIN', 'PTS', 'TOUCHES', 'Front CTTouches', 'Time OfPoss', 'Avg Sec PerTouch', 
                    'Avg Drib PerTouch', 'PTS PerTouch', 'ElbowTouches', 'PostUps', 'PaintTouches', 
                    'PTS PerElbow Touch', 'PTS PerPost Touch', 'PTS PerPaint Touch'
                    ]

                df[int_columns] = df[int_columns].replace('-', 0).astype(int)
                df[float_columns] = df[float_columns].replace('-', 0).astype(float)
                df['Player'] = df['Player'].apply(unidecode)

                df.columns = [col + '_touches' for col in df.columns]


                
                #save to csv
                file_path_csv = csv_folder_path #f"nba_tracking/tracking_csv_2024-25"
                path = file_path_csv
                csv_path = path
                os.makedirs(csv_path, exist_ok=True)
                df.to_csv(f"{csv_path}/{modified_filename}.csv", index=False)

                display(df)



if __name__ == "__main__":
    import sys
    # log_file_path = "current_usage_parser.log"
    # sys.stdout = open(log_file_path, "a")
    # sys.stderr = open(log_file_path, "a")

    if len(sys.argv) != 3:
        print("Usage: python his_usage_parser.py <sub_folder> <csv_sub_folder>")
        sys.exit(1)


    sub_folder = sys.argv[1]
    csv_sub_folder = sys.argv[2]
    tracking_parser(sub_folder, csv_sub_folder)




# tracking_parser(r"..\tracking_data\nba_html_2024-25","D:/tracking_data_csv/nba_csv_2024-25")