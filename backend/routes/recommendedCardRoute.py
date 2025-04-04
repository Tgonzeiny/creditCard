from flask import Blueprint, request, jsonify

recommendedCardBlueprint = Blueprint("recommendedCard", __name__)

@recommendedCardBlueprint.route("/recommend-card", methods = ["GET"])
def recommendCard():
    mcc = request.args.get("mcc")

    #Will store card logic later for example "Card name" -> MCC
    cardMap = {}

    recommended = cardMap.get(mcc, "Default Card")

    return jsonify({ "recommendedCard": recommended })