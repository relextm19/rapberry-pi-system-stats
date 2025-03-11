cd /home/relextm19/stats_page/stats_page/backend/

source venv/bin/activate

# Start the log_stats.py program in the background
python3 log_stats.py &

# Start the get_stats.py program in the background
gunicorn --chdir /home/relextm19/stats_page/stats_page/backend -b 127.0.0.1:2137 wsgi:app &

# Navigate to the frontend directory and serve the production build
cd /home/relextm19/stats_page/stats_page/frontend/dist
serve -s .