def partition(mylist,lb,ub):
    pivot = mylist[lb]
    start=lb
    end=ub
    while start<end:
        while mylist[start]<=pivot:
            start+=1
        while mylist[end]>pivot:
            end-=1
        if start<end:
            mylist[start],mylist[end]=mylist[end],mylist[start]
    mylist[lb],mylist[end]=mylist[end],mylist[lb]
    return end
def QuickSort(mylist,lb,ub):
    if lb<ub:
        loc=partition(mylist,lb,ub)
        QuickSort(mylist,lb,loc-1)
        QuickSort(mylist,loc+1,ub)
string=input("Enter the number to be sorted ")
mylist=[int(x) for x in string.split()]
QuickSort(mylist,0,len(mylist)-1)
print(mylist)
