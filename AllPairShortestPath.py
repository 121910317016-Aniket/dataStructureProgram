def FloydWarshallAlgorithm(graph):
    for i in range(4):
        for j in range(4):
            if j==i:
                continue
            for k in range(4):
                if k==i:
                    continue
                if graph[i][k]+graph[j][i]<graph[j][k]:
                    graph[j][k]=graph[i][k]+graph[j][i]



INF=32678
graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0,   1],
         [INF, INF, INF, 0]
         ]
FloydWarshallAlgorithm(graph)
for i in range(4):
    for j in range(4):
        print(graph[i][j],end=' ')
    print()