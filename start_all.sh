cd backend/

source venv/bin/activate

# Start the log_stats.py program in the background
python3 log_stats.py &

# Start the get_stats.py program in the background
gunicorn -b 127.0.0.1:5000 wsgi:app &

# Navigate to the frontend directory and serve the production build
cd ../frontend/dist
serve -s .

