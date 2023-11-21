import requests
from flask import Flask

app = Flask(__name__)

annuaire_url = 'http://127.0.0.1:5002'
serveur_name = 'serveur1'
serveur_url = 'http://127.0.0.1:5001'

# Enregistrement du serveur auprès de l'annuaire
requests.post(f'{annuaire_url}/register', json={'serveur_name': serveur_name, 'serveur_url': serveur_url})

@app.route('/ping', methods=['GET'])
def ping():
    print("Reçoit ping de Server 2")
    return 'pong'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)
