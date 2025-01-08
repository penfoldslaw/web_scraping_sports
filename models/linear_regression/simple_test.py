import pandas as pd
import os
player_path = r'nba_ph_csv/season_2019-20/all_quarters/Jayson Tatum_content.csv'
df_player = pd.read_csv(player_path)
df_defense = pd.read_csv(r'nba_dh_csv\defense_csv_2019-20\all_quarter_defense_content.csv')

print(df_player.head())