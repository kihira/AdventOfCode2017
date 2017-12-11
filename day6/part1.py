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
cycles = 1
flag = False
banks = input("Banks: ").split("\t")
for index in range(len(banks)):
    banks[index] = int(banks[index])
prevBanks.append(banks)

while not flag:
    banks = distribute(banks)

    # Check if we've seen this configuration before
    for prevBank in prevBanks:
        if prevBank == banks:
            print(prevBanks)
            print(prevBank)
            print(cycles)
            flag = True
            break
    prevBanks.append(banks)
    cycles += 1
