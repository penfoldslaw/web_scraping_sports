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

service = Service(executable_path="../firefox_drive/geckodriver.exe", log_path="geckodriver.log")
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
firefox_options.add_argument("--headless")  # Run in headless mode if needed
#firefox_options.add_argument("--start-maximized")  # Run in headless mode if needed

# Initialize the Firefox WebDriver
driver = webdriver.Firefox(service=service,options=firefox_options)

# Initialize the Firefox WebDriver when webdrive not installed manaully
# driver = webdriver.Firefox(
#     service=Service(GeckoDriverManager().install()),
#     options=firefox_options
# )


def schedule_scraper(team,year):
    driver.get(f"https://www.espn.com/nba/team/schedule/_/name/{team}/season/{year}")
    time.sleep(3)

    page_html = driver.page_source

    folder = os.path.join("nba_schedules", f"nba_html_{year}")
    file_path = os.path.join(folder, f"{team}_schedule_content.html")
    os.makedirs(folder, exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(page_html)

    print(f"{team} {year} has been completed!!!")



if __name__ == "__main__":
    import sys
    import datetime
    log_file_path = "schedule_scraper.log"
    sys.stdout = open(log_file_path, "a")
    sys.stderr = open(log_file_path, "a")

    def log_with_timestamp(message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{timestamp} - {message}")
        print(f"{timestamp} - {message}", file=sys.stderr)

    log_with_timestamp("Scraping data...") 

    if len(sys.argv) != 3:
        print("Usage: python defense_scraper.py <team> <year> ")
        sys.exit(1)

    
    team = sys.argv[1]
    year = sys.argv[2]
    # defense_scraper(r"nba_defense_historic", "2020-21", "2020-21")
    schedule_scraper (team,year)
    driver.quit()
