genA = 634
genB = 301
total = 0

for i in range(40000000):
    genA = (genA * 16807) % 2147483647
    genB = (genB * 48271) % 2147483647
    if genA & 0xFFFF == genB & 0xFFFF:
        total += 1

print(total)
