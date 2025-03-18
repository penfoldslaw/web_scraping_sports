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
import sys
import datetime
from pathlib import Path

path = Path(__file__).resolve().parents[1]
# service = Service(executable_path=path / "../firefox_drive/geckodriver.exe", log_path="geckodriver.log") # for inside directory run
service = Service(executable_path=path / "firefox_drive/geckodriver.exe", log_path="geckodriver.log")


#  Firefox options
firefox_options = Options()
firefox_options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
# firefox_options.add_argument("--headless")  # Run in headless mode if needed
firefox_options.add_argument("--start-maximized")  # Run in headless mode if needed

# Initialize the Firefox WebDriver
driver = webdriver.Firefox(service=service,options=firefox_options)


@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def scrape_data(http, matchup,main_folder,date_of_match):

    # log_path = "box_score_data/box_score_log"
    # os.makedirs(log_path, exist_ok= True)
    # log_file_path = "box_score_log/box_score_scraper.log"
    # sys.stdout = open(log_file_path, "a")
    # sys.stderr = open(log_file_path, "a")

    def log_with_timestamp(message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{timestamp} - {message}")
        print(f"{timestamp} - {message}", file=sys.stderr)

    log_with_timestamp("Scraping data...") 


    driver.get(http)
    time.sleep(3)



    driver.execute_script("window.scrollBy(0, 800);")

    time.sleep(3)


    # Extract the entire HTML page
    page_html = driver.page_source


    # Save the HTML to a file
    folder = os.path.join(main_folder, f"nba_html_{date_of_match}")
    file_path = os.path.join(folder, f"{matchup}_content.html")
    os.makedirs(folder, exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(page_html)


    #time.sleep(30)
    print(f"Box score {matchup} printed")
    # advance stats  



    print(driver.title.encode('ascii', 'replace').decode())


if __name__ == "__main__":

    if len(sys.argv) != 5:
        print("Usage: python box_scraper.py <http> <matchup> <folder_path> <date>")
        sys.exit(1)

    # Get arguments from the command line

    http = sys.argv[1]
    matchup = sys.argv[2]
    main_folder = sys.argv[3]
    date_of_match = sys.argv[4]

    try:
        scrape_data(http,matchup,main_folder,date_of_match)
        driver.quit()


    except Exception as e:
        print(f"Function failed after retries: {e}")



# scrape_data("https://www.nba.com/game/bos-vs-mia-0022400958/box-score","bos-mia","box_score_data/box_score", "3-14-25")