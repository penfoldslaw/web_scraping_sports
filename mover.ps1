# $source ="D:\nba_player_csv_current"
# $destination = "D:\nba_player_csv_historic\season_2024-25"

function Copy-Folder {
    param (
        [string]$Source,
        [string]$Destination
    )

    # Check if destination exists
    if (Test-Path $Destination) {
        # Remove existing destination folder
        Remove-Item -Path $Destination -Recurse -Force
    }

    # Copy the source folder to destination
    Copy-Item -Path $Source -Destination $Destination -Recurse -Force
}

# Example Usage:
Copy-Folder -Source "D:\nba_player_csv_current\season_2024-25" -Destination "D:\nba_player_csv_historic\season_2024-25"

Copy-Folder -Source "D:\nba_usage_csv_current\usage_csv_2024-25" -Destination "D:\nba_usage_csv_historic\usage_csv_2024-25"

Copy-Folder -Source "D:\nba_defense_csv_current\defense_csv_2024-25" -Destination "D:\nba_defense_history_csv\defense_csv_2024-25"
