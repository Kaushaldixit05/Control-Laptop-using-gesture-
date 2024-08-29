from pymavlink import mavutil

# Start a connection to the flight controller
connection = mavutil.mavlink_connection('/dev/ttyUSB0', baud=115200)

# Wait for a heartbeat from the flight controller
# This sets the system and component ID of remote system for the link
connection.wait_heartbeat()
print("Heartbeat received")

# Example: Requesting data from the flight controller
try:
    while True:
        msg = connection.recv_match(blocking=True)
        print(f"Received message: {msg}")
except KeyboardInterrupt:
    print("Exiting...")

# Close the connection when done
connection.close()