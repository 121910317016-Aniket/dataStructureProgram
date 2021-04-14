sum=30
def solve(s,index,mylist,list):
    if s>sum:
        return
    if s==sum:
        hasSolution=True
        displaySolutionSet(mylist)
        #hasSolution = False
        return
    for i in range(index,len(list)):
        mylist.append(list[i])
        solve(s+list[i],i+1,mylist,list)
        mylist.pop()
def displaySolutionSet(mylist):
    for i in range(len(mylist)):
        print(mylist[i],end=' ')
    print()
list=[10, 7, 5, 18, 12, 20, 15]
hasSolution=False
mylist=[]
solve(0,0,mylist,list)

