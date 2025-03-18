import os
import pandas as pd
from pathlib import Path
from IPython.display import display

# Helper function to build the paths with customizable base path
def build_data_path(base_path, **Kwargs):
    # Replace placeholders with actual values
    for key, value in Kwargs.items():
        base_path=base_path.replace(f"{{{key}}}", str(value))
    return base_path
    
    

# def his_player_defense_data(player_base_path, defense_base_path,player, date):

#     """
#         Retrieves and merges player, defensive, and schedule data for a given player and date.

#         This function loads player statistics, defensive metrics, and schedule details 
#         from CSV files, merges them, and returns a combined dataset with relevant statistics.

#         Parameters:
#             player_base_path (str): The base path for player data files.
#             defense_base_path (str): The base path for defensive statistics files.
#             player (str): The player's name.
#             date (str): The specific date for which data is needed.
#             schedule_team (str): The team name used for retrieving the schedule data.

#         Returns:
#             tuple:
#                 - merged_df_schedule (DataFrame): A DataFrame containing merged player, 
#                 defense, and schedule data.
#                 - defense_historic_player (DataFrame): A DataFrame with defensive stats 
#                 (TEAM, PACE, OffRtg) for the player's team.
#     """


#     player_dataframes = {}  # Dictionary to store each player's DataFrame
#     defense_dataframes = {}  # Dictionary to store each player's defense DataFrame

#     single_player_df = pd.DataFrame()  # Initialize a DataFrame for the current player
#     defense_df = pd.DataFrame()  # Initialize a DataFrame for the current player's defense

#     # Get the data paths using the helper function and the custom base paths
#     path = build_data_path(player_base_path, player=player, date=date)
#     # print(path)
#     path_defense = build_data_path(defense_base_path, date=date)
#     # print(path_defense)

#     # Check if files exist and process them
#     if os.path.exists(path) and os.path.exists(path_defense):
#         # Player data
#         season_df_player = pd.read_csv(path)
#         season_df_player['season'] = date
#         single_player_df = pd.concat([single_player_df, season_df_player], ignore_index=True)

#         # Defense data
#         defense_df_season = pd.read_csv(path_defense)
#         defense_df_season['season_defense'] = date
#         defense_df = pd.concat([defense_df, defense_df_season], ignore_index=True)
#     else:
#         print(f'{date} not found for {player} or defense')

#     # Add player data to the dictionary
#     player_dataframes[player] = single_player_df
#     defense_dataframes[player] = defense_df

#     # Merge the player and defense data on 'season' and 'TEAM' fields
#     try:
#         merged_df = pd.merge(single_player_df, defense_df, how='inner', left_on=['Away', 'season'], right_on=['TEAM', 'season_defense']).reset_index(drop=True)
#         merged_df = merged_df.sort_values(by="Date")
#         defense_current_player = defense_df

#     except Exception as e:
#         print(f"Data most likely doesn't exist for {player} or  defense doesn't exit for this {date} or error checker {e}")

#     pd.set_option('display.max_rows', 1000)  # Maximum number of rows to display
#     pd.set_option('display.max_columns', None)  # Show all columns
#     pd.set_option('display.width', 1000)  # Adjust column width for better readability
    

#     return merged_df, defense_current_player


def his_player_defense_data(player_base_path, defense_base_path, player, date):
    """
    Retrieves and merges player, defensive, and schedule data for a given player and date.
    Returns empty DataFrames if data is missing instead of stopping execution.
    """

    player_dataframes = {}
    defense_dataframes = {}

    single_player_df = pd.DataFrame()
    defense_df = pd.DataFrame()

    path = build_data_path(player_base_path, player=player, date=date)
    path_defense = build_data_path(defense_base_path, date=date)

    # Check if the necessary files exist
    if os.path.exists(path):
        season_df_player = pd.read_csv(path)
        season_df_player['season'] = date
        single_player_df = pd.concat([single_player_df, season_df_player], ignore_index=True)
    else:
        print(f'Player data missing for {player} on {date}, skipping.')

    if os.path.exists(path_defense):
        defense_df_season = pd.read_csv(path_defense)
        defense_df_season['season_defense'] = date
        defense_df = pd.concat([defense_df, defense_df_season], ignore_index=True)
    else:
        print(f'Defense data missing for {date}, skipping.')

    player_dataframes[player] = single_player_df
    defense_dataframes[player] = defense_df

    # Try merging only if both DataFrames have data
    if not single_player_df.empty and not defense_df.empty:
        try:
            merged_df = pd.merge(
                single_player_df, defense_df,
                how='inner', left_on=['Away', 'season'], right_on=['TEAM', 'season_defense']
            ).reset_index(drop=True)

            merged_df = merged_df.sort_values(by="Date")
            defense_current_player = defense_df

        except Exception as e:
            print(f"Merge error for {player} on {date}: {e}")
            merged_df = pd.DataFrame()
            defense_current_player = pd.DataFrame()
    else:
        print(f'Skipping merge for {player} on {date} due to missing data.')
        merged_df = pd.DataFrame()
        defense_current_player = pd.DataFrame()

    return merged_df, defense_current_player


