from flask import Flask, jsonify
import os

app = Flask(__name__)

LOG_PATH = 'temp/stats_log.log'
#Usually the approach is terrible but i think it suits my needs here
DATA_SIZE = [1, 1, 4, 4, 4, 1] #cpu temp, cpu usage, memory stats, disk stats, network stats, uptime

@app.route('/api/stats', methods=['GET'])
def get_stats():
    if os.path.exists(LOG_PATH):
        all_stats = []
        with open(LOG_PATH, 'r') as file:
            chunks = file.read().split(',')
            for chunk in chunks:
                stats = {
                    'cpu_temp': float(chunks[0]),
                    'cpu_usage': float(chunks[1]),
                    'memory_stats': chunks[2:6],
                    'disk_stats': chunks[6:10],
                    'network_stats': chunks[10:14],
                    'uptime': float(chunks[14])
                }
                all_stats.append(stats)
        
        return jsonify(all_stats)    
    return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)