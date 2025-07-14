import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'
    PORT = int(os.getenv('PORT', 8000))
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///app.db')