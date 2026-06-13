#traffic light simulator.create a variable lightcolor and assign it a value of red, yellow or green. Use an if statement to print what action a driver should take.
lightcolor = "red"  # Example value, can be changed to "yellow" or "green"

if lightcolor == "red":
    print("Driver should stop.")
elif lightcolor == "yellow":
    print("Driver should prepare to stop.")
elif lightcolor == "green":
    print("Driver can proceed.")