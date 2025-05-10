from nba_api.stats.endpoints import commonteamroster
from nba_api.stats.static import teams
import pandas as pd
from unidecode import unidecode
from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats.endpoints import commonteamroster
import requests

# Patch requests.Session.request to always include custom headers
original_request = requests.Session.request

def patched_request(self, method, url, **kwargs):
    headers = kwargs.get("headers", {})
    headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' +
                      '(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://www.nba.com/',
        'Origin': 'https://www.nba.com',
        'x-nba-stats-origin': 'stats',
        'x-nba-stats-token': 'true'
    })
    kwargs["headers"] = headers
    return original_request(self, method, url, **kwargs)

requests.Session.request = patched_request

def get_team_roster():

    team_abbreviations = [
        "BOS", "BKN", "NYK", "PHI", "TOR",  # Atlantic Division
        "CHI", "CLE", "DET", "IND", "MIL",  # Central Division
        "ATL", "CHA", "MIA", "ORL", "WAS",  # Southeast Division
        "DEN", "MIN", "OKC", "POR", "UTA",  # Northwest Division
        "GSW", "LAC", "LAL", "PHX", "SAC",  # Pacific Division
        "DAL", "HOU", "MEM", "NOP", "SAS"   # Southwest Division
    ]


    # Get all NBA teams and create a mapping of abbreviations to team IDs
    nba_teams = teams.get_teams()
    team_id_map = {team['abbreviation']: team['id'] for team in nba_teams}

    # Dictionary to store team rosters
    team_rosters = {}

    # Loop through each team
    for team_abbr in team_abbreviations:
        team_id = team_id_map[team_abbr]

        # Specify the season in 'YYYY-YY' format
        season = '2024-25'

        # Retrieve the team's roster
        roster = commonteamroster.CommonTeamRoster(team_id=team_id, season=season)

        # Convert the roster data to a pandas DataFrame
        roster_df = roster.get_data_frames()[0]

        # Normalize player names by removing accents
        roster_df['PLAYER_uni'] = roster_df['PLAYER'].apply(unidecode)


        roster_df['api_team_name'] = team_abbr

        # Store the roster for the team
        team_rosters[team_abbr] = roster_df

        # Display rosters
    import pandas as pd
    import os
    from IPython.display import display
    for team_abbr, roster_df in team_rosters.items():
        print(f"\n{team_abbr} Roster:")
        display(roster_df[['PLAYER_uni','POSITION','api_team_name']])
        # roster = roster.DataFrame(ri)
        directory = "D:/roster_folder/2024"
        os.makedirs(directory, exist_ok=True)
        roster_df.to_csv(fr"{directory}/{team_abbr}_roster_file.csv", index=False)


get_team_roster()



