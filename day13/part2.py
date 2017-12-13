with open("data.txt", "r") as file:

    firewall = {}
    severity = 0
    for row in file:
        layer, depth = list(map(int, row.strip().split(": ")))
        firewall[layer] = depth

    delay = 0
    flag = True
    while flag:
        flag = False
        for layer in firewall:
            if (layer + delay) % ((firewall[layer] - 1) * 2) == 0:
                delay += 1
                flag = True
                break

    print(delay)
