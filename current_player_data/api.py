from nba_api.stats.static import players

def get_player_id(player_name):
    all_players = players.get_players()
    for player in all_players:
        if player_name.lower() in player['full_name'].lower():
            return player['id'], player['full_name']
    return None, None

# Example Usage
player_name = "Dalton Knecht"
player_id, full_name = get_player_id(player_name)
print(f"Player ID for {full_name}: {player_id}")
