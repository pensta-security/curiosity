from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify

system = Blueprint('system', __name__)

@system.route('/sys')
def index():
    """Main page"""
    return render_template('system/index.html')


@system.route('/update')
def update():
    """update page"""
    try:
        data = []
        response = requests.post('http://curiosity-api-service.default.svc.cluster.local/update', json=data, timeout=2)
        response.raise_for_status()
        return jsonify({'message': 'Update running...'})
    except requests.RequestException as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500
    return jsonify({"message": "Update running..."}), 200