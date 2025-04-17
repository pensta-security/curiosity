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
    if(delete_and_create_from_manifest(temp_file)):
        return jsonify({"message": "Update running"}), 200
    else:
        return jsonify({"message": "Error running update!"}), 200

def delete_and_create_from_manifest(manifest_file):
    # Try deleting the manifest (ignore errors)
    try:
        result_delete_cmd = subprocess.run(
            ['kubectl', 'delete', '-f', manifest_file],
            capture_output=True, text=True, check=True
        )
    except subprocess.CalledProcessError as e:
        print("Delete failed:", e.stderr)

    # Try applying the manifest (ignore errors)
    try:
        result_create_cmd = subprocess.run(
            ['kubectl', 'apply', '-f', manifest_file],
            capture_output=True, text=True, check=True
        )
    except subprocess.CalledProcessError as e:
        print("Apply failed:", e.stderr)
        return False

    return True

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
