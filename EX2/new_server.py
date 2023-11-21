import requests
from flask import Flask, jsonify

app = Flask(__name__)

annuaire_url = 'http://127.0.0.1:5002'
serveur_name = 'new_server'
serveur_url = 'http://127.0.0.1:5003'

# Enregistrement du nouveau serveur
requests.post(f'{annuaire_url}/register', json={'serveur_name': serveur_name, 'serveur_url': serveur_url})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5003)