def current_player_defense_data(player_base_path, defense_base_path,schedule_base_path,player,date,schedule_team):

    """
        Retrieves and merges player, defensive, and schedule data for a given player and date.

        This function loads player statistics, defensive metrics, and schedule details 
        from CSV files, merges them, and returns a combined dataset with relevant statistics.

        Parameters:
            player_base_path (str): The base path for player data files.
            defense_base_path (str): The base path for defensive statistics files.
            schedule_base_path (str): The base path for game schedule files.
            player (str): The player's name.
            date (str): The specific date for which data is needed.
            schedule_team (str): The team name used for retrieving the schedule data.

        Returns:
            tuple:
                - merged_df_schedule (DataFrame): A DataFrame containing merged player, 
                defense, and schedule data.
                - defense_current_player (DataFrame): A DataFrame with defensive stats 
                (TEAM, PACE, OffRtg) for the player's team.
    """




    single_player_df = pd.DataFrame()
    defense_df = pd.DataFrame()
    schedule_df = pd.DataFrame()

    path = build_data_path(player_base_path, player=player, date=date)
    path_defense = build_data_path(defense_base_path, date=date)
    path_schedule = build_data_path(schedule_base_path, schedule_team=schedule_team, date=date)
    


    if os.path.exists(path) and os.path.exists(path_defense):
        # Player data
        season_df_player = pd.read_csv(path)
        season_df_player['season'] = date
        single_player_df = pd.concat([single_player_df, season_df_player], ignore_index=True).drop_duplicates()

        # Defense data
        defense_df_season = pd.read_csv(path_defense)
        defense_df_season['season_defense'] = date
        defense_df = pd.concat([defense_df, defense_df_season], ignore_index=True).drop_duplicates()

        # Schedule data
        season_df_schedule = pd.read_csv(path_schedule)
        season_df_schedule['season_schedule'] = date
        schedule_df = pd.concat([schedule_df, season_df_schedule], ignore_index=True).drop_duplicates()

    else:
        print(f'{date} not found either for {player} or defense')


    pd.set_option('display.max_rows', 1000)  # Maximum number of rows to display
    pd.set_option('display.max_columns', None)  # Show all columns
    pd.set_option('display.width', 1000)  # Adjust column width for better readability
    
    try:
        merged_df = pd.merge(single_player_df, defense_df, how='inner', left_on=['Away', 'season'], right_on=['TEAM', 'season_defense']).reset_index(drop=True)
        merged_df = merged_df.sort_values(by="Date")
        merged_df_schedule = pd.merge(merged_df, schedule_df, how='inner', left_on='Team',right_on='home_team').drop_duplicates().reset_index(drop=True)
        defense_current_player = defense_df[['TEAM','PACE','OffRtg']]
    except Exception as e:
        print(f"Data most likely doesn't exist for {player} or  defense doesn't exit for this {date} or error checker {e}")
    
    return merged_df_schedule , defense_current_player



def tracking_and_usage(stats_path:dict,date):
    stats_dataframe = {}  # Dictionary to store each stats DataFrame
    # all_stats_df = pd.DataFrame()  # Initialize a DataFrame for the each stats

    for stats_name,stats_data in stats_path.items():


        all_path =build_data_path(stats_data,date=date)

        if os.path.exists(all_path):
            ind_stats_df = pd.read_csv(all_path)
            ind_stats_df['season'] = date
            # all_stats_df = pd.concat([all_stats_df, ind_stats_df], ignore_index=True)
        else:
            print(f'{date} not found for {stats_name}')


        stats_dataframe[stats_name] = ind_stats_df

    return stats_dataframe




