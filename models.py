from flask_sqlalchemy import SQLAlchemy
from app import APP


APP.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///bluetooth.db"
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
database = SQLAlchemy(APP)

class BluetoothData(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    distance = database.Column(database.Float, nullable=False)
    rssi = database.Column(database.Integer, nullable=False)
    material = database.Column(database.String, nullable=False)



database.create_all()
