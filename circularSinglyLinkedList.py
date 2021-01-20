class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CircularLinkedList:
    def __init__(self):
        self.start = None
    def insertionAtFirst(self,data):
        if self.start is None:
            self.start = Node(data)
        else:
            newNode=Node(data)
            self.start.right=newNode
            newNode.right=self.start
            self.start=newNode
    def insertionAtLast(self,data):
        if self.start is None:
            self.start=Node(data)
        else:
            newNode=Node(data)
            temp=self.start
            while temp.next is not self.start:
                temp=temp.next
            temp.next=newNode
            newNode.next=self.start
    def insertionAtKey(self,key,data):
        if self.start is None:
            print("Linked list is empty ")
        else:
            temp=self.start
            prev=self.start
            while temp.data!=key:
                prev=temp
                temp=temp.next
            newNode=Node(data)
            newNode.next=temp
            prev.next=newNode
    def deletionAtFirst(self):
        if self.start is None:
            print("Linked list is empty ")
        else:
            temp1=self.start
            self.start=self.start.next
            temp=self.start
            while temp.next is not temp1:
                temp=temp.next
            temp.next=self.start
    def deletionAtLast(self):
        if self.start is None:
            print("Linked list is empty ")
        else:
            store=self.start
            temp=self.start
            while temp.next.next is not store:
                temp=temp.next
            temp.next=store
    def deletionAtkey(self,key):
        if self.start is None:
            print("already empty ")
        else:
            temp=self.start
            prev=self.start
            while key!=temp.data:
                prev=temp
                temp=temp.next
            prev.next=temp.next
    def viewNode(self):
        if self.start is None:
            print('linked list is empty ')
        else:
            prev=self.start
            temp=self.start
            while temp.next is not self.start
                print(prev.next,end=' ')
                prev=temp
                temp=temp.next
            print(prev.next.data)
ob=CircularLinkedList()
while True:
    print('\n1->insertion at first ')
    print('2->insertion at the key ')
    print('3->insertion at key ')
    print('4->deletion at first ')
    print('5->deletion at end ')
    print('')