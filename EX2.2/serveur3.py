from flask import Flask, request, jsonify

app = Flask(__name__)

serveurs = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    serveurs[data['serveur_name']] = data['serveur_url']
    return jsonify({'message': 'Enregistré avec succès'})

@app.route('/ping_server', methods=['GET'])
def ping_server():
    serveur_name = request.args.get('serveur_name')
    if serveur_name in serveurs:
        serveur_url = serveurs[serveur_name]
        response = requests.get(f'{serveur_url}/ping')
        return response.text
    else:
        return jsonify({'message': 'Serveur non enregistré'})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002)
