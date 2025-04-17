from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Curiosity API is running"}), 200

@app.route('/run-manifest')
def runmanifest():
    return jsonify({"message": "Manifest is running"}), 200

@app.route('/update')
def update():
    return jsonify({"message": "Update running"}), 200

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
