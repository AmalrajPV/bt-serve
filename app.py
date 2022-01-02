from flask import Flask
from flask_cors import CORS 

APP = Flask(__name__)
CORS(APP) #allowing request from all header
