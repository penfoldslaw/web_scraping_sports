# from bs4 import BeautifulSoup
# import requests

# url = 'https://www.nba.com/stats/leaders?PerMode=Totals'
# response = requests.get(url)
# html_content = response.content

# #print(html_content)

# with open('nba_html_2024.html', 'r', encoding='utf-8') as file:
#     html_content = file.read()


# soup = BeautifulSoup(html_content, 'html.parser')
# table = soup.find('table', class_='Crom_table__p1iZz')

# #headers = [header.text for header in table.find_all('th')]
# # for heading in headings:
# #     print(heading.text)


# # Parse the HTML content with BeautifulSoup
# soup = BeautifulSoup(html_content, 'html.parser')

# # Find the table
# table = soup.find('table', class_='Crom_table__p1iZz')

# # Extract headers
# headers = [header.text.strip() for header in table.find_all('th')]

# # stats = [headers.text.strip() for headers in table.find_all('a', href='/stats/')]
# stats = [headers.text.strip() for headers in table.find_all('td')]

# tr_elements = soup.find_all('tr')


# giannis_tag = soup.find('a', href='/stats/player/203507/')



# table_data = []
# for tr in tr_elements:
#     row_data = [td.get_text(strip=True) for td in tr.find_all('td')]
#     table_data.append(row_data)


# print(table_data)


import requests
import pandas as pd

#url = 'https://stats.nba.com/stats/boxscorescoringv3'
url = 'https://stats.nba.com/stats/boxscoretraditionalv3'
headers = {
'Referer': 'https://www.nba.com/',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
payload = {
'GameID': '0022000911',
'LeagueID': '00',
'endPeriod': '0',
'endRange': '28800',
'rangeType': '0',
'startPeriod': '0',
'startRange': '0'}

jsonData = requests.get(url, headers=headers, params=payload).json()

# #away_df = pd.json_normalize(jsonData['boxScoreScoring']['awayTeam']['players'])
# #home_df = pd.json_normalize(jsonData['boxScoreScoring']['homeTeam']['players']) 
# away_df = pd.json_normalize(jsonData['boxScoreTraditional']['awayTeam']['players'])
# home_df = pd.json_normalize(jsonData['boxScoreTraditional']['homeTeam']['players'])

print(jsonData)