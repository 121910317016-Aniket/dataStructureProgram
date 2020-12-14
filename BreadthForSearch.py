def bfs(graph,node):
    queue.append(node)
    visited.append(node)
    while queue:
        s=queue.pop(0)
        print(s,end=' ')
        for nighbhour in graph[s]:
            if nighbhour not in visited:
                visited.append(nighbhour)
                queue.append(nighbhour)

queue=[]
visited=[]
graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}
bfs(graph,'A')