#dictionary to act as an adjacency list
graph = {
    "C": ["B", "E", "F"],
    "B": ["A", "D", "E", "F"],
    "F": [],
    "E": [],
    "A": ["D"],
    "D": []

}
# Set to keep track of visited nodes.
visited = set()

def Depth_first_search(visited,graph, root):
    if root not in visited:
        print(root)
        visited.add(root)
        for neighbour in graph[root]:
            Depth_first_search(visited, graph, neighbour)

# Driver Code
print("The Depth-First Search ")
Depth_first_search(visited, graph, "C")