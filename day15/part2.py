total = 0


def generatorA():
    genA = 634
    while True:
        genA = (genA * 16807) % 2147483647
        if genA % 4 == 0:
            yield genA & 0xFFFF


def generatorB():
    genB = 301
    while True:
        genB = (genB * 48271) % 2147483647
        if genB % 8 == 0:
            yield genB & 0xFFFF


A = generatorA()
B = generatorB()

for i in range(5000000):
    if A.__next__() == B.__next__():
        total += 1

print(total)
