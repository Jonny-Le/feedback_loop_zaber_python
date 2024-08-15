from zaber_motion.ascii import Connection
from zaber_motion import Units

STARTING_CONSTANT = 17                             #Starting position in millimeters. Default is 17mm

connection = None

def zaber_connect(zaber_device):
    """Connect to the Zaber device and return the device object."""
    global connection
    if connection is None or not connection.is_open():
        connection = Connection.open_serial_port("/dev/tty.usbserial-A10NGE60")  #Change connection as needed
        connection.enable_alerts()
        device_list = connection.detect_devices()
        print("Found {} devices".format(len(device_list)))

        zaber_device = device_list[0]
        return zaber_device.get_axis(1)
    else:
        print("Connection already open.")
        return connection.detect_devices()[0].get_device(1)

def zaber_calibration(zaber, move_direction, move_value):

    port_string = ""

    if zaber.is_parked():
        zaber.unpark()

    if move_direction == "down":
        # Move down to the sensor
        zaber.move_relative(move_value, Units.LENGTH_MILLIMETRES)
        print("Moved down to touch the sensor.")

    elif move_direction == "up":
        # Move back up to starting position
        zaber.move_absolute(STARTING_CONSTANT, Units.LENGTH_MILLIMETRES)
        zaber.park()
        print("Moved back to starting position and parked.")

def zaber_test():
    return 0