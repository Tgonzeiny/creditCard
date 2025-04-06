from flask import Flask, jsonify, request
from flask_cors import CORS
from models import userModel, cardModel, rewrardModel


flaskApp = flask(__name__)
CORS(flaskApp)