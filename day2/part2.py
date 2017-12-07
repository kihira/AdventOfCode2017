with open("part2.txt", "r") as file:
    checksum = 0
    for row in file:
        numbers = []
        for entry in row.split("\t"):
            numbers.append(int(entry))
        shouldBreak = False
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if i == j:
                    continue
                if numbers[i] % numbers[j] == 0:
                    checksum += numbers[i] / numbers[j]
                    shouldBreak = True
                    break
            if shouldBreak:
                break
    print(checksum)
