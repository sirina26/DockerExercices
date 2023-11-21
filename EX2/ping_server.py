import requests
import time
from flask import Flask

app = Flask(__name__)

annuaire_url = 'http://127.0.0.1:5002'

@app.route('/pong', methods=['GET'])
def pong():
    print("Received pong from Server 1")
    time.sleep(0.5)

    response = requests.get(f'{annuaire_url}/serveurs/pong_server')
    
    if 'serveur_url' in response.json():
        serveur_url = response.json()['serveur_url']
        print(f"Server 2 got serveur_url: {serveur_url}")

        response = requests.get(f'{serveur_url}/ping')
        print(f"Sent ping to Server 1. Response: {response.text}")
        return response.text
    else:
        print("Failed to get serveur_url from annuaire.")
        return 'error'

# Ajout de la route /ping
@app.route('/ping', methods=['GET'])
def ping():
    return "Received ping from Server 2"

# Ajout de la route pour éviter l'erreur 404
@app.route('/', methods=['GET'])
def index():
    return "Ping Server is running"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
