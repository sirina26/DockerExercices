from flask import Flask, request, jsonify
import requests
import time

app = Flask(__name__)
server3_url = "http://coordinate-service:8080"

@app.route('/send_address', methods=['GET'])
def send_address():
    my_url = request.host_url.rstrip('/')  # Obtient l'URL du serveur gateway
    try:
        response = requests.post(f'{server3_url}/receive_address', json={'address': my_url})
        print("Gateway sent its address to Server 3")
        return "Address sent to Server 3"
    except requests.exceptions.RequestException as e:
        print("Error sending address to Server 3:", e)
        return "Error sending address"

@app.route('/send_pong', methods=['GET'])
def send_pong():
    try:
        server_addresses = requests.get(f'{server3_url}/server_addresses').json()
        for address in server_addresses:
            try:
                response = requests.get(f'{address}/pong')
                print(f"Gateway sent 'pong' to {address}")
            except requests.exceptions.RequestException as e:
                print(f"Error sending 'pong' to {address}: {e}")
        return "Pong sent to all servers"
    except requests.exceptions.RequestException as e:
        print("Error getting server addresses from Server 3:", e)
        return "Error getting server addresses"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
