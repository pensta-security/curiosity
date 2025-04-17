from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify

system = Blueprint('system', __name__)

@system.route('/sys')
def index():
    """Main page"""
    return render_template('system/index.html')


@system.route('/update')
def update():
    """update page"""
    return jsonify({"message": "Manifest is running"}), 200