def his_usage_team(player_names: dict, date_list: list,stats_path:dict,player_base_path,defense_base_path):
    """
        Computes historical usage data for a given set of players over a list of dates.

        This function merges player statistics, usage data, and defensive statistics 
        to create a dataset containing various metrics such as usage percentage (USG%), 
        team pace, offensive rating, and possession data.

        Parameters:
            player_names (dict): A dictionary mapping player names to their respective teams.
            date_list (list): A list of dates for which data should be collected.
            usage_path (str): The base path to the usage data files.
            player_base_path (str): The base path to the player statistics data files.
            defense_base_path (str): The base path to the defensive statistics data files.

        Returns:
            tuple:
                - current_player_dic (dict): A dictionary where each key is a player, and 
                the value is a DataFrame containing their historical merged statistics.
                - current_defense_df (DataFrame): The latest available defensive statistics DataFrame.
    """


    current_player_dic = {}

    for player, team in player_names.items():
        current_player_frames =[]

        for date in date_list:
            # usage_path =build_data_path(usage_path,date=date)
            # usage_data = pd.read_csv(usage_path)

            #merging player and defense dat into one
            merged_data, current_defense_df = his_player_defense_data(player_base_path,defense_base_path,player,date)

            def add_one_stats(merged_data, one_stat_data, player, player_column, columns):
                """Efficiently adds stats for a player to the merged dataset. stats are from usage and everything from tracking data csv"""
                one_stat_data["season"] = date
                player_data = one_stat_data.loc[one_stat_data[player_column] == player, columns]

                if not player_data.empty:
                    # Create a new DataFrame with the selected columns to merge
                    new_columns = pd.DataFrame([player_data.iloc[0].values], columns=columns, index=merged_data.index)
                    merged_data = pd.concat([merged_data, new_columns], axis=1)

                return merged_data

            
            
            
            track_data = tracking_and_usage(stats_path,date)
            keys_list = list(track_data.keys())

            for idx, (track_name, track_df) in enumerate(track_data.items()):
                if track_name == keys_list[idx]:  # Ensures correct mapping
                    columns = list(track_df.columns)
                    if track_name == "usage_path":
                        player_column = columns.pop(1)
                        columns.pop(1)
                    else:
                        player_column = columns.pop(0)  # Extract player identifier column
                        columns.pop(0)
                    merged_data = add_one_stats(merged_data, track_df, player, player_column, columns)

            # #adding season to usage_data
            # usage_data['season'] = date

            # #Getting the player usage percentage for usage data and adding to merge
            # player_usage = usage_data.loc[usage_data['Player'] == player, 'USG%'].values[0]
            # merged_data['USG'] = player_usage

            #adding the current player team pace
            if not current_defense_df.empty:
                team_stat = current_defense_df.loc[current_defense_df['TEAM'] == team, 'PACE'].values[0]
                merged_data["team_pace"] = team_stat

                # adding current player team OffRtg
                team_offrtg = current_defense_df.loc[current_defense_df['TEAM'] == team, 'OffRtg'].values[0]
                merged_data["team_offrtg"] = team_offrtg

                team_poss = current_defense_df.loc[current_defense_df['TEAM'] == team, 'POSS'].values[0]
                merged_data["team_poss"] = team_poss
                
                # Exclude rows where the TEAM column matches the given team
                merged_data = merged_data[merged_data['TEAM'] != team]
            else:
                print("defense data skipping defense merge")
                continue


            # merged_data = merged_data[['season','Date', 'Home/Away_game' ,'Matchup' ,'PTS','MIN_x', 'Team', 'TEAM', 'FGA', 'USG', 'DefRtg', 'PACE','team_pace']]

            # Turn date into seconds
            merged_data['Date_in_Seconds'] = pd.to_datetime(merged_data['Date']).astype('int64') // 10**9
            merged_data = merged_data.sort_values(by="Date_in_Seconds")


            # Turn Home/Away game into 1 and 0
            merged_data['home_away'] = merged_data['Home/Away_game'].apply(lambda x: 1 if x == 'Away' else 0)
            # Dropping duplicates
            merged_data = merged_data.drop_duplicates()
            
            # Append the DataFrame for this date to the player's list
            current_player_frames.append(merged_data)

        # Combine all dates for the current player into one DataFrame
        current_player_dic[player] = pd.concat(current_player_frames, ignore_index=True)
        pd.set_option('display.max_rows', 1000)  # Maximum number of rows to display
        pd.set_option('display.max_columns', None)  # Show all columns
        pd.set_option('display.width', 1000)  # Adjust column width for better readability


    return current_player_dic, current_defense_df



# def his_usage_team(player_names: dict, date_list: list,stats_path:dict,player_base_path,defense_base_path):
#     """
#         Computes historical usage data for a given set of players over a list of dates.

#         This function merges player statistics, usage data, and defensive statistics 
#         to create a dataset containing various metrics such as usage percentage (USG%), 
#         team pace, offensive rating, and possession data.

