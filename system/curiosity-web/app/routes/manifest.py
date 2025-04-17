from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
import requests

manifest = Blueprint('manifest', __name__)

@manifest.route('/manifest/list')
def index():
    """Main page"""
    return render_template('manifest/list.html')

@manifest.route('/manifest/create')
def create():
    """Editor page"""
    return render_template('manifest/editor.html')