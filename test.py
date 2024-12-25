from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Example option: Start maximized

# Initialize the WebDriver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), 
    options=chrome_options
)

driver.get("https://www.nba.com/players")

# Locate the search bar by its 'aria-label' attribute
search_bar = driver.find_element(By.XPATH, "//input[@aria-label='Player Natural Search Bar']")

# Enter the search term
search_term = "Giannis Antetokounmpo"
search_bar.send_keys(search_term)

# Trigger the search (e.g., press Enter)
search_bar.send_keys(Keys.RETURN)

# Wait for the results to load
time.sleep(5)

# Locate the link by matching the text 'Giannis Antetokounmpo'
player_link = driver.find_element(By.XPATH, "//div[@class='RosterRow_playerName__G28lg']")
player_link.click()  # This simulates a click

time.sleep(5)  # Replace with WebDriverWait for robustness

#this click the stats page 
stats_link = driver.find_element(By.XPATH, "//ul[@class='InnerNavTabs_list__tIFRN']/li[2]")
stats_link.click()

time.sleep(5)


# Locate and click the dropdown button
dropdown_button = driver.find_element(By.CLASS_NAME, "ArrowToggleButton_arrowText__ep3Dn")
dropdown_button.click()

# Add another brief delay to allow the dropdown to expand
time.sleep(5)


# Locate and click the "Career" option
career_option = driver.find_element(By.LINK_TEXT, 'Advanced Box Scores')
career_option.click()


# this clicks on the dropdown for the season
dropdown_season = driver.find_element(By.XPATH, "//div[@class='DropDown_dropdown__TMlAR']")
dropdown_season.click()
time.sleep(5)

#this click on the season that you want
season = driver.find_element(By.XPATH,  "//option[@value='2019-20']")
season.click()

time.sleep(5)

time.sleep(10)

# Extract the entire HTML page
page_html = driver.page_source


# Save the HTML to a file
with open("dropdown_content.html", "w", encoding="utf-8") as file:
    file.write(page_html)

time.sleep(30)


print(driver.title)
driver.quit()
