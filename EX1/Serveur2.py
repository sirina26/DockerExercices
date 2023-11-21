import requests
import time
from flask import Flask

app = Flask(__name__)

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

#pip install flask
#pip install requests
#python Serveur2.py
#http://127.0.0.1:5000
## Exercice 1 : ping pong

#Ecrire deux serveurs devant communiquer l'un avec l'autre.
#
#- le premier doit envoyer une requête http "pong" vers le deuxième
#- à ce moment le second a une demie seconde pour lui envoyer une requête "ping"
#- à la récepetion de cette requête le premier a alors une demie seconde pour lui envoyer une requête "pong"
#
#Les deux serveurs connaissent l'adresse l'un de l'autre à l'avance.
#
#![](./img/fig1.png)
#(N'oubliez pas de commit).