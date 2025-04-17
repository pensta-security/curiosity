import os
from pathlib import Path

class Config:
    # Application configuration
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-key-for-curiosity-application')
    
    # Database configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///curiosity.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    
    # Manifest categories
    MANIFEST_CATEGORIES = ['osintel', 'scanner', 'utils', 'services', 'labs']