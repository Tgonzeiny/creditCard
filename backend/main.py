from flask import Flask
from flask_cors import CORS
from routes.recommendedCardRoute import recommendedCardBlueprint

def startApp():
    app = Flask(__name__)

    CORS(app)

    app.register_blueprint(recommendedCardBlueprint)

    return app

if __name__ == "__main__":
    app = startApp()
    app.run(debug=True, host="0.0.0.0", port = 5000)