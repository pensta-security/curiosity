from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.models.models import Project
from app import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    """Main dashboard page"""
    projects_count = Project.query.count()
    return render_template('dashboard.html', projects_count=projects_count)

@main.route('/about')
def about():
    """About page with application information"""
    return render_template('about.html')
