import pandas as pd
import os
import numpy as np
from IPython.display import display
import pprint
from datetime import datetime




pd.set_option('display.max_rows', 1000)  # Maximum number of rows to display
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.width', 1000)  # Adjust column width for better readability




import os
import pandas as pd
import sys

log_file_path = "streamlit_consumption\streamlit_log.log"


# Open the log file in append mode ("a")
sys.stdout = open(log_file_path, "w")
sys.stderr = open(log_file_path, "w")

# input_dir = os.makedirs("D:\streamlit_ingest", exist_ok=True)
main_folder = "D:/prediction_output"
nested_df_dict = {}


def get_subfolder_name(main_folder, nested_df_dict):
    for root, dirs, files in os.walk(main_folder):
        for file in files:
            if file.endswith(".csv"):
                subfolder_name = os.path.basename(root)  # Get subfolder name
                file_path = os.path.join(root, file)
                df_name = os.path.splitext(file)[0]      # Get filename without .csv

                # Read CSV
                df = pd.read_csv(file_path)

                # Create subfolder dictionary if it doesn't exist
                if subfolder_name not in nested_df_dict:
                    nested_df_dict[subfolder_name] = {}

                # Store the DataFrame inside its subfolder
                nested_df_dict[subfolder_name][df_name] = df
    return nested_df_dict

nested_df_dict = get_subfolder_name(main_folder, nested_df_dict)


# pprint.pprint(nested_df_dict)
print(nested_df_dict.keys())
# print(nested_df_dict)
# print(nested_df_dict["PTS_outputs"].keys())
# df = nested_df_dict["PTS_outputs"]["PTS_output_2025-04-06"]
# display(df)

# Access the inner dictionary

linear_prediction_dict_list = ["PTS_outputs", "AST_outputs", "REB_outputs", "3PM_outputs"]

linear_prediction_df_list = []
for i in linear_prediction_dict_list:
    inner_dict = nested_df_dict[i]

    # Get the last key (in insertion order, which is preserved in Python 3.7+)
    last_key = list(inner_dict.keys())[-1]

    # Get the corresponding DataFrame
    last_df = inner_dict[last_key]

    # Optional: show the key and DataFrame shape
    print(f"Last file: {last_key}, shape: {last_df.shape}")

    linear_prediction_df_list.append(last_df)



import ast

def calculate_score_percentages(row,target):
    # Safely parse the recentgames_PTS list from string to list
    try:
        recent_games = ast.literal_eval(row[f'recentgames_{target}']) if isinstance(row[f'recentgames_{target}'], str) else row[f'recentgames_{target}']
    except Exception:
        return pd.Series([0, 0, 0], index=['First_Pct', 'Second_Pct', 'Third_Pct'])

    if not recent_games or len(recent_games) == 0:
        return pd.Series([0, 0, 0], index=['First_Pct', 'Second_Pct', 'Third_Pct'])

    total_games = len(recent_games)
    
    # Ensure thresholds are integers
    first = int(row[f'{target}_First'])
    second = int(row[f'{target}_Second'])
    third = int(row[f'{target}_Third'])


    

    # Count scores >= threshold
    first_count = sum(int(score) >= first for score in recent_games)
    second_count = sum(int(score) >= second for score in recent_games)
    third_count = sum(int(score) >= third for score in recent_games)

    # Convert to percentages
    first_pct = round((first_count / total_games) * 100, 2)
    second_pct = round((second_count / total_games) * 100, 2)
    third_pct = round((third_count / total_games) * 100, 2)

    if first_pct == 100 :
        first_pct = 95

    if second_pct == 100:
        second_pct = 95
        
    if third_pct == 100:
        third_pct = 95    


    return pd.Series([first_pct, second_pct, third_pct], index=['First_Pct', 'Second_Pct', 'Third_Pct'])





list_of_targets = ["PTS", "AST", "REB", "3PM"]

target_number = [0,1,2,3]

final_processed_dfs = []


