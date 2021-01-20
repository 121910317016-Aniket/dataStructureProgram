class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CircularLinkedList:
    def __init__(self):
        self.start=None
    def insertion(self,data):
        newNode=Node(data)
        if self.start is None:
            self.start=newNode
            newNode.next=newNode
        else:
            temp=self.start
            while temp.next is not self.start:
                temp=temp.next
            temp.next=newNode
            newNode.next=self.start


    def traversal(self):
        if self.start is None:
            print("List is empty ")
        else:
            temp=self.start
            while temp.next is not self.start:
                print(temp.data,end=' ')
                temp=temp.next
            print(temp.data)
    def isEmpty(self):
        if self.start is None:
            print("circular linked list is empty ,Try to insert some element ")
        else:
            print('There are elements in CLL ')
    def deletion(self):
        if self.start is None:
            print('list is empty ')
        else:
            Old_starting=self.start
            self.start=self.start.next
            curr=self.start
            while curr.next is not Old_starting:
                curr=curr.next
            curr.next=self.start
object=CircularLinkedList()
while True:
    print()
    print('1->Insertion ')
    print('2->Traversal ')
    print('3->IsEmpty ')
    print('4->Deletion ')
    print('Press Anything to Exit the Program')
    option = int(input('Enter the option '))
    if option==1:
        data=int(input('Enter the data '))
        object.insertion(data)
    elif option==2:
        object.traversal()
    elif option==3:
        object.isEmpty()
    elif option==4:
        object.deletion()
    else:
        print('Thank You ')
        break
