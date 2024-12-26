from bs4 import BeautifulSoup

# Correct file path
file_path = r"nba_historic\nba_html_2019\Paul George_content.html"

# Open the file with UTF-8 encoding
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Print the parsed HTML
print(soup.prettify())

