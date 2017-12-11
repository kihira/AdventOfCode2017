all_nodes = {}


def calc_weight(node):
    weight = node["weight"]
    if len(node["children"]) > 0:
        for child in node["children"]:
            weight += calc_weight(all_nodes[child])
    return weight


with open("part1.txt", "r") as file:
    # Load all nodes
    for row in file:
        data = row.split(" ")
        node = {"parent": None, "children": [], "weight": int(data[1].strip()[1:-1])}
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
    base_node = None
    for node in all_nodes:
        if all_nodes[node]["parent"] is None:
            base_node = all_nodes[node]
            break
    # Calc weight of children
    for child in base_node["children"]:
        print(f"{child} ({all_nodes[child]['weight']}): {calc_weight(all_nodes[child])}")
