import time

# Safe following distance (meters)
SAFE_DISTANCE = 20

# Initial speeds (km/h)
vehicle_speed = 60
lead_vehicle_speed = 50

# Initial distance between vehicles
distance = 25


def adaptive_cruise_control(vehicle_speed, lead_vehicle_speed, distance):
    if distance < SAFE_DISTANCE:
        print("Vehicle too close! Slowing down.")
        vehicle_speed -= 5
    elif distance > SAFE_DISTANCE + 5:
        print("Safe distance. Speeding up.")
        vehicle_speed += 2
    else:
        print("Maintaining speed.")

    return vehicle_speed


print("Starting Adaptive Cruise Control Simulation\n")

for step in range(5):

    print(f"Step {step+1}")
    print(f"Distance to lead vehicle: {distance} meters")
    print(f"Current speed: {vehicle_speed} km/h")

    vehicle_speed = adaptive_cruise_control(
        vehicle_speed, lead_vehicle_speed, distance
    )

    # Simulate changing traffic distance
    distance -= 3

    time.sleep(1)
    print("-" * 30)
