from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/data')
def data():
    return jsonify(message="Hello from the server!")

if __name__ == '__main__':
    app.run(debug=True)
