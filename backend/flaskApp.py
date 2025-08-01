from flask import Flask, jsonify
from flask_cors import CORS

from backend.accountData.cards.cardDirectory import cardDirectory
from backend.routes.userRoutes import userRoutes
#from models import userModel, cardModel, rewardModel


flaskApp = Flask(__name__)
CORS(flaskApp) #allows the app to abe called from other sources


flaskApp.register_blueprint(userRoutes)

if __name__ == '__main__':
    flaskApp.run(debug=True)

@flaskApp.route('/getAllCards', methods=['GET'])
def getAllCards():
    cd = cardDirectory()
    cards = cd.getAllCards()
    cd.close()
    return jsonify({"cards":cards})

@flaskApp.route("/")
def home():
    return jsonify({"message": "Welcome to creditCardAPI"})

#added later
#addUser
#getUserCards
#getCardRewards
#addCardToUser
