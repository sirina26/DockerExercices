from flask import Flask

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    print("Received ping from Server 2")
    return 'pong'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)
