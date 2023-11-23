import time
from flask import Flask, request, jsonify

app = Flask(__name__)
server_addresses = {'s1': 'http://ping-service:4567', 's2': 'http://pong-service:5372'}

@app.route('/receive_address', methods=['POST'])
def receive_address():
    data = request.get_json()
    server_name = data.get('server_name')
    server_address = data.get('address')
    if server_name and server_address:
        server_addresses[server_name] = server_address
        print(f"Address received for {server_name}: {server_address}")
        return "Address received"
    else:
        return "Invalid address format"

@app.route('/server_addresses', methods=['GET'])
def get_server_addresses():
    return jsonify(server_addresses)

if __name__ == '__main__':
    time.sleep(10)
    app.run(host='0.0.0.0', port=8080)
