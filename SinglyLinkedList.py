class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.start=None
    def insertion(self,data):
        newNode = Node(data)
        if self.start is None:
            self.start=newNode
        else:
            newNode.next=self.start
            self.start=newNode
    def is_empty(self):
        if self.start is None:
            print("linked list is empty ")
        else:
            print("List is not empty ")
    def deletion(self):
        if self.start.next is None:
            self.start=None
        else:
            self.start=self.start.next
    def traversal(self):
        if self.start is None:
            print("List is empty ")
        else:
            temp=self.start
            while temp is not None:
                print(temp.data,end=' ')
                temp=temp.next
object = LinkedList()
while True:
    print()
    print("1->Insertion at Front ")
    print("2->checking linked is empty or Not ")
    print("3->deletion at Front ")
    print("4->traversal ")
    print("5->To exit the program ")
    option = int(input("Enter the option "))
    if option==1:
        data = int(input("Enter the data "))
        object.insertion(data)
    elif option==2:
        object.is_empty()
    elif option==3:
        object.deletion()
    elif option==4:
        object.traversal()
    elif option==5:
        break
    else:
        print("Option wrong please enter correct option")
print("You are now out of program ")