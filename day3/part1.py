num = int(input("Input: "))
count = 0
squareLength = 3

while squareLength * squareLength < num:
    squareLength += 2
squareLength -= 2
cornerValue = squareLength * squareLength
diff = num - cornerValue

midPoint = (squareLength + 1) / 2
# # Walk right one
# diff += 1
# # Walk north
# if squareLength > diff:
#     diff = diff - midPoint
# else:
#     diff -= squareLength
# # Walk west
# if squareLength + 1 > diff:
#     diff = diff - midPoint
# else:
#     diff -= squareLength + 1
# # Walk South
# if squareLength + 1 > diff:
#     diff = diff - midPoint
# else:
#     diff -= squareLength + 1
# # Walk East
# if squareLength + 1 > diff:
#     diff = diff - midPoint

print(squareLength)
print(cornerValue)
print(diff)
print(midPoint)
