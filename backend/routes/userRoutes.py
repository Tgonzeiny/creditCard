from flask import Blueprint, jsonify, request
from backend.accounts.userAccounts import userAccounts
from backend.security.passwordHandler import PasswordHandler

userRoutes = Blueprint('userRoutes', __name__)

@userRoutes.route('/api/register', methods=['POST'])
def createUser():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not all([username, email, password]):
        return jsonify({"success": False, "message": "Missing data"})
    
    password = hashPassword(password)
    user = userAccounts()

    if user.userExists(email):
        user.close()
        return jsonify({"success": False, "message": "User already exists"}), 400
    
    result = user.createUser(username, email, password)
    user.close()

    return jsonify(result), (200 if result['success'] else 400)

# This route will handle user login
@userRoutes.route('/api/login', methods=['POST'])
def login():
    print('Login request received')
    data = request.get_json()
    email = data['email']
    password = hashPassword(data['password'])

    login = userAccounts().loginUser(email, password)
    if login['success']:
        return jsonify({
            "message": login['message'], "user_id": login['user_id']
        }), 200
    else:
        print("Login failed for email:", email)
        return jsonify({
            "message": login['message']
        }), 401
    
# This function hashes the password using the PasswordHandler class
def hashPassword(password):
    passwordHandler = PasswordHandler()
    hashed_password = passwordHandler.hash_password(password)
    passwordHandler.close()
    return hashed_password
