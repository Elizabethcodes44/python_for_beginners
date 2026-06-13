#traffic light simulator.create a variable lightcolor and assign it a value of red, yellow or green. Use an if statement to print what action a driver should take.
light_color = input("Hi driver, what is the traffic light color? (red/yellow/green): ")

if light_color == "red":
    print("Stop")
elif light_color == "yellow":
    print("Slow down and prepare to stop")
elif light_color == "green":
    print("Go")