# Command to connect to MAVPROXY
# mavproxy.py --master=/dev/ttyS0 --baudrate 57600 --aircraft MyCopter

import sys
# Import DroneKit-Python
from dronekit import connect, VehicleMode
import time

def writeFlush(text):
    
    sys.stdout.write(text)
    sys.stdout.flush()

def arm_and_takeoff(vehicle, aTargetAltitude):
    writeFlush("Basic pre-arm checks\n")

    while not vehicle.is_armable:
        writeFlush("Waiting for vehicle to initialise...\n")
        time.sleep(1)
    writeFlush("Arming motors")

    # Copter should 'arm' in GUIDED mode
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    # Confirm vehicle armed before attempting to take off
    while not vehicle.armed:
        writeFlush("Waiting for arming...")
        time.sleep(1)
    
    writeFlush("Taking off!")
    vehicle.simple_takeoff(aTargetAltitude) # Take off.

    # Ascension
    while True:
        writeFlush("Altitude: %s\n" % str(vehicle.location.global_relative_frame.alt))
        if vehicle.location.global_relative_frame.alt >= aTargetAltitude*0.95:
            writeFlush("Reached target altitude")
            break
        time.sleep(1)

    # Landing
    writeFlush("Setting LAND mode...")
    vehicle.mode = VehicleMode("LAND")

def main():
    targetAltitude = int(sys.argv[1])
    writeFlush("Target altitude: " + str(targetAltitude))

    # Connect to the Vehicle.
    vehicle = connect('/dev/ttyS0', wait_ready=True, baud=57600)

    # Get some vehicle attributes (state)
    writeFlush("Get some vehicle attribute values:\n")
    writeFlush("GPS: %s\n" % vehicle.gps_0)
    writeFlush("Battery: %s\n" % vehicle.battery)
    writeFlush("Is Armable?: %s\n" % vehicle.is_armable)
    writeFlush("System status: %s\n" % vehicle.system_status.state)
    writeFlush("Mode: %s\n" % vehicle.mode.name)
    writeFlush("DRONE ARM: " + str(vehicle.armed) + "\n")

    arm_and_takeoff(vehicle, targetAltitude)
    vehicle.close()

    writeFlush("SCRIPT ENDED")

if __name__ == '__main__':
    main()

# print " Last Heartbeat: %s" % vehicle.last_heartbeat