# Run current player scraper and parser
set -e
echo "starting scraper script"
python3 /mnt/c/Users/mandy/Documents/Github/web_scraping_sports/current_player_data/current_player_scraper_processor.py &
python3 /mnt/c/Users/mandy/Documents/Github/web_scraping_sports/current_defense_data/current_defense_scraper_processor.py &
python3 /mnt/c/Users/mandy/Documents/Github/web_scraping_sports/current_usage_data/current_usage_scraper_processor.py &
python3 /mnt/c/Users/mandy/Documents/Github/web_scraping_sports/schedule/schedule_scraper_processor.py&

wait

echo "starting parser script"
# Run current defense scraper and parser
pwd
python3 /mnt/c/Users/mandy/Documents/Github/web_scraping_sports/current_player_data/current_player_parser_processor.py &
python3 /mnt/c/Users/mandy/Documents/Github/web_scraping_sports/current_defense_data/current_defense_parser_processor.py &
python3 /mnt/c/Users/mandy/Documents/Github/web_scraping_sports/current_usage_data/current_usage_parser_processor.py &
python3 /mnt/c/Users/mandy/Documents/Github/web_scraping_sports/schedule/schedule_parser_processor.py&

wait

echo "all script done"