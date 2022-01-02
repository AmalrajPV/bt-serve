from flask_marshmallow import Marshmallow
from models import BluetoothData
from app import APP
ma = Marshmallow(APP)

class BluetoothDataSchema(ma.Schema):
    class Meta:
        model = BluetoothData
        fields = ("id", "distance", "material", "rssi")


bluetooth_schema = BluetoothDataSchema(many=True)

