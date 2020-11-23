"""B-17
Roll_no-16
Aniket kumar
singly_linked_list
Linked List is a linear data structure. Unlike arrays,
linked list elements are not stored at a contiguous location;
the elements are linked using pointers.
Node contain two parts one data and other next pointer which point to next node

 Application of singly Linked list are

 1) linked list is used for implementing stack and queue
 2) Linked Lists can also be used to represent Graphs
 3) Maintaining directory of names
 4) Dynamic memory allocation : We use linked list of free blocks.
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.start = None
    def insertion(self, data):
        newNode = Node(data)
        if self.start is None:
            self.start = newNode
        else:
            newNode.next = self.start
            self.start = newNode
    def insertionAtTail(self,data):
        newNode=Node(data)
        if self.start is None:
            self.start=newNode
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=newNode
    def insertionAtPos(self,pos,data):
        newNode=Node(data)
        if self.start is None:
            print('Linked list is empty ')
        else:
            i=1
            prev=self.start
            temp=self.start
            while True:
                prev=temp
                temp=temp.next
                if i==pos-1:
                    break
                i+=1
            prev.next=newNode
            newNode.next=temp
    def insertionAfterKey(self,key,data):
        newNode=Node(data)
        if self.start is None:
            print('list is empty ')
        else:
            temp=self.start
            prev=self.start
            while True:
                if temp.data==key:
                    break
                prev=temp
                temp=temp.next
            prev=temp
            temp=temp.next
            prev.next=newNode
            newNode.next=temp
    def insertionAtKey(self,key,data):
        newNode=Node(data)
        if self.start is None:
            print('list is empty ')
        else:
            temp=self.start
            prev=self.start
            while True:
                if temp.data==key:
                    break
                prev=temp
                temp=temp.next
            prev.next=newNode
            newNode.next=temp
    def is_empty(self):
        if self.start is None:
            print("linked list is empty ")
        else:
            print("List is not empty ")
    def deletion(self):
        if self.start.next is None:
            self.start = None
        else:
            self.start = self.start.next
    def deletionAtTail(self):
        if self.start is None:
            print('List is empty ')
        else:
            temp=self.start
            prev=self.start
            while temp.next is not None:
                prev=temp
                temp=temp.next
            prev.next=None
    def deletionAtKey(self,key):
        if self.start is None:
            print('List is empty ')
        else:
            temp=self.start
            prev=self.start
            while True:
                if temp.data==key:
                    break
                prev=temp
                temp=temp.next
            prev.next=temp.next
    def deletionAfterKey(self,key):
        if self.start is None:
            print('List is empty ')
        else:
            temp=self.start
            prev=self.start
            while True:
                if temp.data==key:
                    break
                prev=temp
                temp=temp.next
            prev=temp
            temp=temp.next
            prev.next=temp.next
    def deletionAtPos(self,pos):
        if self.start is None:
            print('list is empty ')
        elif pos==1:
            self.start=self.start.next
        else:
            temp=self.start
            prev=self.start
            i=1
            while True:
                if i==pos:
                    break
                prev=temp
                temp=temp.next
                i+=1
            prev.next=temp.next

    def traversal(self):
        if self.start is None:
            print("List is empty ")
        else:
            temp = self.start
            while temp is not None:
                print(temp.data,end=' ')
                temp = temp.next
object = LinkedList()
while True:
    print()
    print("1->Insertion at Front ")
    print("2->checking linked is empty or Not ")
    print("3->deletion at Front ")
    print("4->traversal ")
    print('5->insertion At tail ')
    print('6->insertion At given Position ')
    print('7->Insertion After key ')
    print('8->insertion at key ')
    print('9->deletion At tail ')
    print('10->deletion at key ')
    print('11->Deletion after key ')
    print('12->deletion at pos')
    print("Press Anything To exit the program ")
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
        data=int(input('Enter the data '))
        object.insertionAtTail(data)
    elif option==6:
        pos=int(input('Enter the position '))
        data=int(input('Enter the data '))
        object.insertionAtPos(pos,data)
    elif option==7:
        key=int(input('Enter the key '))
        data=int(input('Enter the data '))
        object.insertionAfterKey(key,data)
    elif option==8:
        key=int(input('Enter the key '))
        data=int(input('Enter the data '))
        object.insertionAtKey(key,data)
    elif option==9:
        object.deletionAtTail()
    elif option==10:
        key=int(input('ENter the key '))
        object.deletionAtKey(key)
    elif option==11:
        key=int(input('Enter the key '))
        object.deletionAfterKey(key)
    elif option==12:
        pos=int(input('enter the position '))
        object.deletionAtPos(pos)
    else:
        print("Exited")
        break
print("You are now out of program ")