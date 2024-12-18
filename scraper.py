from bs4 import BeautifulSoup
import requests

url = 'https://www.nba.com/stats/leaders?PerMode=Totals'
response = requests.get(url)
html_content = response.content

#print(html_content)

with open('nba_html_2024.html', 'r', encoding='utf-8') as file:
    html_content = file.read()


soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find('table', class_='Crom_table__p1iZz')

#headers = [header.text for header in table.find_all('th')]
# for heading in headings:
#     print(heading.text)


# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the table
table = soup.find('table', class_='Crom_table__p1iZz')

# Extract headers
headers = [header.text.strip() for header in table.find_all('th')]

# stats = [headers.text.strip() for headers in table.find_all('a', href='/stats/')]
stats = [headers.text.strip() for headers in table.find_all('td')]

tr_elements = soup.find_all('tr')


giannis_tag = soup.find('a', href='/stats/player/203507/')



table_data = []
for tr in tr_elements:
    row_data = [td.get_text(strip=True) for td in tr.find_all('td')]
    table_data.append(row_data)


print(table_data)