class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class DoublyLinkedList:
    def __init__(self):
        self.start=None
    def insertionAtFirst(self,data):
        if self.start is None:
            self.start = Node(data)
        else:
            newNode=Node(data)
            self.start.left=newNode
            newNode.right=self.start
            self.start=newNode
    def insertionAtLast(self,data):
        if self.start is None:
            self.start = Node(data)
        else:
            temp=self.start
            while temp.right is not None:
                temp=temp.right
            newNode=Node(data)
            newNode.left=temp
            temp.right=newNode
    def insertionAtkey(self,key,data):
        if self.start is None:
            print("Linked list is empty ")
        else:
            temp=self.start
            prev=self.start
            while key!=temp.data:
                prev=temp
                temp=temp.right
            newNode=Node(data)
            temp.left=newNode
            newNode.right=temp
            newNode.left=prev
            prev.right=newNode
    def deletionAtFirst(self):
        if self.start is None:
            print("NO DATA ")
        else:
            self.start.right.left=None
            self.start=self.start.right
    def deletionAtLast(self):
        if self.start is None:
            print("No data ")
        else:
            temp=self.start
            while temp.right.right is not None:
                temp=temp.right
            temp.right = None
    def deletionAtKey(self,key):
        if self.start is None:
            print("Linked list is empty ")
        else:
            temp=self.start
            prev=self.start
            while key!=temp.data:
                prev=temp
                temp=temp.right
            prev.right=temp.right
            temp.right.left=prev

    def viewNode(self):
        if self.start is None:
            print("Linked list is empty ")
        else:
            temp=self.start
            while temp is not None:
                print(temp.data,end = ' ')
                temp=temp.right


ob=DoublyLinkedList()
while True:
    print("\n1->insertion at begining ")
    print("2->insertion at the end ")
    print("3->insertion at the key ")
    print("4->viewNode ")
    print("5->deletion at first ")
    print("6-> deletion at last ")
    print("7->deletion at the key ")
    option=int(input("Enter the option "))
    if option == 1:
        ob.insertionAtFirst(int(input("Enter the data ")))
    elif option == 2:
        ob.insertionAtLast(int(input('Enter the data ')))
    elif option == 3:
        ob.insertionAtkey(int(input("Enter the key ")),int(input("Enter the data ")))
    elif option == 4:
        ob.viewNode()
    elif option == 5:
        ob.deletionAtFirst()
    elif option == 6:
        ob.deletionAtLast()
    elif option == 7:
        ob.deletionAtKey(int(input("Enter the key ")))
    else:
        print("wrong choice ")
