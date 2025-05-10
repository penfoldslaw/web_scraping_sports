import configparser
import ast  # To safely convert the string back to a Python list

def fetch_matchup_list(file_path='matchup.cfg'):
    """
    Fetches the matchup list from a configuration file.

    Parameters:
        file_path (str): Path to the configuration file.

    Returns:
        list: A Python list containing matchup items.
    """
    # Initialize the ConfigParser
    config = configparser.ConfigParser()

    # Read the configuration file
    config.read(file_path)

    # Fetch and convert the matchup list
    matchup = ast.literal_eval(config['Teams']['matchup'])

    return matchup

if __name__ == "__main__":
    # Example file path
    file_path = 'matchup.cfg'  # Ensure this file exists and has the correct format

    # Fetch the matchup list
    matchup = fetch_matchup_list(file_path)

    # Print the fetched matchup list
    print(matchup)

# # Example usage
# file_path = 'config.ini'
# matchup = fetch_matchup_list(file_path)
# print(matchup)