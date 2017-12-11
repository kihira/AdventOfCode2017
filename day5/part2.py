with open("part1.txt", "r") as file:
    offsets = []
    for row in file:
        offsets.append(int(row.strip()))

    position = 0
    steps = 0
    while position < len(offsets):
        instruction = offsets[position]
        if instruction >= 3:
            offsets[position] -= 1
        else:
            offsets[position] += 1
        position += instruction
        steps += 1
    print(steps)
