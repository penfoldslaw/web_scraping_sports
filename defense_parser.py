from bs4 import BeautifulSoup
import os



from bs4 import BeautifulSoup 
import os

folder_path = "nba_defense_historic/nba_html_2019-20"      #r'nba_historic\nba_html_2019'

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    # Check if it's a file (and not a subfolder)
    if os.path.isfile(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            # Read the content of the file
            html_content = file.read()
            original_filename = filename
            remove_string_in_filename = ".html"
            modified_filename = original_filename.replace(remove_string_in_filename,"") 
            #print(f"Contents of {modified_filename}")

        # Parse the HTML content
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find the table header row
        header_row = soup.find('tr', class_='Crom_headers__mzI_m') 

        # Extract the text from each <th> element
        if header_row:
            headers = [th.text.strip() for th in header_row.find_all('th')]
            print(headers)
        else:
            print("Header row not found.")

            rows = soup.find_all('tr')

            # Loop through rows and extract data
            list = []
            tbody = soup.find('tbody', class_='Crom_body__UYOcU')
            print(tbody)
            # Extract the rows and their data
            rows = tbody.find_all('tr')
            for row in rows:
                cells = row.find_all('td')
                row_data = [cell.get_text(strip=True) for cell in cells]
                #print(row_data)
                list.append(row_data)
            print(list)

            # import pandas as pd 
            # df = pd.DataFrame(list, columns=headers)

            # print(df.head(5))
            
        