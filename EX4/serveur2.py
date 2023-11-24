from flask import Flask, request
import requests
import time
from threading import Thread
import socket

app = Flask(__name__)
server_3_url = "http://coordinate-service:8080"
message_broker_url = "http://serveur4:1111"
app.config['NETWORK_NAME'] = 'pong-net-1'

def send_pong():
    while True:
        time.sleep(0.5)
        try:
            response = requests.get(message_broker_url + "/get_address/s1", timeout=5)
            server_1_address = response.json().get('address')
            if server_1_address:
                response = requests.get(server_1_address + "/", timeout=5)
                print("Server Pong received ping from Server Ping via Message Broker:", response.text)
            else:
                print("Server Pong: Unable to get Server Ping address from Message Broker")
        except requests.exceptions.RequestException as e:
            print("Error sending pong:", e)

@app.route('/')
def ping():
    return "ping"

@app.route('/send_address')
def send_address():
    try:
        response = requests.post(server_3_url + "/receive_address", json={"address": message_broker_url})
        print("Server Pong sent its address to Server 3")
        return "Address sent to Server 3"
    except requests.exceptions.RequestException as e:
        print("Error sending address to Server 3:", e)
        return "Error sending address"

if __name__ == '__main__':
    pong_thread = Thread(target=send_pong)
    pong_thread.start()

    app.run(host='0.0.0.0', port=5372)
