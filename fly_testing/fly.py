# Import DroneKit-Python
from dronekit import connect, VehicleMode

# Connect to the Vehicle.
vehicle = connect('/dev/ttyS0', wait_ready=True, baud=57600) 

# Get some vehicle attributes (state)
print "Get some vehicle attribute values:"
print " GPS: %s" % vehicle.gps_0
print " Battery: %s" % vehicle.battery
print " Last Heartbeat: %s" % vehicle.last_heartbeat
print " Is Armable?: %s" % vehicle.is_armable
print " System status: %s" % vehicle.system_status.state
print " Mode: %s" % vehicle.mode.name    # settable

# Imports for OpenCV

# Start OpenCV Loop

# On detect area's movement

	# Move in movement's direction
		# Function call to move

# End OpenCV Loop

# End Section (Close everything that needs closing)

	# Close vehicle object before exiting script

vehicle.close()

	# Checking Complete

print("Completed")
