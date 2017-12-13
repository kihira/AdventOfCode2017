with open("data.txt", "r") as file:

    severity = 0
    for row in file:
        layer, depth = list(map(int, row.strip().split(": ")))
        if layer % ((depth - 1) * 2) == 0:
            severity += layer * depth

    print(severity)
