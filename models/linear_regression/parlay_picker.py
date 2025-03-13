import random
import pandas as pd
from IPython.display import display


import random
import pandas as pd



# Convert to DataFrame

def create_parlays(player_data, num_groups, players_per_group):
    # List of all possible player data points (player, stat, and range)
    all_players = []

    for idx, row in player_data.iterrows():
        player_name = row['Player']
        stats = ['REB', 'AST', 'PTS', '3PM', 'PTS+REB']
        for stat in stats:
            stat_range = row[stat]
            confidence = row[f'confidence_level_{stat}']
            safebet = row[f'middlebet_{stat}']

            all_players.append((player_name, stat, stat_range, confidence, safebet))
                

    # Randomize the order of the player data
    random.shuffle(all_players)

    # Create the parlays based on num_groups and players_per_group
    parlays = []
    for _ in range(num_groups):
        parlay = []
        for _ in range(players_per_group):
            if all_players:
                parlay.append(all_players.pop())
        parlays.append(parlay)

    # Create a list of DataFrames for each parlay
    parlays_df = []
    group_confidence_scores = []
    for idx, parlay in enumerate(parlays, 1):
        parlay_name = f"Parlay {idx}"
        parlay_data = {
            'Player': [],
            'Stat': [],
            'Stat Range': [],
            'Confidence': [],
            'middlebet': []
        }
        total_confidence = 0  # Variable to calculate the total confidence score
        for player, stat, stat_range, confidence, safebet in parlay:
            parlay_data['Player'].append(player)
            parlay_data['Stat'].append(stat)
            parlay_data['Stat Range'].append(stat_range)
            parlay_data['Confidence'].append(confidence)
            parlay_data['middlebet'].append(safebet)
            total_confidence += confidence
        
        # Calculate the average confidence score for this parlay
        avg_confidence = total_confidence / len(parlay)
        group_confidence_scores.append((parlay_name, avg_confidence))
        
        # Convert to DataFrame
        df = pd.DataFrame(parlay_data)
        
        # df["middlebet"] = df["middlebet"].astype(int)


        # Apply middlebet correction **only to the DataFrame, not the entire list**
        # df.loc[(df["Stat"] == "PTS+REB") & (df["middlebet"] == 0), "middlebet"] = None

        parlays_df.append(df)



    
    return parlays_df, group_confidence_scores


if __name__ == "__main__":
    raise ImportError("This script is intended to be imported as a module, not executed directly.")


# # Example usage
# num_groups = 7  # Number of parlays you want to generate
# players_per_group = 5  # Number of players in each parlay

# parlays_df, group_confidence_scores = create_parlays(player_data, num_groups, players_per_group)


# # Display the confidence scores for each group
# print("Confidence scores for each group:")
# for group, score in group_confidence_scores:
#     print(f"{group}: {score:.2f}")


# # Display the DataFrames for each parlay and their confidence scores
# for (parlay_name, score), parlay_df in zip(group_confidence_scores, parlays_df):
#     print("\n")
#     print(f"{parlay_name}: total confidence score: {score:.2f}")
#     display(parlay_df)
#     print("\n")






