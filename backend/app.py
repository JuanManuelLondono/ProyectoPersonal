from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"Mensaje": "API funcionando"})

if __name__ == '__main__':
    app.run(debug=True)
