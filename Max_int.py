north_int = int(input("Number of cars travelling north: "))
south_int = int(input("Number of cars travelling south: "))
east_int = int(input("Number of cars travelling east: "))
west_int = int(input("Number of cars travelling west: "))

W_e = west_int + east_int
#cars = 1
N_s = south_int + north_int
while north_int > 0 or south_int > 0 or west_int > 0 or east_int > 0: 
    #cars = south_int + north_int + west_int + east_int
    if north_int or south_int > west_int or east_int:
        if north_int > 0:
            north_int = north_int - 5
        elif north_int <= 0:
            north_int = 0
        elif south_int > 0: 
            south_int = south_int - 5
        elif south_int <= 0:
            south_int
        print("Green light on N/S")
    elif N_s < W_e: 
        if west_int > 0:
            west_int = west_int - 5
        elif west_int <= 0:
            west_int = 0
        elif east_int > 0: 
            east_int = east_int - 5
        elif east_int <= 0:
            east_int
        print("Green light on E/W")

print("No cars waiting, the traffic jam has been solved!")S