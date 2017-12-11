def distribute(data: []):
    input = data.copy()
    # Find bank with largest number of blocks
    largest = 0
    for index in range(len(input)):
        if input[index] > input[largest]:
            largest = index

    # Spread it out
    blocks = input[largest]
    input[largest] = 0
    pos = largest + 1
    while blocks > 0:
        if pos >= len(input):
            pos = 0
        input[pos] += 1
        blocks -= 1
        pos += 1
    return input


prevBanks = []
banks = list(map(int, input("Banks: ").split("\t")))

while banks not in prevBanks:
    prevBanks.append(banks)
    banks = distribute(banks)

print(prevBanks)
print(len(prevBanks))
print(len(prevBanks) - prevBanks.index(banks))
