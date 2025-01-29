#!/bin/bash

# Run historic player scraper and parser
python web_scraping_sports/historic_player_data/his_player_scraper_processor.py &
python web_scraping_sports/historic_defense_data/his_defense_scraper_processor.py &
python web_scraping_sports/his_usage_data/his_usage_scraper_processor.py


# Run historic and current parser
python web_scraping_sports/historic_player_data/his_player_parser_processor.py &
python web_scraping_sports/historic_defense_data/his_defense_parser_processor.py &
python web_scraping_sports/his_usage_data/his_usage_parser_processor.py


# Ensure the script waits for all background processes to complete
wait

