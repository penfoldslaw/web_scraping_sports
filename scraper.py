from bs4 import BeautifulSoup
import requests

url = 'https://www.nba.com/stats/leaders?PerMode=Totals'
response = requests.get(url)
html_content = response.content

#print(html_content)


soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find('table', class_='Crom_table__p1iZz')

#headers = [header.text for header in table.find_all('th')]
# for heading in headings:
#     print(heading.text)
print(soup[:100])