#         Parameters:
#             player_names (dict): A dictionary mapping player names to their respective teams.
#             date_list (list): A list of dates for which data should be collected.
#             usage_path (str): The base path to the usage data files.
#             player_base_path (str): The base path to the player statistics data files.
#             defense_base_path (str): The base path to the defensive statistics data files.

#         Returns:
#             tuple:
#                 - current_player_dic (dict): A dictionary where each key is a player, and 
#                 the value is a DataFrame containing their historical merged statistics.
#                 - current_defense_df (DataFrame): The latest available defensive statistics DataFrame.
#     """


#     current_player_dic = {}

#     for player, team in player_names.items():
#         current_player_frames =[]

#         for date in date_list:
#             # usage_path =build_data_path(usage_path,date=date)
#             # usage_data = pd.read_csv(usage_path)

#             #merging player and defense dat into one
#             merged_data, current_defense_df = his_player_defense_data(player_base_path,defense_base_path,player,date)

#             def add_one_stats(merged_data, one_stat_data, player, player_column, columns):
#                 """Efficiently adds stats for a player to the merged dataset. stats are from usage and everything from tracking data csv"""
#                 one_stat_data["season"] = date
#                 player_data = one_stat_data.loc[one_stat_data[player_column] == player, columns]

#                 if not player_data.empty:
#                     # Create a new DataFrame with the selected columns to merge
#                     new_columns = pd.DataFrame([player_data.iloc[0].values], columns=columns, index=merged_data.index)
#                     merged_data = pd.concat([merged_data, new_columns], axis=1)

#                 return merged_data

            
            
            
#             track_data = tracking_and_usage(stats_path,date)
#             keys_list = list(track_data.keys())

#             for idx, (track_name, track_df) in enumerate(track_data.items()):
#                 if track_name == keys_list[idx]:  # Ensures correct mapping
#                     columns = list(track_df.columns)
#                     if track_name == "usage_path":
#                         player_column = columns.pop(1)
#                         columns.pop(1)
#                     else:
#                         player_column = columns.pop(0)  # Extract player identifier column
#                         columns.pop(0)
#                     merged_data = add_one_stats(merged_data, track_df, player, player_column, columns)

#             # #adding season to usage_data
#             # usage_data['season'] = date

#             # #Getting the player usage percentage for usage data and adding to merge
#             # player_usage = usage_data.loc[usage_data['Player'] == player, 'USG%'].values[0]
#             # merged_data['USG'] = player_usage

#             #adding the current player team pace
#             team_stat = current_defense_df.loc[current_defense_df['TEAM'] == team, 'PACE'].values[0]
#             merged_data["team_pace"] = team_stat

#             # adding current player team OffRtg
#             team_offrtg = current_defense_df.loc[current_defense_df['TEAM'] == team, 'OffRtg'].values[0]
#             merged_data["team_offrtg"] = team_offrtg

#             team_poss = current_defense_df.loc[current_defense_df['TEAM'] == team, 'POSS'].values[0]
#             merged_data["team_poss"] = team_poss
            
#             # Exclude rows where the TEAM column matches the given team
#             merged_data = merged_data[merged_data['TEAM'] != team]


#             # merged_data = merged_data[['season','Date', 'Home/Away_game' ,'Matchup' ,'PTS','MIN_x', 'Team', 'TEAM', 'FGA', 'USG', 'DefRtg', 'PACE','team_pace']]

#             # Turn date into seconds
#             merged_data['Date_in_Seconds'] = pd.to_datetime(merged_data['Date']).astype('int64') // 10**9
#             merged_data = merged_data.sort_values(by="Date_in_Seconds")


#             # Turn Home/Away game into 1 and 0
#             merged_data['home_away'] = merged_data['Home/Away_game'].apply(lambda x: 1 if x == 'Away' else 0)
#             # Dropping duplicates
#             merged_data = merged_data.drop_duplicates()
            
#             # Append the DataFrame for this date to the player's list
#             current_player_frames.append(merged_data)

#         # Combine all dates for the current player into one DataFrame
#         current_player_dic[player] = pd.concat(current_player_frames, ignore_index=True)


#     return current_player_dic, current_defense_df


if __name__ == "__main__":
    raise ImportError("This script is intended to be imported as a module, not executed directly.")
    # example use case:
    # player = "James Harden"
    # date = "2019-20"
    # player_base_path = "../../historic_player_data/nba_ph_csv/season_{date}/all_quarters/{player}_content.csv"
    # defense_base_path = "../../historic_defense_data/nba_dh_csv/defense_csv_{date}/all_quarter_defense_content.csv"

    # his_player_defense_data(player, date, player_base_path, defense_base_path)
    


