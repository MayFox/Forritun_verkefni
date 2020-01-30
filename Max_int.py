north_int = int(input("Number of cars travelling north: "))
south_int = int(input("Number of cars travelling south: "))
east_int = int(input("Number of cars travelling east: "))
west_int = int(input("Number of cars travelling west: "))


while north_int > 0 or south_int > 0 or west_int > 0 or east_int > 0:
    if north_int > east_int and north_int > west_int or south_int > east_int and south_int > west_int:
        if north_int > 0:
            north_int = north_int - 5
        if south_int > 0:
            south_int = south_int - 5
        print ("Green light on N/S")
    else:
        if east_int > 0:
            east_int = east_int - 5
        if west_int > 0:
            west_int = west_int - 5
        print ("Green light on E/W")

    if north_int < 0:
        north_int = 0
    if south_int < 0:
        south_int = 0
    if west_int < 0:
        west_int = 0
    if east_int < 0:
        east_int = 0

print("No cars waiting, the traffic jam has been solved!")