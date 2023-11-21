from flask import Flask

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    print("Reçoit ping de Server 2")
    return 'pong'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)

#pip install flask
#python Serveur1.py
#http://127.0.0.1:5001