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
from tenacity import retry, stop_after_attempt, wait_fixed
from pathlib import Path

path = Path(__file__).resolve().parents[1]
# service = Service(executable_path=path / "../firefox_drive/geckodriver.exe", log_path="geckodriver.log") # for inside directory run
service = Service(executable_path=path / "firefox_drive/geckodriver.exe", log_path="geckodriver.log")
#driver = webdriver.Firefox(service=service)

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
# firefox_options.add_argument("--headless")  # Run in headless mode if needed
firefox_options.add_argument("--start-maximized")  # Run in headless mode if needed

# Initialize the Firefox WebDriver
driver = webdriver.Firefox(service=service,options=firefox_options)

# Initialize the Firefox WebDriver when webdrive not installed manaully
# driver = webdriver.Firefox(
#     service=Service(GeckoDriverManager().install()),
#     options=firefox_options
# )




@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def scrape_data(player,season,main_folder,folder_year,quarter_data):
    driver.get("https://www.nba.com/players")
    time.sleep(4)

    # This locates the search bar by its 'aria-label' attribute
    search_bar = driver.find_element(By.XPATH, "//input[@aria-label='Player Natural Search Bar']")

    # Enter the search term
    search_term = player
    search_bar.send_keys(search_term)


    # Trigger the search (e.g., press Enter)
    search_bar.send_keys(Keys.RETURN)
    
    # This is so it gives it time to reload
    time.sleep(4)


    # After the player name has been searched this clicks the player note that this has only been tested for one player coming up not multiple
    player_link = driver.find_element(By.XPATH, "//div[@class='RosterRow_playerName__G28lg']")
    player_link.click()  # This simulates a click

    time.sleep(4)


    #this click the stats page 
    stats_link = driver.find_element(By.XPATH, "//ul[@class='InnerNavTabs_list__tIFRN']/li[2]")
    stats_link.click()

    time.sleep(4)


    current_url = driver.current_url

    if not current_url.endswith("/boxscores-traditional"):
        updated_url = current_url + f"/boxscores-traditional?Season={season}"
        driver.get(updated_url)  # Navigate to the updated URL
    driver.execute_script("window.scrollBy(0, 500);") 

   


    time.sleep(4)

    # Extract the entire HTML page
    page_html = driver.page_source


    # Save the HTML to a file
    #main_folder = main_folder
    folder = os.path.join(main_folder, f"nba_html_{folder_year}")
    file_path = os.path.join(folder, f"{player}_content.html")
    os.makedirs(folder, exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(page_html)

    

    #time.sleep(30)
    print(f"All quarters printed {season} {player}")
    # advance stats  
    if quarter_data == 'yes':
        if not current_url.endswith("/boxscores-traditional"):
            updated_url = current_url + f"/boxscores-traditional?Season={season}"
            driver.get(updated_url)  # Navigate to the updated URL

        driver.execute_script("window.scrollBy(0, 500);") 
        time.sleep(4)

        xpath_quarters=["1","2","3","4"]
        
        folder_quarter_data = ["q1","q2", "q3", "q4"]
        
        for nba_quarter, folder_name in zip(xpath_quarters, folder_quarter_data):
            print(f"Processing: period {nba_quarter}, {folder_name}")

            if not current_url.endswith(f"/boxscores-traditional?Season={season}"):
                updated_url = current_url + f"/boxscores-traditional?Season={season}&Period={nba_quarter}"
                driver.get(updated_url)  # Navigate to the updated URL
            time.sleep(4)

            driver.execute_script("window.scrollBy(0, 500);")

            time.sleep(1) 

            page_html = driver.page_source


            # Save the HTML to a file
            which_q_folder = folder_name
            folder = os.path.join(main_folder, f"nba_html_{folder_year}", "quarter_data", which_q_folder)
            os.makedirs(folder, exist_ok=True)
            file_path = os.path.join(folder, f"{player}_content_{which_q_folder}.html")
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(page_html)




    
    # time.sleep(10)

    print(driver.title.encode('ascii', 'replace').decode())
    driver.quit()

if __name__ == "__main__":
    import sys
    import datetime
    log_file_path = "history_logs/his_player_scraper.log"
    sys.stdout = open(log_file_path, "a")
    sys.stderr = open(log_file_path, "a")

    def log_with_timestamp(message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{timestamp} - {message}")
        print(f"{timestamp} - {message}", file=sys.stderr)

    log_with_timestamp("Scraping data...") 

    if len(sys.argv) != 6:
        print("Usage: python scraper.py <player> <season> <main_folder> <year>")
        sys.exit(1)

    # Get arguments from the command line
    player = sys.argv[1]
    season = sys.argv[2]
    main_folder = sys.argv[3]
    folder_year = sys.argv[4]
    quarter_data = sys.argv[5] if len(sys.argv) > 5 else 'no'

    try:
        scrape_data(player,season,main_folder,folder_year,quarter_data)
        # driver.quit()

    except Exception as e:
        print(f"Function failed after retries: {e}")



