def bubbleSort(list):
    for i in range(len(list)):
        for j in range(len(list)-1-i):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
string=input("Enter the number to be sorted ")
list=[int(x) for x in string.split()]
bubbleSort(list)
print('After sorting ',list)