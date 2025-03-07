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
from selenium.webdriver.support.ui import Select
import datetime
from tenacity import retry, stop_after_attempt, wait_fixed
from pathlib import Path


# this launches the firefox browser
path = Path(__file__).resolve().parents[1]
service = Service(executable_path=path / "firefox_drive/geckodriver.exe", log_path="geckodriver.log")


#  Firefox options
firefox_options = Options()
# firefox_options.add_argument("--headless")  # Run in headless mode if needed
firefox_options.add_argument("--start-maximized")  # Run in headless mode if needed

# Initialize the Firefox WebDriver
driver = webdriver.Firefox(service=service,options=firefox_options)

season = "2023-24"

driver.get(f"https://www.nba.com/stats/players/passing?Season={season}")
time.sleep(2)

driver.execute_script("window.scrollBy(0, 500);") 




all_link = driver.find_element(By.XPATH, "//*[@id='__next']/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[2]/div[1]/div[3]/div/label/div/select/option[1]")

all_link.click()


# Extract the entire HTML page
page_html = driver.page_source

# Save the HTML to a file
#main_folder = main_folder
main_folder = "tracking_data"
folder_year = season
track_data = "passing"

folder = os.path.join(main_folder, f"nba_html_{folder_year}")
file_path = os.path.join(folder, f"{track_data}_content.html")
os.makedirs(folder, exist_ok=True)
with open(file_path, "w", encoding="utf-8") as file:
    file.write(page_html)




current_url = driver.current_url

def url_check(url,track_data):
    if not current_url.endswith("/this_is_so_the_url_changes"):
        updated_url = url
        driver.get(updated_url)

    time.sleep(2)

    driver.execute_script("window.scrollBy(0, 500);") 

    all_link = driver.find_element(By.XPATH, "//*[@id='__next']/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[2]/div[1]/div[3]/div/label/div/select/option[1]")

    all_link.click()

    page_html = driver.page_source

    folder = os.path.join(main_folder, f"nba_html_{folder_year}")
    file_path = os.path.join(folder, f"{track_data}_content.html")
    os.makedirs(folder, exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(page_html)

url_check(f"https://www.nba.com/stats/players/catch-shoot?Season={season}", "catch_shoot")


url_check(f"https://www.nba.com/stats/players/pullup?Season={season}", "pullup")

url_check(f"https://www.nba.com/stats/players/shooting-efficiency?Season={season}", "shooting_efficiency")

url_check(f"https://www.nba.com/stats/players/drives?Season={season}", "drives")

url_check(f"https://www.nba.com/stats/players/tracking-post-ups?Season={season}", "tracking_post_ups")

url_check(f"https://www.nba.com/stats/players/paint-touch?Season={season}", "paint_touch")

url_check(f"https://www.nba.com/stats/players/elbow-touch?Season={season}", "elbow_touch")

url_check(f"https://www.nba.com/stats/players/touches?Season={season}", "touches")

driver.quit()








