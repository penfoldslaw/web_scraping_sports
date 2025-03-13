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
from selenium.webdriver.support.ui import Select
from pathlib import Path
import sys
import datetime


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
firefox_options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
#firefox_options.add_argument("--headless")  # Run in headless mode if needed
firefox_options.add_argument("--start-maximized")  # Run in headless mode if needed

# Initialize the Firefox WebDriver
driver = webdriver.Firefox(service=service,options=firefox_options)

# Initialize the Firefox WebDriver when webdrive not installed manaully
# driver = webdriver.Firefox(
#     service=Service(GeckoDriverManager().install()),
#     options=firefox_options
# )




@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def scrape_data(season,main_folder,folder_year):

    log_file_path = "current_logs/current_usage_scraper.log"
    sys.stdout = open(log_file_path, "w")
    sys.stderr = open(log_file_path, "w")

    def log_with_timestamp(message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{timestamp} - {message}")
        print(f"{timestamp} - {message}", file=sys.stderr)

    log_with_timestamp("Scraping data...") 

    driver.get(f"https://www.nba.com/stats/players/usage?dir=A&sort=USG_PCT&Season={season}")
    time.sleep(5)


    # # After the player name has been searched this clicks the player note that this has only been tested for one player coming up not multiple
    all_link = driver.find_element(By.XPATH, "//*[@id='__next']/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[2]/div[1]/div[3]/div/label/div/select")
    #all_link.click()  # This simulates a click

    # Create a Select object
    select = Select(all_link)

    # Select the "All" option by visible text
    select.select_by_visible_text("All")

    time.sleep(5)

    driver.execute_script("window.scrollBy(0, 500);")

    time.sleep(5)


    # Extract the entire HTML page
    page_html = driver.page_source


    # Save the HTML to a file
    folder = os.path.join(main_folder, f"nba_html_{folder_year}")
    file_path = os.path.join(folder, f"{season}_content.html")
    os.makedirs(folder, exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(page_html)


    #time.sleep(30)
    print(f"All quarters printed {season}")
    # advance stats  



    print(driver.title.encode('ascii', 'replace').decode())

if __name__ == "__main__":
    # import sys
    # import datetime
    # log_file_path = "current_player_usage.log"
    # sys.stdout = open(log_file_path, "a")
    # sys.stderr = open(log_file_path, "a")

    # def log_with_timestamp(message):
    #     timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #     print(f"{timestamp} - {message}")
    #     print(f"{timestamp} - {message}", file=sys.stderr)

    # log_with_timestamp("Scraping data...") 

    if len(sys.argv) != 4:
        print("Usage: python scraper.py <season> <main_folder> <year>")
        sys.exit(1)

    # Get arguments from the command line

    season = sys.argv[1]
    main_folder = sys.argv[2]
    folder_year = sys.argv[3]

    try:
        scrape_data(season,main_folder,folder_year)
        driver.quit()

    except Exception as e:
        print(f"Function failed after retries: {e}")



