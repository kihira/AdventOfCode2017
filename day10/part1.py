# Not the best way but it works
def reverse(numbers: [], start: int, length: int):
    sublist = []
    for index in range(start, start + length):
        while index >= len(numbers):
            index -= len(numbers)
        sublist.append(numbers[index])
    sublist.reverse()
    subindex = 0
    for index in range(start, start + length):
        while index >= len(numbers):
            index -= len(numbers)
        numbers[index] = sublist[subindex]
        subindex += 1


with open("data.txt", "r") as file:
    curr_pos = 0
    skip_size = 0
    lengths = [int(entry) for entry in file.readline().strip().split(",")]
    numbers = [x for x in range(256)]

    for length in lengths:
        # reverse part of list, starting at curr_pos and going for length
        reverse(numbers, curr_pos, length)

        curr_pos += length + skip_size
        skip_size += 1
    print(numbers)
    print(numbers[0] * numbers[1])
