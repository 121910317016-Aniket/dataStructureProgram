 # Using a Python dictionary to act as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# graph = dict()
# graph[0] = [1, 2]
# graph[1] = [0, 3, 4]
# graph[2] = [0, 5, 6]
# graph[3] = [1]
# graph[4] = [1]
# graph[5] = [2]
# graph[6] = [2]

visited = set()  # Set to keep track of visited nodes.


def dfs(visited, graph, node):
    if node not in visited:
        print(node,end=' ')
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


# Driver Code
dfs(visited, graph, 'A')
#dfs(visited, graph, 0)
