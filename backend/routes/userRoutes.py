from flask import Blueprint, jsonify, request
from backend.accounts.userAccounts import userAccounts

userRoutes = Blueprint('userRoutes', __name__)

@userRoutes.route('/createUser', methods=['POST'])
def createUser():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not all([username, email, password]):
        return jsonify({"success": False, "message": "Missing data"})

    user = userAccounts()
    result = user.createUser(username, email, password)
    user.close()

    return jsonify(result), (200 if result['success'] else 400)
