def FloydWarshallAlgorithm(graph):
    for k in range(4):
        for i in range(4):
            for j in range(4):
                if i==j and k==i and k==j:
                    continue 
                else:
                    if graph[i][j]>graph[i][k]+graph[k][j]:
                        graph[i][j]=graph[i][k]+graph[k][j]
                      
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