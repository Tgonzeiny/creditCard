from flask import Blueprint, jsonify, request
from backend.accounts.userAccounts import userAccounts
from backend.security.passwordHandler import PasswordHandler
import jwt
import datetime

userRoutes = Blueprint('userRoutes', __name__)
SECRET_KEY = "changeLater" # In production, use a secure method to store this key

@userRoutes.route('/api/register', methods=['POST'])
def createUser():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not all([email, password]):
        return jsonify({"success": False, "message": "Missing data"})
    
    password = hashPassword(password)
    user = userAccounts()

    if user.userExists(email):
        user.close()
        return jsonify({"success": False, "message": "User already exists"}), 400
    
    result = user.createUser(email, password)
    user.close()

    return jsonify(result), (200 if result['success'] else 400)

# This route will handle user login
@userRoutes.route('/api/login', methods=['POST'])
def login():
    print('Login request received')
    data = request.get_json()
    email = data['email']
    password = (data['password'])

    login = userAccounts().loginUser(email, password)
    if login['success']:
        token = jwt.encode({
            'user_id': login['user_id'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        },
        SECRET_KEY, algorithm='HS256')

        return jsonify({
            "success": True,
            "message": login['message'],
            "user id": login['user_id'],
            "token": token
        }), 200

    else:
        print("Login failed for email:", email, data['password'])
        return jsonify({
            "success": False,
            "message": login['message']
        }), 401
    
# This function hashes the password using the PasswordHandler class
def hashPassword(password):
    passwordHandler = PasswordHandler()
    hashed_password = passwordHandler.hash_password(password)
    return hashed_password