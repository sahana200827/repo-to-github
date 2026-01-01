def traffic_light(cycles=5):
    lights = ["RED - STOP", "GREEN - GO", "YELLOW - SLOW DOWN"]
    for i in range(cycles):
        print(lights[i % 3])

# Run for 9 cycles
traffic_light(9)