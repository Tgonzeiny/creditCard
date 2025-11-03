from urllib import request

from flask import jsonify

from backend.accounts.userAccounts import userAccounts
from backend.routes.userRoutes import userRoutes


@userRoutes.route('/add_card', methods=['POST'])
def add_card():
    data = request.get_json()
    username = data['username']
    card_id = data['card_id']

    if not username or not card_id:
        return jsonify({"Success": False, "message": "Username and card_id are required"})

    user = userAccounts().getUserbyUsername(username)
    if not user:
        return jsonify({"Success": False, "message": "User not found"}), 404

    user_id = user['user_id']

    result = userAccounts().addCardToUser(user_id, card_id)

    if result['success']:

        return jsonify({"Success": True, "message": result['message']}), 200
    else:
        return jsonify({"Success": False, "message": result['message']}), 500
