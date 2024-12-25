from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Example option: Start maximized
chrome_options.add_argument("--disable-popup-blocking")

# Initialize the WebDriver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), 
    options=chrome_options
)





def scrape_data(player,year):
    driver.get("https://www.nba.com/players")
    time.sleep(2)

    # This locates the search bar by its 'aria-label' attribute
    search_bar = driver.find_element(By.XPATH, "//input[@aria-label='Player Natural Search Bar']")

    # Enter the search term
    search_term = player
    search_bar.send_keys(search_term)


    # Trigger the search (e.g., press Enter)
    search_bar.send_keys(Keys.RETURN)
    
    # This is so it gives it time to reload
    time.sleep(2)


    # After the player name has been searched this clicks the player note that this has only been tested for one player coming up not multiple
    player_link = driver.find_element(By.XPATH, "//div[@class='RosterRow_playerName__G28lg']")
    player_link.click()  # This simulates a click

    time.sleep(2)


    #this click the stats page 
    stats_link = driver.find_element(By.XPATH, "//ul[@class='InnerNavTabs_list__tIFRN']/li[2]")
    stats_link.click()

    time.sleep(2)

    # Locate and click the dropdown button for the advance stats page
    dropdown_button = driver.find_element(By.CLASS_NAME, "ArrowToggleButton_arrowText__ep3Dn")
    dropdown_button.click()
    time.sleep(2)

    # Locate and click the "Career" option
    advance_option = driver.find_element(By.LINK_TEXT, 'Advanced Box Scores')
    #scroll to the advance_option to prevent the code from breaking
    driver.execute_script("window.scrollBy(0, 500);")  # Scroll down by 500 pixels
    ## another option if this keeps breaking is to find the button for advance click it so the option will become avaliable and click on that
    advance_option.click()

    # Add another brief delay to allow the dropdown to expand
    time.sleep(2)

    # this clicks on the dropdown for the season
    dropdown_season = driver.find_element(By.XPATH, "//div[@class='DropDown_dropdown__TMlAR']")
    dropdown_season.click()
    time.sleep(2)

    #this click on the season that you want
    season_year = year
    season = driver.find_element(By.XPATH,  f"//option[@value={season_year}]")
    season.click()

    time.sleep(2)

    # Extract the entire HTML page
    page_html = driver.page_source


    # Save the HTML to a file
    folder = os.path.join("nba_historic", f"nba_html_{season_year}")
    file_path = os.path.join(folder, f"{player}_content.html")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(page_html)

    # time.sleep(30)

    print(driver.title.encode('ascii', 'replace').decode())
    driver.quit()

if __name__ == "__main__":
    scrape_data("Paul George",'"2019-20"')



