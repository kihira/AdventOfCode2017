with open("part1.txt", "r") as file:
    all_nodes = {}
    # Load all nodes
    for row in file:
        data = row.split(" ")
        node = {"parent": None, "children": []}
        if len(data) > 3:
            for child in data[3:]:
                if child[-1] == ",":
                    child = child[:-1]
                child = child.strip()
                node["children"].append(child)
        all_nodes[data[0]] = node
    # Pair nodes with their parents
    for node_name in all_nodes:
        for child in all_nodes[node_name]["children"]:
            all_nodes[child]["parent"] = node_name
    # Find the node without a parent
    for node in all_nodes:
        if all_nodes[node]["parent"] is None:
            print(node)
            break
