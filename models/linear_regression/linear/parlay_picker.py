import random
import pandas as pd
from IPython.display import display
from collections import defaultdict

# def create_parlays(player_data, num_groups, players_per_group, min_confidence=90, threepm_confidence= 40):
#     # List of all possible player data points (player, stat, and range)
#     all_players = []

#     for idx, row in player_data.iterrows():
#         player_name = row['Player']
#         team = row['team']
#         stats = ['REB', 'AST', 'PTS', '3PM']
#         for stat in stats:
#             stat_range = row[stat]
#             confidence = row[f'confidence_level_{stat}']
#             safebet = row[f'recentgames_{stat}']

#             # Only add players with confidence level at or above the minimum
#             if confidence >= min_confidence or confidence >= threepm_confidence:
#                 all_players.append((player_name, team, stat, stat_range, confidence, safebet))
    
#     # Group players by team
#     team_groups = defaultdict(list)
#     for player_info in all_players:
#         player_name, team, stat, stat_range, confidence, safebet = player_info
#         team_groups[team].append(player_info)
    
#     # Sort players within each team by confidence level
#     for team in team_groups:
#         team_groups[team].sort(key=lambda x: x[4], reverse=True)  # Sort by confidence (index 4)
    
#     # Create a set to track used player-stat combinations
#     used_player_stats = set()
    
#     # Create the parlays based on num_groups and players_per_group
#     parlays = []
#     available_teams = list(team_groups.keys())
    
#     for _ in range(num_groups):
#         if not available_teams:
#             break  # Stop if no teams left
        
#         # Pick a team with available players
#         team = None
#         for t in available_teams[:]:
#             # Get players from this team who haven't been used yet
#             available_players = [p for p in team_groups[t] 
#                                if (p[0], p[2]) not in used_player_stats]  # (player_name, stat)
            
#             if len(available_players) >= players_per_group:
#                 team = t
#                 break
#             elif not available_players:
#                 # Remove teams with no available players
#                 available_teams.remove(t)
        
#         if not team:
#             break  # No team has enough players left
        
#         # Create a parlay with players from this team
#         parlay = []
#         for player_info in team_groups[team][:]:
#             player_name, team, stat, stat_range, confidence, safebet = player_info
#             player_stat_key = (player_name, stat)
            
#             # Skip if this player-stat combination has already been used
#             if player_stat_key in used_player_stats:
#                 continue
            
#             # Add to current parlay
#             parlay.append(player_info)
#             used_player_stats.add(player_stat_key)
            
#             # Stop when we have enough players for this parlay
#             if len(parlay) >= players_per_group:
#                 break
        
#         # Only add non-empty parlays
#         if len(parlay) == players_per_group:
#             parlays.append(parlay)

#     # Create a list of DataFrames for each parlay
#     parlays_df = []
#     group_confidence_scores = []
#     for idx, parlay in enumerate(parlays, 1):
#         parlay_name = f"Parlay {idx}"
#         parlay_data = {
#             'Player': [],
#             'team': [],
#             'Stat': [],
#             'Stat Range': [],
#             'Confidence': [],
#             'recentgames': []
#         }
#         total_confidence = 0
#         for player, team, stat, stat_range, confidence, safebet in parlay:
#             parlay_data['Player'].append(player)
#             parlay_data['team'].append(team)
#             parlay_data['Stat'].append(stat)
#             parlay_data['Stat Range'].append(stat_range)
#             parlay_data['Confidence'].append(confidence)
#             parlay_data['recentgames'].append(safebet)
#             total_confidence += confidence
        
#         # Calculate the average confidence score for this parlay
#         avg_confidence = total_confidence / len(parlay) if parlay else 0
#         group_confidence_scores.append((parlay_name, avg_confidence))
        
#         # Convert to DataFrame
#         df = pd.DataFrame(parlay_data)
#         parlays_df.append(df)
    
#     return parlays_df, group_confidence_scores


# import random
# import pandas as pd
# import numpy as np

# def weighted_random_choice(choices, weights, k):
#     return random.choices(choices, weights=weights, k=k)

# def create_parlays_high(player_data, num_groups, players_per_group):
#     # List of all possible player data points (player, stat, and range)
#     all_players = []
#     confidence_levels = []

#     for idx, row in player_data.iterrows():
#         player_name = row['Player']
#         stats = ['REB', 'AST', 'PTS', '3PM']
#         for stat in stats:
#             stat_range = row[stat]
#             confidence = row[f'confidence_level_{stat}']
#             safebet = row[f'recentgames_{stat}']

#             all_players.append((player_name, stat, stat_range, confidence, safebet))
#             confidence_levels.append(confidence)  # Store confidence levels

