with open("part1.txt", "r") as file:
    checksum = 0
    for row in file:
        large, small = 0, 9999
        for entry in row.split("\t"):
            entry = int(entry)
            if entry > large:
                large = entry
            if entry < small:
                small = entry

        checksum += large - small
    print(checksum)
