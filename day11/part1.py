with open("data.txt", "r") as file:
    x, y, z, furthest = 0, 0, 0, 0

    for step in file.readline().strip().split(","):
        if step == "n":
            y += 1
            z -= 1
        elif step == "ne":
            x += 1
            z -= 1
        elif step == "se":
            x += 1
            y -= 1
        elif step == "s":
            y -= 1
            z += 1
        elif step == "sw":
            x -= 1
            z += 1
        elif step == "nw":
            y += 1
            x -= 1
        if (abs(x) + abs(y) + abs(z)) / 2 > furthest:
            furthest = (abs(x) + abs(y) + abs(z)) / 2
    print(furthest)
