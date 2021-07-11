def multistageGraph():
    stages=4
    cost=[]
    d=[]
    for i in range(9):
        cost[i].append(0)
        d[i].append(0)
    path = []
    for i in range(5):
        path[i].append(0)

    c=[[0,0,0,0,0,0,0,0],
       [0,2,1,3,0,0,0,0],
       [0,0,0,0,2,3,0,0],
       [0,0,0,0,6,7,0,0],
       [0,0,0,0,6,8,0,0],
       [0,0,0,0,0,0,0,6],
       [0,0,0,0,0,0,0,4],
       [0,0,0,0,0,0,0,5]
    ]
    for i in range(n-1,-1):
        if i>=1:
            min=32757
            for k in range(i+1,n+1):
                if(c[i][k]!=0 and c[i][k]+cost[k]<min):
                    min=c[i][k]+cost[k]
                    d[i]=k
            cost[i]=min
    path[1]=1
    path[stage]=8
    for i in range(2,stage):
        p[i]=d[p[i-1]]
    for i in range(stage+1):
        print(p[i])
multistageGraph()
