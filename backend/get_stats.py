from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

LOG_PATH = 'temp/stats_log.log'
#Usually the approach is terrible but i think it suits my needs here
#DATA_SIZE = [1, 1, 4, 4, 4, 1] cpu temp, cpu usage, memory stats, disk stats, network stats, uptime

@app.route('/api/stats', methods=['GET'])
def get_stats():
    if os.path.exists(LOG_PATH):
        all_stats = []
        with open(LOG_PATH, 'r') as file:
            chunks = file.read().split(',')
            '''
            we ittarate through the chunks of data moving 15 steps at a time cause thats the size of one chunk.
            the -1 accounts for the last comma which doesnt lead to any data
            '''
            for i in range(0, len(chunks) - 1, 15):               
                print(chunks[i:i+15])
                stats = {
                    'cpu_usage': float(chunks[0 + i]),
                    'cpu_temp': float(chunks[1 + i]),
                    'memory_stats': chunks[2 + i:6 + i],
                    'disk_stats': chunks[6 + i:10 + i],
                    'network_stats': chunks[10 + i:14 + i],
                    'uptime': float(chunks[14 + i])
                }
                all_stats.append(stats)
        
        return jsonify(all_stats)    
    return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)