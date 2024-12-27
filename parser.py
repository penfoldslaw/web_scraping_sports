from bs4 import BeautifulSoup

# Correct file path
file_path = r"nba_historic\nba_html_2019\Paul George_content.html"

# Open the file with UTF-8 encoding
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Print the parsed HTML
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

# Extract the rows and their data
rows = tbody.find_all('tr')
for row in rows:
    cells = row.find_all('td')
    row_data = [cell.get_text(strip=True) for cell in cells]
    print(row_data)
    list.append(row_data)
print(list)

import pandas as pd 
df = pd.DataFrame(list, columns=headers)
print(df.head(50))

