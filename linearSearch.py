def linearSearch(list,element):
    for i in range(len(list)):
        if list[i]==element:
            return True
    return False
string=input("Enter the number ")
list=[int(x) for x in string.split()]
if linearSearch(list,element=int(input('Enter the number to be search '))):
    print("Number found ")
else:
    print("Number not found ")