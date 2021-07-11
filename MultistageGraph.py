def multistageGraph():
    n=8
    stage=4
    cost=[]
    d=[]
    for i in range(8):
        cost.append(0)
        d.append(0)
    path = []
    for i in range(4):
        path.append(0)

    c=[[0, 1, 2, 5,0, 0, 0, 0],
         [0, 0, 0, 0, 4, 11, 0, 0],
         [0, 0, 0, 0, 9, 5, 16, 0],
         [0, 0, 0, 0, 0, 0, 2, 0],
         [0, 0, 0, 0, 0, 0, 0, 18],
         [0, 0, 0, 0, 0, 0, 0, 13],
         [0, 0, 0, 0, 0, 0, 0, 2]]
    
    for i in range(n-2,-1,-1):
        if i>=0:
            min=32757
            for k in range(i+1,n):
                if(c[i][k]!=0 and c[i][k]+cost[k]<min):
                    min=c[i][k]+cost[k]
                    d[i]=k
            cost[i]=min
    path[0]=0
    path[stage-1]=7
    for i in range(1,stage):
        path[i]=d[path[i-1]]
    for i in range(stage):
        print(path[i])
multistageGraph()
