from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def home():
    return jsonify("Hello, World!")


@app.route('/health')
def health():
    return jsonify("I'm alive")


@app.route('/ready')
def ready():
    return jsonify("I'm ready to proceed")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8080, use_reloader=False)
