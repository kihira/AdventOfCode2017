from collections import defaultdict


with open("data.txt", "r") as file:
    graph = defaultdict(list)

    for row in file:
        data = row.strip().split(" ")
        vertex = int(data[0])
        for connected in [int(data[x].replace(",", "")) for x in range(2, len(data))]:
            graph[vertex].append(connected)
            graph[connected].append(vertex)

    groups = []
    for i in range(2000):
        queue = [i]
        connected = set()
        while queue:
            vertex = queue.pop()
            for adjacent in graph[vertex]:
                if adjacent not in connected:
                    connected.add(adjacent)
                    queue.append(adjacent)
        if connected not in groups:
            groups.append(connected)

    print(len(groups))
