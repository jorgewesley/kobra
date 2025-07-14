from flask import Blueprint, request, jsonify
from jose import jwt
from passlib.context import CryptContext
from config import Config

auth_bp = Blueprint('auth', __name__)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    # Implemente lógica de autenticação aqui
    token = jwt.encode({'sub': username}, Config.SECRET_KEY, algorithm='HS256')
    return jsonify({'token': token})