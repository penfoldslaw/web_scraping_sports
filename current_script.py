import subprocess

def run_script(script_path):
    process = subprocess.Popen(["python3", script_path])
    return process

# Run the scraper scripts in parallel
scraper_scripts = [
    "current_player_data/current_player_scraper_processor.py",
    "current_defense_data/current_defense_scraper_processor.py",
    "current_usage_data/current_usage_scraper_processor.py",
    "schedule/schedule_scraper_processor.py"
]

processes = [run_script(script) for script in scraper_scripts]

# Wait for all processes to finish
for process in processes:
    process.wait()

print("Starting parser scripts")

# Run the parser scripts in parallel
parser_scripts = [
    "current_player_data/current_player_parser_processor.py",
    "current_defense_data/current_defense_parser_processor.py",
    "current_usage_data/current_usage_parser_processor.py",
    "schedule/schedule_parser_processor.py"
]

processes = [run_script(script) for script in parser_scripts]

# Wait for all processes to finish
for process in processes:
    process.wait()

print("All scripts done")