#     parlays = []
#     group_confidence_scores = []
    
#     for _ in range(num_groups):
#         if not all_players:
#             break  # Stop if we run out of players

#         # Weighted selection of players
#         selected_players = weighted_random_choice(all_players, confidence_levels, players_per_group)

#         # Remove selected players from the pool
#         for player in selected_players:
#             index = all_players.index(player)
#             del all_players[index]
#             del confidence_levels[index]  # Keep lists synchronized

#         # Organize selected players into DataFrame
#         parlay_data = {
#             'Player': [p[0] for p in selected_players],
#             'Stat': [p[1] for p in selected_players],
#             'Stat Range': [p[2] for p in selected_players],
#             'Confidence': [p[3] for p in selected_players],
#             'recentgames': [p[4] for p in selected_players],
#         }
#         df = pd.DataFrame(parlay_data)

#         # Calculate the group's average confidence
#         avg_confidence = np.mean(parlay_data['Confidence'])
#         group_confidence_scores.append((f"Parlay {len(parlays)+1}", avg_confidence))

#         parlays.append(df)

#     return parlays, group_confidence_scores


# if __name__ == "__main__":
#     raise ImportError("This script is intended to be imported as a module, not executed directly.")


# # player_data = df_merged
# # # For very high confidence parlays
# # parlays_high, scores_high = create_parlays(player_data, num_groups=5, players_per_group=6, min_confidence=90)

# # # For moderate confidence parlays
# # parlays_medium, scores_medium = create_parlays(player_data, num_groups=5, players_per_group=3, min_confidence=6)



# # print("Confidence scores for each group:")
# # for group, score in scores_high:
# #     print(f"{group}: {score:.2f}")


# # # Display the DataFrames for each parlay and their confidence scores
# # for (parlay_name, score), parlay_df in zip(scores_high, parlays_high):
# #     print("\n")
# #     print(f"{parlay_name}: total confidence score: {score:.2f}")
# #     display(parlay_df)
# #     print("\n")




# # # Define the number of parlays and players per parlay
# # num_groups = 2  # Example: Create 3 parlays
# # players_per_group = 7 # Example: Each parlay consists of 4 players

# # # Call the function
# # parlays, confidence_scores = create_parlays_high(df_merged, num_groups, players_per_group)

# # # Display results
# # for i, (df, (parlay_name, avg_conf)) in enumerate(zip(parlays, confidence_scores), 1):
# #     print(f"\n{parlay_name} (Avg Confidence: {avg_conf:.2f})")
# #     display(df)




import random
import pandas as pd
from IPython.display import display
from collections import defaultdict

def create_parlays(player_data, num_groups, players_per_group, min_confidence=90, threepm_confidence=40):
    # List of all possible player data points (player, stat, and range)
    all_players = []

    for idx, row in player_data.iterrows():
        player_name = row['Player']
        team = row['team']
        stats = ['REB', 'AST', 'PTS', '3PM']
        for stat in stats:
            stat_range = row[stat]
            confidence = row[f'confidence_level_{stat}']
            safebet = row[f'recentgames_{stat}']

            # Apply different confidence thresholds based on stat type
            if stat == '3PM':
                # Add 3PM stats with confidence level at or above threepm_confidence
                if confidence >= threepm_confidence:
                    all_players.append((player_name, team, stat, stat_range, confidence, safebet))
            else:
                # For other stats, use the regular minimum confidence
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
            'recentgames': []
        }
        total_confidence = 0
        for player, team, stat, stat_range, confidence, safebet in parlay:
            parlay_data['Player'].append(player)
            parlay_data['team'].append(team)
            parlay_data['Stat'].append(stat)
            parlay_data['Stat Range'].append(stat_range)
            parlay_data['Confidence'].append(confidence)
            parlay_data['recentgames'].append(safebet)
            total_confidence += confidence
        
        # Calculate the average confidence score for this parlay
        avg_confidence = total_confidence / len(parlay) if parlay else 0
        group_confidence_scores.append((parlay_name, avg_confidence))
        
        # Convert to DataFrame
        df = pd.DataFrame(parlay_data)
        parlays_df.append(df)
    
    return parlays_df, group_confidence_scores


