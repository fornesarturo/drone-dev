def writeFlush(text):
    import sys
    sys.stdout.write(text)
    sys.stdout.flush()

def main():
    # Import DroneKit-Python
    from dronekit import connect, VehicleMode

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

    vehicle.close()

    writeFlush("SCRIPT ENDED")

if __name__ == '__main__':
    main()

# print " Last Heartbeat: %s" % vehicle.last_heartbeat