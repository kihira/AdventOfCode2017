def is_anagram(word1: str, word2: str):
    chars = {}
    for char in word1:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    for char in word2:
        if char not in chars:
            return False
        if chars[char] == 0:
            return False
        chars[char] -= 1
    for count in chars.values():
        if count != 0:
            return False
    return True


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
            for existing_word in words:
                if is_anagram(existing_word, word):
                    flag = True
                    break
            if flag:
                break
            words[word] = True
        print(words)
        if not flag:
            valid += 1

    print(valid)
