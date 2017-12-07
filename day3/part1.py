from math import sqrt

num = int(input("Input: "))
count = 0

while not sqrt(num).is_integer():
    num -= 1
    count += 1

print(num)
print(count)
print(f"Steps: {format(sqrt(num) - 1 + count)}")
