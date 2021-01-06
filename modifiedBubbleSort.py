def bubbleSort(list):
    flag=True
    for i in range(len(list)):
        for j in range(len(list)-i-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
                flag=False
    return flag
string=input("Enter the number to be sorted ")
list=[int(x) for x in string.split()]
if bubbleSort(list):
    print("Already sorted ")
else:
    print("Not sorted and sorted array is ",list)