from flask import Flask, request
import requests
import time
from threading import Thread

app = Flask(__name__)
server_3_url = "http://coordinate-service:8080"
message_broker_url = "http://serveur4:1111"


def send_ping():
    while True:
        time.sleep(0.5)
        try:
            response = requests.get(message_broker_url + "/get_address/s2", timeout=5)
            server_2_address = response.json().get('address')
            if server_2_address:
                response = requests.get(server_2_address + "/", timeout=5)
                print("Server Ping received ping from Server Pong via Message Broker:", response.text)
            else:
                print("Server Ping: Unable to get Server Pong address from Message Broker")
        except requests.exceptions.RequestException as e:
            print("Error sending ping:", e)

@app.route('/')
def pong():
    return "pong"

@app.route('/send_address')
def send_address():
    try:
        response = requests.post(server_3_url + "/receive_address", json={"address": message_broker_url})
        print("Server Ping sent its address to Server 3")
        return "Address sent to Server 3"
    except requests.exceptions.RequestException as e:
        print("Error sending address to Server 3:", e)
        return "Error sending address"

if __name__ == '__main__':
    ping_thread = Thread(target=send_ping)
    ping_thread.start()

    app.run(host='0.0.0.0', port=4567)