def create_parlays_high(player_data, num_groups, players_per_group, min_confidence=90, threepm_confidence=40):
    """
    Create optimal betting parlays with improved selection algorithm to prevent duplicate player-stat combinations
    in the same group while maximizing overall confidence.
    
    Args:
        player_data (DataFrame): DataFrame containing player stats and confidence levels
        num_groups (int): Number of parlay groups to create
        players_per_group (int): Number of players/stats per parlay group
        min_confidence (float): Minimum confidence threshold for non-3PM stats (default: 90)
        threepm_confidence (float): Minimum confidence threshold for 3PM stats (default: 40)
        
    Returns:
        tuple: (list of parlay DataFrames, list of tuples with parlay names and confidence scores)
    """
    # List of all possible player data points (player, stat, and range)
    all_players = []
    confidence_levels = []

    # Process player data and filter by confidence thresholds
    for idx, row in player_data.iterrows():
        player_name = row['Player']
        team = row['team']
        stats = ['REB', 'AST', 'PTS', '3PM']
        
        for stat in stats:
            if stat not in row or f'confidence_level_{stat}' not in row:
                continue
                
            stat_range = row[stat]
            confidence = row[f'confidence_level_{stat}']
            safebet = row.get(f'recentgames_{stat}', 0)  # Use get with default to avoid KeyError
            
            # Apply different confidence thresholds based on stat type
            threshold = threepm_confidence if stat == '3PM' else min_confidence
            
            if confidence >= threshold:
                all_players.append((player_name, team, stat, stat_range, confidence, safebet))
                confidence_levels.append(confidence)
    
    # Sort by confidence (highest first) to prioritize high-confidence picks
    sorted_data = sorted(zip(all_players, confidence_levels), key=lambda x: x[1], reverse=True)
    all_players = [item[0] for item in sorted_data]
    confidence_levels = [item[1] for item in sorted_data]
    
    parlays = []
    group_confidence_scores = []
    
    # Create the specified number of parlay groups
    for group_idx in range(num_groups):
        if len(all_players) < players_per_group:
            break  # Stop if we don't have enough players for a full group
        
        selected_players = []
        selected_indices = []
        
        # Track players already in this group to avoid duplicates
        players_in_group = set()
        
        # Try to select players_per_group players for this parlay
        remaining_attempts = len(all_players)  # Limit attempts to avoid infinite loop
        
        while len(selected_players) < players_per_group and remaining_attempts > 0:
            remaining_attempts -= 1
            
            # Get candidates that aren't already in the group (weighted by confidence)
            valid_indices = []
            valid_weights = []
            
            for i, player_data in enumerate(all_players):
                if i not in selected_indices:
                    player_name, _, stat, _, _, _ = player_data
                    player_stat_key = (player_name, stat)
                    
                    # Skip if this player-stat combo is already in the group
                    if player_stat_key in players_in_group:
                        continue
                        
                    valid_indices.append(i)
                    valid_weights.append(confidence_levels[i])
            
            # If no valid candidates remain, break the loop
            if not valid_indices:
                break
                
            # Select a player based on weighted confidence
            try:
                selected_idx = random.choices(valid_indices, weights=valid_weights, k=1)[0]
                
                player_name, team, stat, stat_range, confidence, safebet = all_players[selected_idx]
                player_stat_key = (player_name, stat)
                
                # Add to selected players and mark as used
                selected_players.append(all_players[selected_idx])
                selected_indices.append(selected_idx)
                players_in_group.add(player_stat_key)
                
            except IndexError:
                # No more valid players to select
                break
        
        # If we couldn't get enough players, skip this group
        if len(selected_players) < players_per_group:
            continue
            
        # Remove selected players from the pool (in reverse index order to avoid index shifting)
        for idx in sorted(selected_indices, reverse=True):
            del all_players[idx]
            del confidence_levels[idx]

        # Organize selected players into DataFrame
        parlay_data = {
            'Player': [p[0] for p in selected_players],
            'Team': [p[1] for p in selected_players],
            'Stat': [p[2] for p in selected_players],
            'Stat Range': [p[3] for p in selected_players],
            'Confidence': [p[4] for p in selected_players],
            'Recent Games': [p[5] for p in selected_players],
        }
        df = pd.DataFrame(parlay_data)

        # Calculate the group's average confidence
        avg_confidence = sum(parlay_data['Confidence']) / len(parlay_data['Confidence'])
        group_confidence_scores.append((f"Parlay {group_idx+1}", round(avg_confidence, 2)))

        parlays.append(df)

    # Sort parlays by confidence score (highest first)
    sorted_results = sorted(zip(parlays, group_confidence_scores), key=lambda x: x[1][1], reverse=True)
    
    # Rename parlays based on new ordering
    sorted_parlays = []
    sorted_scores = []
    
    for i, (parlay, (_, score)) in enumerate(sorted_results):
        sorted_parlays.append(parlay)
        sorted_scores.append((f"Parlay {i+1}", score))

    return sorted_parlays, sorted_scores


if __name__ == "__main__":
    raise ImportError("This script is intended to be imported as a module, not executed directly.")

