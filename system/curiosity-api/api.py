from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Curiosity API is running"}), 200

if __name__ == '__main__':
    app.run(debug=True, host=0.0.0.0)
