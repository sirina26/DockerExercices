from flask import Flask
import requests

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    print("Reçoit ping de Server 2")
    return 'pong'

def register_with_server3(server3_url):
    my_url = 'http://127.0.0.1:5001'  # Change this to the actual URL of Server 1
    requests.post(f'{server3_url}/register', json={'serveur_name': 'Serveur1', 'serveur_url': my_url})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)
    register_with_server3('http://127.0.0.1:5002')  # Assume Server 3 is running on port 5002
