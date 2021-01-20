class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class DoublyLinkedList:
    def __init__(self):
        self.start=None
    def insertion(self,data):
        newNode=Node(data)
        if self.start is None:
            self.start=newNode
        else:
            temp=self.start
            temp.left=newNode
            newNode.right=temp
            self.start=newNode
    def deletion(self):
        if self.start is None:
            print('List is empty ')
        else:
            self.start.right.left=None
            self.start=self.start.right
    def deletionAfterKey(self,key):
        if self.start is None:
            print('list is empty ')
        elif self.start.data==key:
            temp=self.start
            prev=self.start
            prev.right = temp.right.right
            temp.right.left = prev
        else:
            prev=self.start
            temp=self.start
            while True:

                if temp.data==key:
                    break
                prev = temp
                temp = temp.right
            if temp.right is None:
                print('No element are there')
            elif temp.right.right is None:
                temp.right=None
            else:
                prev.right.right = temp.right.right
                temp.right.left = prev.right

    def deletionBeforeKey(self,key):
        if self.start is None:
            print('list is empty ')
        elif self.start.data==key:
            print('No element before it ')
            return
        elif self.start.right.data==key:
            temp=self.start.right
            temp.left=None
            self.start=temp
        else:
            prev=self.start
            temp=self.start
            pos=1
            temp1=self.start
            while True:
                if temp1.data==key:
                    break
                pos+=1
                temp1=temp1.right

            j=1
            while True:
                if j==pos-1:
                    break
                prev=temp
                temp=temp.right
                j+=1
            prev.right=temp.right
            temp.right.left=prev
    def deletionAtPos(self,ps):
        if self.start is None:
            print('list is empty ')
        elif self.start.right.right is None:
            self.start.right=None
        else:
            temp=self.start
            prev=self.start
            i=1
            while True:
                if i==ps:
                    break
                prev=temp
                temp=temp.right
                i+=1
            prev.right=temp.right
            temp.right.left=prev

    def traversal(self):
        if self.start is None:
            print('List is empty ')
        else:
            temp=self.start
            while temp is not None:
                print(temp.data,end=' ')
                temp=temp.right
            print()
    def reverseTraversal(self):
        if self.start is None:
            print('List is empty ')
        else:
            temp = self.start
            while temp.right is not None:
                temp=temp.right
            while temp is not None:
                print(temp.data,end=' ')
                temp=temp.left
            print()
    def isEmpty(self):
        if self.start is None:
            print('list is empty')
        else:
            print('Not empty')
    def peek(self):
        if self.start is None:
            print('list is empty ')
        else:
            temp=self.start
            while temp.right is not None:
                temp=temp.right
            print('peek element is {} '.format(temp.data))
Object = DoublyLinkedList()
while True:
    print('1->insertion ')
    print('2->deletion ')
    print('3->traversal ')
    print('4->reverseTraversal ')
    print('5->isEmpty ')
    print('6->peek ')
    print('7->deletion after key ')
    print('8->deletion Before key ')
    print('9->deletion at Position ')
    print('Press anything to exit program ')
    option=int(input('Enter the option '));''
    if option==1:
        data=int(input('Enter the data '))
        Object.insertion(data)
    elif option==2:
        Object.deletion()
    elif option==3:
        Object.traversal()
    elif option==4:
        Object.reverseTraversal()
    elif option==5:
        Object.isEmpty()
    elif option==6:
        Object.peek()
    elif option==7:
        key=int(input('Enter the key '))
        Object.deletionAfterKey(key)
    elif option==8:
        key=int(input('Enter the key '))
        Object.deletionBeforeKey(key)
    elif option==9:
        ps = int(input('Enter the position '))
        Object.deletionAtPos(ps)
    else:
        break

