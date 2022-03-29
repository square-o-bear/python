map1 = ["|", " ", " ", " ", "P"]
map2 = ["P", " ", " ", "|", " "]
map3 = [" ", "|", " ", "P", " "]
map4 = [" ", "P", "|", " ", " "]
map5 = [" ", " ", "P", " ", "|"]
playr_x = 4
playr_y = 1
dvig = ""
while True:
    print(playr_y, playr_y%5)
    if playr_y % 5 == 1:
        print(map1)
        map1[playr_x] = " "
        if playr_x == 0:
            playr_y += 1

    if playr_y % 5 == 2:

        print(map2)
        map2[playr_x] = " "
        if playr_x == 3:
            playr_y += 1

    if playr_y % 5 == 3:
        print(map3)
        map3[playr_x] = " "
        if playr_x == 1:
            playr_y += 1

    if playr_y % 5 == 4:
        print(map4)
        map4[playr_x] = " "
        if playr_x == 2:
            playr_y += 1

    if playr_y % 5 == 0:
        print(map5)
        map1[playr_x] = " "
        if playr_x == 4:
            playr_y += 1

    dvig = input("действие : ")

    if dvig == "a":
        playr_x -= 1
    elif dvig == "d":
        playr_x += 1
    if playr_y %5 == 1:
        map1[playr_x] = "P"

    if playr_y % 5 == 2:
        map2[playr_x] = "P"

    if playr_y % 5 == 3:
        map3[playr_x] = "P"

    if playr_y % 5 == 4:
        map4[playr_x] = "P"

    if playr_y % 5 == 0:
        map5[playr_x] = "P"

    if playr_y % 5 == 1 & playr_y != 1:
        map1 = ["|", " ", " ", " ", "P"]
        map2 = ["P", " ", " ", "|", " "]
        map3 = [" ", "|", " ", "P", " "]
        map4 = [" ", "P", "|", " ", " "]
        map5 = [" ", " ", "P", " ", "|"]