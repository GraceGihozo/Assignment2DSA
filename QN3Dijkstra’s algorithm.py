inf = float("inf")
#source
start = "C"


graph={
      'C': {'B': 5, 'E': 22, 'F': 30},
      'B': {'D': 17, 'A': 13, 'E': 20, 'C': 5, 'F': 18},
      'F': {'C': 30, 'B': 18},
      'E': {'B': 20, 'C': 22},
      'D': {'A': 10, 'B': 17},
      'A' : {'D': 10, 'B': 13}


}


# dict_empty for cost = {}
costs = {}
parents ={}
for node in graph:
    Stop = node
    costs[node] = inf
    parents[node] = {}
costs[start] = 0
# Find which vertex is to be visited next
def find_cheapest_node(costs, not_checked):
    lowest_cost = inf
    cheapest_node = ""
    for node in costs:
        if node in not_checked and costs[node] <= lowest_cost:
            lowest_cost = costs[node]
            cheapest_node = node

    return cheapest_node

if __name__ == "__main__":
    not_checked = [node for node in costs]
    node = find_cheapest_node(costs, not_checked)
    while not_checked:
        print(f"Not Checked:{not_checked}")
        cost = costs[node]
        child_cost = graph[node]
        # Updating new distances
        for c in child_cost:
            if costs[c]> cost+ child_cost[c]:
                costs[c] = cost+child_cost[c]
                parents[c] = node

        not_checked.pop(not_checked.index(node))
        node = find_cheapest_node(costs, not_checked)
    print(f"The shortest path from C and costs to each vertices: {costs}")
    print(f"The cost to go from {start} to {Stop} is {costs[Stop]}!")

    #Print the path
    if costs[Stop] < inf:
        path = [Stop]
        i = 0
        while start not in path:
            path.append(parents[path[i]])
            i += 1

        print(f"The shortest path is {path[::-1]}")

    else:
        print("A path could not be found")










