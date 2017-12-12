with open("part1.txt", "r") as file:
    data = file.readline()

    ignore = False
    garbage = False
    score = 0
    curr_depth = 0
    removed = 0
    for char in data:
        if garbage:
            if ignore:
                ignore = False
                continue
            if char == "!":
                ignore = True
            elif char == ">":  # end garbage
                garbage = False
            else:
                removed += 1
        else:
            if char == "{":  # open group
                curr_depth += 1
                score += curr_depth
            elif char == "}":  # close group
                curr_depth -= 1
            elif char == "<":  # start garbage
                garbage = True
    print(score)
    print(removed)