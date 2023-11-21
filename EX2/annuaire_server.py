from flask import Flask, request, jsonify

app = Flask(__name__)

# Dictionnaire pour stocker les informations des serveurs enregistrés
serveurs = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    serveurs[data['serveur_name']] = data['serveur_url']
    return jsonify({'message': 'Server registered successfully'})

@app.route('/serveurs/<serveur_name>', methods=['GET'])
def get_serveur_url(serveur_name):
    serveur_url = serveurs.get(serveur_name)
    if serveur_url:
        return jsonify({'serveur_url': serveur_url})
    else:
        return jsonify({'error': 'Serveur not found'}), 404

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002)
