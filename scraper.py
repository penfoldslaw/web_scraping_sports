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
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

# Chrome options
# chrome_options = Options()
# chrome_options.add_argument("--start-maximized")  # Example option: Start maximized
# chrome_options.add_argument("--disable-popup-blocking")

# # Initialize the WebDriver
# driver = webdriver.Chrome(
#     service=Service(ChromeDriverManager().install()), 
#     options=chrome_options
# )


#  Firefox options
firefox_options = Options()
firefox_options.add_argument("--headless")  # Run in headless mode if needed
#firefox_options.add_argument("--start-maximized")  # Run in headless mode if needed

# Initialize the Firefox WebDriver
driver = webdriver.Firefox(
    service=Service(GeckoDriverManager().install()),
    options=firefox_options
)





def scrape_data(player,season,folder_year):
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

    #time.sleep(2)


    #this click the stats page 
    stats_link = driver.find_element(By.XPATH, "//ul[@class='InnerNavTabs_list__tIFRN']/li[2]")
    stats_link.click()

    #time.sleep(2)

    # Locate and click the dropdown button for the advance stats page
    dropdown_button = driver.find_element(By.XPATH, "//*[@id='__next']/div[2]/div[2]/section/div[4]/section[1]/div/nav/div[1]/button/span")
    driver.execute_script("window.scrollBy(0, 200);")  # Scroll down by 500 pixels

    dropdown_button.click()
    #time.sleep(2)

    # Locate and click the "Career" option
    advance_option = driver.find_element(By.LINK_TEXT, 'Advanced Box Scores')
    advance_option.click()

    # delay to allow the dropdown to expand
    time.sleep(2)

    # this clicks on the dropdown for the season
    dropdown_season = driver.find_element(By.XPATH, "//*[@id='__next']/div[2]/div[2]/section/div[4]/section[2]/div/div/div[1]/label/div")
    driver.execute_script("window.scrollBy(0, 200);")  #this is to scroll down

    dropdown_season.click()
    time.sleep(2)

    #this click on the season that you want
    
    season_select = driver.find_element(By.XPATH,  f"//option[@value={season}]")
    season_select.click()
    #driver.execute_script("window.scrollBy(0, 300);") 


    time.sleep(2)

    # Extract the entire HTML page
    page_html = driver.page_source


    # Save the HTML to a file
 
    folder = os.path.join("nba_historic", f"nba_html_{folder_year}")
    file_path = os.path.join(folder, f"{player}_content.html")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(page_html)

    #time.sleep(30)
    print("All quarters printed")
    # advance stats  
    advance_filter = driver.find_element(By.XPATH, "//*[@id='__next']/div[2]/div[2]/section/div[4]/section[2]/div/div/div[4]/div[2]/button/span")
    advance_filter.click()

    time.sleep(2)

    #this select the quarters button
    select_quaters = driver.find_element(By.XPATH,"//*[@id='__next']/div[2]/div[2]/section/div[4]/section[2]/div/div/div[4]/div[1]/section[2]/div/div[3]/label/div")
    # driver.execute_script("arguments[0].scrollIntoView(true);", select_quaters)
    select_quaters.click()

    #this select q1

    xpath_quarters=["//*[@id='__next']/div[2]/div[2]/section/div[4]/section[2]/div/div/div[4]/div[1]/section[2]/div/div[3]/label/div/select/option[2]",
                    "//*[@id='__next']/div[2]/div[2]/section/div[4]/section[2]/div/div/div[4]/div[1]/section[2]/div/div[3]/label/div/select/option[3]",
                    "//*[@id='__next']/div[2]/div[2]/section/div[4]/section[2]/div/div/div[4]/div[1]/section[2]/div/div[3]/label/div/select/option[4]",
                    "//*[@id='__next']/div[2]/div[2]/section/div[4]/section[2]/div/div/div[4]/div[1]/section[2]/div/div[3]/label/div/select/option[5]"]
    
    folder_quarter_data = ["q1","q2", "q3", "q4"]
    
    for nba_quarter, folder_name in zip(xpath_quarters, folder_quarter_data):
        print(f"Processing: {nba_quarter}, {folder_name}")

        select_q = driver.find_element(By.XPATH, nba_quarter)
        select_q.click()

        get_results = driver.find_element(By.XPATH, "//*[@id='__next']/div[2]/div[2]/section/div[4]/section[2]/div/div/div[4]/div[2]/div/button[2]")
        get_results.click()


        page_html = driver.page_source




        # Save the HTML to a file
        which_q_folder = folder_name
        folder = os.path.join("nba_historic", f"nba_html_{folder_year}", "quarter_data", which_q_folder)
        file_path = os.path.join(folder, f"{player}_content_{which_q_folder}.html")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(page_html)



    
    # time.sleep(10)

    print(driver.title.encode('ascii', 'replace').decode())
    driver.quit()

if __name__ == "__main__":
    import configparser
    import sys

    # Load the configuration
    config = configparser.ConfigParser()
    config.read('scraper_config.cfg')

    # Access values
    player = config['scraper']['players'].split(',')
    season = config['scraper']['season']
    folder_year = config['scraper']['folder_year']
    print(f"scraper data: {player},{season}, {folder_year}")

    if len(sys.argv) != 4:
        print("Usage: python scraper.py <player> <season> <year>")
        sys.exit(1)

    # Get arguments from the command line
    player = sys.argv[1]
    season = sys.argv[2]
    year = sys.argv[3]

    scrape_data(player,season,folder_year)



