# Command to connect to MAVPROXY
# mavproxy.py --master=/dev/ttyS0 --baudrate 57600 --aircraft MyCopter

# Import DroneKit-Python
from dronekit import connect, VehicleMode
import time
# Connect to the Vehicle.
vehicle = connect('/dev/ttyS0', wait_ready=True, baud=57600)
# Get some vehicle attributes (state)
print "Get some vehicle attribute values:"
print " GPS: %s" % vehicle.gps_0
print " Battery: %s" % vehicle.battery
# print " Last Heartbeat: %s" % vehicle.last_heartbeat
print " Is Armable?: %s" % vehicle.is_armable
print " System status: %s" % vehicle.system_status.state
print " Mode: %s" % vehicle.mode.name    # settable

print("DRONE ARM: " + str(vehicle.armed))

def arm_and_takeoff(aTargetAltitude):
    print "Basic pre-arm checks"
    while not vehicle.is_armable:
        print "Waiting for vehicle to initialise..."
        time.sleep(1)
    print "Arming motors"
    # Copter should 'arm' in GUIDED mode
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    # Confirm vehicle armed before attempting to take off
    while not vehicle.armed:
        print "Waiting for arming..."
        time.sleep(1)
    print "Taking off!"
    vehicle.simple_takeoff(aTargetAltitude) # take off.

    while True:
        print "Altitude: ", vehicle.location.global_relative_    frame.alt
        if vehicle.location.global_relative_frame.alt >= aTar    getAltitude*0.95:
            print "Reached target altitude"
            break
        time.sleep(1)
arm_and_takeoff(2)
vehicle.close()

print("Completed")