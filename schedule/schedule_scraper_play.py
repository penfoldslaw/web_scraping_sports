


# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=True)
#     page = browser.new_page()

#     # Go to the ESPN NBA schedule page
#     page.goto("https://www.espn.com/nba/schedule")

#     # Wait for the schedule table to load
#     page.wait_for_selector(".Table__TBODY")

#     # Grab each row in the schedule
#     games = page.query_selector_all(".Table__TBODY .Table__TR")
#     # print(games)

#     schedule = []
#     for game in games:
#         try:
#             teams = game.query_selector_all(".matchTeams .Table__Team a")
            
#             if len(teams) != 2:
#                 continue

#             away_team = teams[0].inner_text().strip()
#             home_team = teams[1].inner_text().strip()

#             time_elem = game.query_selector(".date__col a")
#             time = time_elem.inner_text().strip() if time_elem else "TBD"

#             ticket_elem = game.query_selector(".tickets__col a span")
#             tickets = ticket_elem.inner_text().strip() if ticket_elem else "No tickets"

#             schedule.append({
#                 "away_team": away_team,
#                 "home_team": home_team,
#                 "time": time,
#                 "tickets": tickets
#             })
#         except Exception as e:
#             print(f"Error parsing row: {e}")

#     browser.close()

# # Print or save the schedule
# for g in schedule:
#     print(f"{g['away_team']} @ {g['home_team']} - {g['time']} - {g['tickets']}")

from playwright.sync_api import sync_playwright
import os
import sys

year = "2024-25"

log_file_path = "current_logs/schedule_parser.log"
sys.stdout = open(log_file_path, "w")
sys.stderr = open(log_file_path, "w")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # or headless=False to see it
    page = browser.new_page()
    page.goto("https://www.espn.com/nba/schedule")
    
    # scroll up 500 pixels
    page.evaluate("window.scrollBy(0, -500)")
    
    # Get the entire HTML of the page
    html = page.content()

    # Save to file
    folder = os.path.join("D:/nba_schedules_play", f"nba_html_{year}")
    file_path = os.path.join(folder, f"schedule_content.html")
    os.makedirs(folder, exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)


    print(f"playwright schedule has been completed!!!")

    browser.close()
