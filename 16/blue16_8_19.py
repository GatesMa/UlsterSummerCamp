from bluepy.btle import BTLEException
from bluepy import sensortag
from bluepy.sensortag import SensorTag
import time
import datetime

SENSORTAG_ADDRESS = "54:6C:0E:53:1E:3D"

print('Connecting to {}'.format(SENSORTAG_ADDRESS))
tag = SensorTag(SENSORTAG_ADDRESS)

def enable_sensors(tag):
    tag.IRtemperature.enable()
    tag.barometer.enable()
    tag.lightmeter.enable()
    tag.gyroscope.enable()
    time.sleep(1.0)

def disable_sensors(tag):
    tag.IRtemperature.disable()
    tag.barometer.disable()
    tag.lightmeter.disable()
    tag.gyroscope.disable()

def get_readings(tag):
    try:
        enable_sensors(tag)
        readings = {}

        readings["ir_temp_amb"], readings["ir_temp_obj"] = tag.IRtemperature.read()
        readings["baro_temp"], readings["pressure"] = tag.barometer.read()
        readings["light"] = tag.lightmeter.read()
        readings["gyro_x"], readings["gyro_y"], readings["gyro_z"] = tag.gyroscope.read()
        readings = {key: round(value, 2) for key, value in readings.items()}
        return readings
    except BTLEException as e:
        print("Unable to take sensor readings.")
        print(e)
        return {}
def reconnect(tag):
    try:
        tag.connect(tag.deviceAddr, tag.addrType)
    except Exception as e:
        print("Unable to reconnect to SensorTag.")
        raise e
    



while True:
    readings = get_readings(tag)
    if not readings:
        print("SensorTag disconnected. Reconnecting.")
        reconnect(tag)
        continue
    print("Time:\t{}".format(datetime.datetime.now()))
    print("Temperature:\t", readings["ir_temp_obj"])
    print("Pressure: \t", readings["pressure"])
    print("Lightmeter:\t", readings["light"])
    print("Gryoscope(X, Y, Z):\t", readings["gyro_x"], readings["gyro_y"], readings["gyro_z"])
    print('--------------------------------------')
