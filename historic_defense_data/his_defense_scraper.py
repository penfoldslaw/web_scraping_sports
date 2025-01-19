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
import sys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

service = Service(executable_path="../firefox_drive/geckodriver.exe", log_path="geckodriver.log")


#  Firefox options
firefox_options = Options()
#firefox_options.add_argument("--headless")  # Run in headless mode if needed
firefox_options.add_argument("--start-maximized")  # Run in headless mode if needed

# Initialize the Firefox WebDriver
driver = webdriver.Firefox(service=service,options=firefox_options)

def defense_scraper(main_folder,folder_season,data_season):
    
    web_site_list = [
    f"https://www.nba.com/stats/teams/advanced?Season={data_season}",
    f"https://www.nba.com/stats/teams/advanced?Season={data_season}&Period=1",
    f"https://www.nba.com/stats/teams/advanced?Season={data_season}&Period=2",
    f"https://www.nba.com/stats/teams/advanced?Season={data_season}&Period=3",
    f"https://www.nba.com/stats/teams/advanced?Season={data_season}&Period=4"       
    ]

    file_names = ["all_quarter",
    "q1",
    "q2",
    "q3",
    "q4"
    ]

    for web_site, file_names in zip(web_site_list, file_names) :
        driver.get(web_site)
        time.sleep(3)

        page_html = driver.page_source
        
        # changes to to folder path, file path and names can be done here for all quarter data
        folder = os.path.join(main_folder, f"nba_html_{folder_season}")
        file_path = os.path.join(folder, f"{file_names}_defense_content.html")
        os.makedirs(folder, exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(page_html)

        print(f"{file_names} {data_season} has been completed!!!")

    driver.quit()


if __name__ == "__main__":
    log_file_path = "his_defense_scraper.log"
    sys.stdout = open(log_file_path, "w")
    sys.stderr = open(log_file_path, "w")

    if len(sys.argv) != 4:
        print("Usage: python defense_scraper.py <main_folder> <folder_season> <data_season>")
        sys.exit(1)

    main_folder = sys.argv[1]
    folder_season = sys.argv[2]
    data_season = sys.argv[3]
    # defense_scraper(r"nba_defense_historic", "2020-21", "2020-21")
    print(f"Main folder: {main_folder}, Folder season: {folder_season}, Data season: {data_season}")
    defense_scraper(main_folder,folder_season,data_season)





