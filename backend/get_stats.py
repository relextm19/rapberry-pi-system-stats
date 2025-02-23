from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import os
import csv
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

LOG_PATH = 'temp/stats_log.csv'

def parse_value(value):
    #convert string to list if possible
    try:
        parsed = json.loads(value)  
        if isinstance(parsed, list):
            return parsed
    except json.JSONDecodeError:
        pass
    return value  

@app.route('/api/stats', methods=['GET'])
@cross_origin()
def get_stats():
    if os.path.exists(LOG_PATH):
        stats = [[] for _ in range(6)] #booo! magic number. Its the number of columns in the csv file which is 99.9% not going to change
        with open(LOG_PATH, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                for i in range(6):
                    stats[i].append(parse_value(row[i]))
        return jsonify(stats)    
    return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)