with open("part1.txt", "r") as file:
    valid = 0
    for row in file:
        words = {}
        flag = False
        for word in row.split(" "):
            word = word.strip()
            if word in words:
                flag = True
                break
            words[word] = True
        print(words)
        if not flag:
            valid += 1

    print(valid)
