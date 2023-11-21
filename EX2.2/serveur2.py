from flask import Flask
import requests
import time

app = Flask(__name__)

pong_server_url = 'http://127.0.0.1:5001'

@app.route('/pong', methods=['GET'])
def pong():
    print("Reçoit pong de Server 1")
    time.sleep(0.5)  # Attendez 0.5 secondes
    response = requests.get(f'{pong_server_url}/ping')
    print("Envoie ping au Server 1")
    return response.text

def register_with_server3(server3_url):
    my_url = 'http://127.0.0.1:5000'  # Change this to the actual URL of Server 2
    requests.post(f'{server3_url}/register', json={'serveur_name': 'Serveur2', 'serveur_url': my_url})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
    register_with_server3('http://127.0.0.1:5002')  # Assume Server 3 is running on port 5002
