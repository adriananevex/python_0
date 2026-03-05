def ft_water_reminder():
    last_watering = int(input("Day(s) since last watering: "))

    if last_watering > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
