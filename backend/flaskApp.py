from flask import Flask, jsonify, request
from flask_cors import CORS

from backend.accountData.cards.cardDirectory import cardDirectory
from backend.routes.userRoutes import userRoutes
from backend.accounts.userAccounts import userAccounts
#from models import userModel, cardModel, rewardModel


app = Flask(__name__)
CORS(app) #allows the app to be called from other sources


app.register_blueprint(userRoutes)

#for debugging purposes, prints all the routes in the app
for rule in app.url_map.iter_rules():
    print(rule)

@app.route('/getAllCards', methods=['GET'])
def getAllCards():
    cd = cardDirectory()
    cards = cd.getAllCards()
    cd.close()
    return jsonify({"cards":cards})

@app.route("/")
def home():
    return jsonify({"message": "Welcome to creditCardAPI"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

#added later
#addUser
#getUserCards
#getCardRewards
#addCardToUser
