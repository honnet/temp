#!/usr/bin/python
import serial

SENSOR_SERIAL = "/dev/ttyACM*"
LEDS_SERIAL   = "/dev/ttyACM*"

DEBUG_PRINT = True


# SENSOR ######################################################################
def sensor_init():
    devices = glob.glob(SENSOR_SERIAL)

    if DEBUG_PRINT:
        print devices

    sensor = serial.Serial(devices[0], 115200)

    success = sensor.isOpen()
    if not success:
        print "\n!!! Error: sensor serial port not found !!!"

    return sensor


# LEDS ########################################################################
def LEDs_init():
    devices = glob.glob(LEDS_SERIAL)

    if DEBUG_PRINT:
        print devices

    LEDs = serial.Serial(devices[0], 115200)

    success = LEDs.isOpen()
    if not success:
        print "\n!!! Error: LEDs serial port not found !!!"

    return LEDs


# MAIN ########################################################################
def main():
    sensor = sensor_init()
    LEDs   = LEDs_init()

    while True:
        temp = sensor.readline()
        # sensor.flush() # TODO on OSx? (to avoid potential overflow)
        LEDs.write(temp)


if __name__ == "__main__":
    main()

