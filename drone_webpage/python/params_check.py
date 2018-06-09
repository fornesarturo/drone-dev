def writeFlush(text):
    import sys
    sys.stdout.write(text)
    sys.stdout.flush()

def main():
    # Import DroneKit-Python
    from dronekit import connect, VehicleMode
    import time

    # Connect to the Vehicle.
    vehicle = connect('/dev/ttyS0', wait_ready=True, baud=57600)

    # Get some vehicle attributes (state)
    writeFlush("Get some vehicle attribute values:")
    writeFlush(" GPS: %s" % vehicle.gps_0)
    writeFlush("Battery: %s" % vehicle.battery)
    writeFlush("Is Armable?: %s" % vehicle.is_armable)
    writeFlush("System status: %s" % vehicle.system_status.state)
    writeFlush("Mode: %s" % vehicle.mode.name)
    writeFlush("DRONE ARM: " + str(vehicle.armed))

    vehicle.close()

    writeFlush("SCRIPT ENDED")

if __name__ == '__main__':
    main()

# print " Last Heartbeat: %s" % vehicle.last_heartbeat