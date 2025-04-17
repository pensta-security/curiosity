from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Curiosity API is running"}), 200

@app.route('/run-manifest')
def runmanifest():
    return jsonify({"message": "Manifest is running"}), 200

@app.route('/update', methods=['POST'])
def update():
    temp_file="/manifest-templates/update.yaml"
    # Delete the manifest incase its already ran like a job and sticks around
    result_delete_cmd = subprocess.run(['kubectl', 'delete', '-f', temp_file], 
                               capture_output=True, text=True, check=True)
    # Apply the manifest
    result_create_cmd = subprocess.run(['kubectl', 'apply', '-f', temp_file], 
                               capture_output=True, text=True, check=True)
    
    return jsonify({"message": "Update running"}), 200

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
