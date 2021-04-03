
class Edge:
    def __init__(self,src,dstn,wt):
        self.src=src
        self.dstn=dstn
        self.wt=wt
    def __lt__(self, other):
        return self.wt<other.wt
class KrushkalAlgo:
    def __init__(self, vertix):
        self.v = vertix
    def findParent(self, parent, i):
        if parent[i] == -1:
            return i
        if parent[i] != -1:
            return self.findParent(parent, parent[i])

    def union(self, parent, x, y):
        parent[x] = y
    def Sort(self,List):
        List.sort(reverse=False)
    def isCyclic(self,List):
        parent=[-1]*(self.v)
        for i in List:
            x=self.findParent(parent,i.src)
            y=self.findParent(parent,i.dstn)
            if x==y:
                continue
            else:
                self.union(parent,x,y)
                MST.append(i)

MST=[]
List=[]
def AddEdge(src,dstn,wt):
    List.append(Edge(src,dstn,wt))
AddEdge(0, 1, 8)
AddEdge(0, 2, 5)
AddEdge(1, 2, 9)
AddEdge(1, 3, 11)
AddEdge(2, 3, 15)
AddEdge(2, 4, 10)
AddEdge(3, 4, 7)
k=KrushkalAlgo(5)
k.Sort(List)
k.isCyclic(List)
for i in MST:
    print("Edge {}-->{} and weight is {} ".format(i.src,i.dstn,i.wt))
#Edge 0-->2 and weight is 5 
#Edge 3-->4 and weight is 7 
#Edge 0-->1 and weight is 8 
#Edge 2-->4 and weight is 10 