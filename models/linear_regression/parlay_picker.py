import random
import pandas as pd
from IPython.display import display
from collections import defaultdict

def create_parlays(player_data, num_groups, players_per_group, min_confidence=90):
    # List of all possible player data points (player, stat, and range)
    all_players = []

    for idx, row in player_data.iterrows():
        player_name = row['Player']
        team = row['team']
        stats = ['REB', 'AST', 'PTS', '3PM']
        for stat in stats:
            stat_range = row[stat]
            confidence = row[f'confidence_level_{stat}']
            safebet = row[f'middlebet_{stat}']

            # Only add players with confidence level at or above the minimum
            if confidence >= min_confidence:
                all_players.append((player_name, team, stat, stat_range, confidence, safebet))
    
    # Group players by team
    team_groups = defaultdict(list)
    for player_info in all_players:
        player_name, team, stat, stat_range, confidence, safebet = player_info
        team_groups[team].append(player_info)
    
    # Sort players within each team by confidence level
    for team in team_groups:
        team_groups[team].sort(key=lambda x: x[4], reverse=True)  # Sort by confidence (index 4)
    
    # Create a set to track used player-stat combinations
    used_player_stats = set()
    
    # Create the parlays based on num_groups and players_per_group
    parlays = []
    available_teams = list(team_groups.keys())
    
    for _ in range(num_groups):
        if not available_teams:
            break  # Stop if no teams left
        
        # Pick a team with available players
        team = None
        for t in available_teams[:]:
            # Get players from this team who haven't been used yet
            available_players = [p for p in team_groups[t] 
                               if (p[0], p[2]) not in used_player_stats]  # (player_name, stat)
            
            if len(available_players) >= players_per_group:
                team = t
                break
            elif not available_players:
                # Remove teams with no available players
                available_teams.remove(t)
        
        if not team:
            break  # No team has enough players left
        
        # Create a parlay with players from this team
        parlay = []
        for player_info in team_groups[team][:]:
            player_name, team, stat, stat_range, confidence, safebet = player_info
            player_stat_key = (player_name, stat)
            
            # Skip if this player-stat combination has already been used
            if player_stat_key in used_player_stats:
                continue
            
            # Add to current parlay
            parlay.append(player_info)
            used_player_stats.add(player_stat_key)
            
            # Stop when we have enough players for this parlay
            if len(parlay) >= players_per_group:
                break
        
        # Only add non-empty parlays
        if len(parlay) == players_per_group:
            parlays.append(parlay)

    # Create a list of DataFrames for each parlay
    parlays_df = []
    group_confidence_scores = []
    for idx, parlay in enumerate(parlays, 1):
        parlay_name = f"Parlay {idx}"
        parlay_data = {
            'Player': [],
            'team': [],
            'Stat': [],
            'Stat Range': [],
            'Confidence': [],
            'middlebet': []
        }
        total_confidence = 0
        for player, team, stat, stat_range, confidence, safebet in parlay:
            parlay_data['Player'].append(player)
            parlay_data['team'].append(team)
            parlay_data['Stat'].append(stat)
            parlay_data['Stat Range'].append(stat_range)
            parlay_data['Confidence'].append(confidence)
            parlay_data['middlebet'].append(safebet)
            total_confidence += confidence
        
        # Calculate the average confidence score for this parlay
        avg_confidence = total_confidence / len(parlay) if parlay else 0
        group_confidence_scores.append((parlay_name, avg_confidence))
        
        # Convert to DataFrame
        df = pd.DataFrame(parlay_data)
        parlays_df.append(df)
    
    return parlays_df, group_confidence_scores


import random
import pandas as pd
import numpy as np

def weighted_random_choice(choices, weights, k):
    return random.choices(choices, weights=weights, k=k)

def create_parlays_high(player_data, num_groups, players_per_group):
    # List of all possible player data points (player, stat, and range)
    all_players = []
    confidence_levels = []

    for idx, row in player_data.iterrows():
        player_name = row['Player']
        stats = ['REB', 'AST', 'PTS', '3PM']
        for stat in stats:
            stat_range = row[stat]
            confidence = row[f'confidence_level_{stat}']
            safebet = row[f'middlebet_{stat}']

            all_players.append((player_name, stat, stat_range, confidence, safebet))
            confidence_levels.append(confidence)  # Store confidence levels

    parlays = []
    group_confidence_scores = []
    
    for _ in range(num_groups):
        if not all_players:
            break  # Stop if we run out of players

        # Weighted selection of players
        selected_players = weighted_random_choice(all_players, confidence_levels, players_per_group)

        # Remove selected players from the pool
        for player in selected_players:
            index = all_players.index(player)
            del all_players[index]
            del confidence_levels[index]  # Keep lists synchronized

        # Organize selected players into DataFrame
        parlay_data = {
            'Player': [p[0] for p in selected_players],
            'Stat': [p[1] for p in selected_players],
            'Stat Range': [p[2] for p in selected_players],
            'Confidence': [p[3] for p in selected_players],
            'middlebet': [p[4] for p in selected_players],
        }
        df = pd.DataFrame(parlay_data)

        # Calculate the group's average confidence
        avg_confidence = np.mean(parlay_data['Confidence'])
        group_confidence_scores.append((f"Parlay {len(parlays)+1}", avg_confidence))

        parlays.append(df)

    return parlays, group_confidence_scores


if __name__ == "__main__":
    raise ImportError("This script is intended to be imported as a module, not executed directly.")


# player_data = df_merged
# # For very high confidence parlays
# parlays_high, scores_high = create_parlays(player_data, num_groups=5, players_per_group=6, min_confidence=90)

# # For moderate confidence parlays
# parlays_medium, scores_medium = create_parlays(player_data, num_groups=5, players_per_group=3, min_confidence=6)



# print("Confidence scores for each group:")
# for group, score in scores_high:
#     print(f"{group}: {score:.2f}")


# # Display the DataFrames for each parlay and their confidence scores
# for (parlay_name, score), parlay_df in zip(scores_high, parlays_high):
#     print("\n")
#     print(f"{parlay_name}: total confidence score: {score:.2f}")
#     display(parlay_df)
#     print("\n")




# # Define the number of parlays and players per parlay
# num_groups = 2  # Example: Create 3 parlays
# players_per_group = 7 # Example: Each parlay consists of 4 players

# # Call the function
# parlays, confidence_scores = create_parlays_high(df_merged, num_groups, players_per_group)

# # Display results
# for i, (df, (parlay_name, avg_conf)) in enumerate(zip(parlays, confidence_scores), 1):
#     print(f"\n{parlay_name} (Avg Confidence: {avg_conf:.2f})")
#     display(df)