for i in target_number:
    
    target = list_of_targets[i]

    df = linear_prediction_df_list[i]

    df[['First', 'Second', 'Third']] = df[target].str.split(' - ', expand=True).astype(int)

    df = df.rename(columns=lambda x: f"{target}_{x}" if x in ['First', 'Second', 'Third'] else x)




    display(df.head(10))

    team_totals = df.groupby('team', sort=False)[[f'{target}_First', f'{target}_Second', f'{target}_Third']].sum()
    team_totals['Total'] = team_totals.sum(axis=1)
    team_totals_reset = team_totals.reset_index()  # keeps 'team' as column, keeps order


    print(team_totals)


    # Reset index to get 'team' as a column
    team_totals_reset = team_totals.reset_index()

    # Sort alphabetically (or however you want)
    # team_totals_reset = team_totals_reset.sort_values(by='team').reset_index(drop=True)

    # Create matchups and determine winner based on 'First'
    matchups = []
    for i in range(0, len(team_totals_reset) - 1, 2):
        team1 = team_totals_reset.iloc[i]
        team2 = team_totals_reset.iloc[i + 1]

        winner = team1['team'] if team1[f'{target}_First'] > team2[f'{target}_First'] else team2['team']
        matchup = f"{team1['team']} vs {team2['team']}"

        matchups.append({
            'Matchup': matchup,
            'Winner': winner,
            'Team1_First': team1[f'{target}_First'],
            'Team2_First': team2[f'{target}_First']
        })

    # Convert to DataFrame
    matchups_df = pd.DataFrame(matchups)

    # Display results
    today_date = datetime.today().strftime('%Y-%m-%d')

    matchup_dir = f"D:/streamlit_ingest/matchup_{target}"

    os.makedirs(matchup_dir, exist_ok=True)

    matchup_file_path = os.path.join(matchup_dir, f"matchup_{today_date}.csv")

    matchups_df.to_csv(matchup_file_path, index=False)



    # display(matchups_df)


    






    # Apply to your dataframe
    df[['First_Pct', 'Second_Pct', 'Third_Pct']] = df.apply(lambda row: calculate_score_percentages(row,target), axis=1)

    first_second_third = df[['Player', 'team' ,f'{target}_First', f'{target}_Second', f'{target}_Third','First_Pct', 'Second_Pct', 'Third_Pct', f'recentgames_{target}']]
    first_second_third[f'recentgames_{target}'] = first_second_third[f'recentgames_{target}'].astype(str).str.replace(r'[\[\]]', '', regex=True)



    first_second_third_dir = f"D:/streamlit_ingest/first_second_third_{target}"

    os.makedirs(first_second_third_dir, exist_ok=True)

    first_second_third_file_path = os.path.join(first_second_third_dir, f"first_second_third_{today_date}.csv")

    first_second_third.to_csv(first_second_third_file_path, index=False)

    display(first_second_third.head(10))
    

    df = df.rename(columns={
    'First_Pct': f'{target}_First_Pct',
    'Second_Pct': f'{target}_Second_Pct',
    'Third_Pct': f'{target}_Third_Pct'})
    df[f'recentgames_{target}'] = df[f'recentgames_{target}'].astype(str).str.replace(r'[\[\]]', '', regex=True)


    # Save the processed df to combine later
    # ['Player', 'team', '3PM', 'cv-1_3PM', 'recentgames_3PM', 'rmse_3PM', '3PM_First', '3PM_Second', '3PM_Third', '3PM_First_Pct', '3PM_Second_Pct', '3PM_Third_Pct']
    final_processed_dfs.append(df)


    # Preview
    # display(df[['Player', 'team' ,f'{target}_First', f'{target}_Second', f'{target}_Third','First_Pct', 'Second_Pct', 'Third_Pct']])


from functools import reduce

# Merge on Player and team
final_merged_df = reduce(
    lambda left, right: pd.merge(left, right, on=['Player', 'team'], how='outer'),
    final_processed_dfs
)


final_merged_df_dir = f"D:/streamlit_ingest/final_merged_df"

os.makedirs(final_merged_df_dir, exist_ok=True)

final_merged_df_file_path = os.path.join(final_merged_df_dir, f"final_merged_df_{today_date}.csv")

final_merged_df.to_csv(final_merged_df_file_path, index=False)

# Final combined dataframe
print(final_merged_df)