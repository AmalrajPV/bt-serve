from app import APP
from flask import request
from flask_restful import Resource, Api
from models import BluetoothData, database
from serialize import bluetooth_schema


api = Api(APP)

@APP.route('/')
def home():
    return "welcome"

class BtView(Resource):
    def get(self):
        data = BluetoothData.query.all()
        return bluetooth_schema.dump(data)

    def post(self):
        distance = request.form['distance']
        material = request.form['material']
        rssi = request.form['rssi']
        recived = BluetoothData(distance=distance, material=material, rssi=rssi)
        database.session.add(recived)
        database.session.commit()
        data = BluetoothData.query.all()

        return bluetooth_schema.dump(data)

api.add_resource(BtView, '/list')

if __name__ == '__main__':
    APP.run(debug=False)