from functools import reduce
from operator import xor


def knot_hash(input: str):
    lens = [ord(x) for x in input]
    lens.extend([17, 31, 73, 47, 23])
    nums = [x for x in range(256)]
    pos = 0
    skip = 0
    for _ in range(64):
        for l in lens:
            to_reverse = []
            for x in range(l):
                n = (pos + x) % 256
                to_reverse.append(nums[n])
            to_reverse.reverse()
            for x in range(l):
                n = (pos + x) % 256
                nums[n] = to_reverse[x]
            pos += l + skip
            pos = pos % 256
            skip += 1
    dense = []
    for x in range(16):
        subslice = nums[16 * x:16 * x + 16]
        dense.append('%02x' % reduce(xor, subslice))
    return "".join(dense)


total = 0
for row in range(128):
    string = f"xlqgujun-{row}"
    total += sum(map(int, "{:0128b}".format(int(knot_hash(string), 16))))
print(total)
