import requests
import time
from flask import Flask

app = Flask(__name__)

annuaire_url = 'http://127.0.0.1:5002'
serveur_name = 'serveur2'
serveur_url = 'http://127.0.0.1:5000'

# Enregistrement du serveur auprès de l'annuaire
requests.post(f'{annuaire_url}/register', json={'serveur_name': serveur_name, 'serveur_url': serveur_url})

pong_server_url = 'http://127.0.0.1:5001'

@app.route('/pong', methods=['GET'])
def pong():
    print("Reçoit pong de Server 1")
    time.sleep(0.5)  # Wait for 0.5 seconds
    response = requests.get(f'{pong_server_url}/ping')
    print("Envoie ping au Server 1")
    return response.text

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
