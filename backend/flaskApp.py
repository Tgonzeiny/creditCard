from flask import Flask, jsonify, request
from flask_cors import CORS

from backend.accountData.cards.cardDirectory import cardDirectory
from backend.routes.userRoutes import userRoutes
from backend.accounts.userAccounts import userAccounts
#from models import userModel, cardModel, rewardModel


flaskApp = Flask(__name__)
CORS(flaskApp) #allows the app to be called from other sources


flaskApp.register_blueprint(userRoutes)

@flaskApp.route('/getAllCards', methods=['GET'])
def getAllCards():
    cd = cardDirectory()
    cards = cd.getAllCards()
    cd.close()
    return jsonify({"cards":cards})

# This route will handle user login
@flaskApp.route('/api/login', methods=['POST'])
def login():
    print('Login request received')
    data = request.get_json()
    email = data['email']
    password = data['password']
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

@flaskApp.route("/")
def home():
    return jsonify({"message": "Welcome to creditCardAPI"})

if __name__ == '__main__':
    flaskApp.run(host='0.0.0.0', port=5000, debug=True)

#added later
#addUser
#getUserCards
#getCardRewards
#addCardToUser
