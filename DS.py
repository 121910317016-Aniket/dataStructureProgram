def dijkartaAlgorithm(mylist,l):
    INF = 32678
    distance=[]
    distance.append(0)
    for i in range(1,l):
        distance.append(INF)
    visited = [False]*(l)
    count=0
    u=0
    while True:
        list = []
        for v in range(l):

            if distance[u] + mylist[u][v] < distance[v] and mylist[u][v] != 0 and visited[v] is False:
                distance[v] = distance[u] + mylist[u][v]
                list.append(v)
        visited[u] = True
        min=INF
        index=0
        for i in range(len(list)):
            if min>distance[list[i]]:
                min=distance[list[i]]
                index=list[i]
        u=index
        count+=1
        if count==l:
            break
    for i in range(l):
        print("i {} distance {} ".format(i,distance[i]))
mylist=[[0,2,4,0,0,0],
        [0,0,1,7,0,0],
        [0,0,0,0,3,0],
        [0,0,0,0,0,1],
        [0,0,0,2,0,5],
        [0,0,0,0,0,0]
]
dijkartaAlgorithm(mylist,6)
