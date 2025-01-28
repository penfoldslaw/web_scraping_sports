import os
import pandas as pd
from pathlib import Path
from IPython.display import display

# Helper function to build the paths with customizable base path
def build_data_path(base_path, player=None, date=None):
    # Replace placeholders with actual values
    return base_path.format(date=date, player=player)
    

def his_player_defense_data(player, date, player_base_path, defense_base_path):
    player_dataframes = {}  # Dictionary to store each player's DataFrame
    defense_dataframes = {}  # Dictionary to store each player's defense DataFrame

    single_player_df = pd.DataFrame()  # Initialize a DataFrame for the current player
    defense_df = pd.DataFrame()  # Initialize a DataFrame for the current player's defense

    # Get the data paths using the helper function and the custom base paths
    path = build_data_path(player_base_path, player, date)
    #print(path)
    path_defense = build_data_path(defense_base_path, player, date)
    #print(path_defense)

    # Check if files exist and process them
    if os.path.exists(path) and os.path.exists(path_defense):
        # Player data
        season_df_player = pd.read_csv(path)
        season_df_player['season'] = date
        single_player_df = pd.concat([single_player_df, season_df_player], ignore_index=True)

        # Defense data
        defense_df_season = pd.read_csv(path_defense)
        defense_df_season['season_defense'] = date
        defense_df = pd.concat([defense_df, defense_df_season], ignore_index=True)
    else:
        print(f'{date} not found for {player} or defense')

    # Add player data to the dictionary
    player_dataframes[player] = single_player_df
    defense_dataframes[player] = defense_df

    # Merge the player and defense data on 'season' and 'TEAM' fields
    try:
        merged_df = pd.merge(single_player_df, defense_df, how='inner', left_on=['Away', 'season'], right_on=['TEAM', 'season_defense']).reset_index(drop=True)
        merged_df = merged_df.sort_values(by="Date")
    except Exception as e:
        print(f"Data most likely doesn't exist for {player} or  defense doesn't exit for this {date} or error checker{e}")

    pd.set_option('display.max_rows', 1000)  # Maximum number of rows to display
    pd.set_option('display.max_columns', None)  # Show all columns
    pd.set_option('display.width', 1000)  # Adjust column width for better readability

    

    return merged_df


if __name__ == "__main__":
    raise ImportError("This script is intended to be imported as a module, not executed directly.")
    # example use case:
    # player = "James Harden"
    # date = "2019-20"
    # player_base_path = "../../historic_player_data/nba_ph_csv/season_{date}/all_quarters/{player}_content.csv"
    # defense_base_path = "../../historic_defense_data/nba_dh_csv/defense_csv_{date}/all_quarter_defense_content.csv"

    # his_player_defense_data(player, date, player_base_path, defense_base_path)
    


