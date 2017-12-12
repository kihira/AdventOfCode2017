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
    numbers = [x for x in range(256)]
    lengths = [ord(char) for char in file.readline().strip()]
    lengths.extend([17, 31, 73, 47, 23])
    for round in range(64):
        for length in lengths:
            # reverse part of list, starting at curr_pos and going for length
            reverse(numbers, curr_pos, length)

            curr_pos += length + skip_size
            while curr_pos >= len(numbers):
                curr_pos -= len(numbers)
            skip_size += 1

    # Calc sparse hash
    sparse_hash = []
    for block in range(16):
        number = numbers[block * 16]
        for i in range(1, 16):
            number ^= numbers[(block * 16) + i]
        sparse_hash.append(number)
    print(sparse_hash)

    # Calc hex
    output = ""
    for i in sparse_hash:
        output += format(i, "02x")
    print(output)
