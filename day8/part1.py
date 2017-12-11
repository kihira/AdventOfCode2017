overall_largest = 0
registers = {}


def change_value(register: str, instruction: str, change: int):
    if register not in registers:
        registers[register] = 0
    if instruction == "inc":
        registers[register] += change
    else:
        registers[register] -= change
    global overall_largest
    if registers[register] > overall_largest:
        overall_largest = registers[register]


def get_value(register: str):
    if register in registers:
        return registers[register]
    else:
        return 0


with open("part1.txt", "r") as file:
    for row in file:
        row = row.strip().split(" ")
        if (row[5] == ">" and get_value(row[4]) > int(row[6])) or \
                (row[5] == "<" and get_value(row[4]) < int(row[6])) or \
                (row[5] == ">=" and get_value(row[4]) >= int(row[6])) or \
                (row[5] == "<=" and get_value(row[4]) <= int(row[6])) or \
                (row[5] == "==" and get_value(row[4]) == int(row[6])) or \
                (row[5] == "!=" and get_value(row[4]) != int(row[6])):
            change_value(row[0], row[1], int(row[2]))
    largest = 0
    for register in registers:
        if registers[register] > largest:
            largest = registers[register]
    print(largest)
    print(overall_largest)
