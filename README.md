# Raspberry Pi Stats Web App

This project allows you to log and display system statistics from your Raspberry Pi through a web interface. The application collects system data, stores it, and serves it on a web page. It consists of a backend to collect and log system stats and a frontend to display these stats in a user-friendly interface.

## Features

- Collects and logs system statistics like CPU usage, memory usage, uptime, and network stats.
- Displays collected data on a web interface.
- Built with Python (Flask) for the backend and Vue.js for the frontend.
- Flask serves the data, while Vue.js presents it in a clean UI.
- Data is stored in a CSV file and served using a Python server (Flask and Gunicorn).

## Prerequisites

Before you begin, ensure you have the following installed:

- package menaget such as **npm** for the frontend
- **Python** 3.x and **pip** for the backend
- **Vue.js** (via npm) for the frontend

## Installation

Follow the steps below to set up the project on your Raspberry Pi.

### 1. Clone the repository

Clone the repository to your local machine:

```bash
git clone https://github.com/relextm19/rapberry-pi-system-stats
```

### 2. Set up the backend

1. Navigate to the `backend` directory:

   ```bash
   cd backend
   ```

2. Create a Python virtual environment:

   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:

   ```bash
   source venv/bin/activate
   ```

4. Install the required Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### 3. Set up the frontend

1. Navigate to the `frontend` directory:

   ```bash
   cd frontend
   ```

2. Install the required frontend dependencies using npm:

   ```bash
   npm install
   ```

3. Build the frontend:

   ```bash
   npm run build
   ```

### 4. Start the app

To start the application, run the `start_all.sh` script. This script will do the following:

- Install frontend dependencies
- Build the frontend
- Set up and start the backend (collect system stats, start Flask server)
- Serve the frontend on the web



Run the script:

```bash
chmod +x start_all.sh  # Make sure the script is executable
./start_all.sh         # Run the script to start the app
```

Once the script finishes, the application will be running, and you can access the Raspberry Pi stats through a web interface.

## Usage

Once the app is running, you can access it from any device on your local network by navigating to:

```
http://<raspberry-pi-ip>:3000 or http://raspberrypi.local:3000
```

Where `<raspberry-pi-ip>` is the IP address of your Raspberry Pi.

## Backend

The backend is built with **Python** using the **Flask** framework and serves the system statistics to the frontend. The stats are logged into a CSV file. Each time you start the app the stats are removed, the goal is to track the stats only for each session.

### Key Backend Files:

- `get_stats.py`: Collects system stats (e.g., CPU usage, memory usage).
- `log_stats.py`: Logs the collected stats into a CSV file.
- `wsgi.py`: Entry point for the Flask server, to be used by Gunicorn.

## Frontend

The frontend is built using **Vue.js** and provides a clean interface to display the system statistics collected by the backend.

## Contributing

Feel free to fork this project and submit pull requests. Any improvements or suggestions are welcome.

## License

This project is open-source and available under the [MIT License](LICENSE).
