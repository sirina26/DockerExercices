import time
from flask import Flask, request, jsonify

app = Flask(__name__)
server_addresses = {'s1': 'http://ping-service:4567', 's2': 'http://pong-service:5372'}

@app.route('/get_address/<server_name>', methods=['GET'])
def get_address(server_name):
    return jsonify({'address': server_addresses.get(server_name)})

if __name__ == '__main__':
    time.sleep(10)
    app.run(host='0.0.0.0', port=1111)
