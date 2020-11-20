class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.start=None
    def insert(self,data):
        if self.start is None:
            self.start =Node(data)
        else:
            self._insert(data,self.start)
    def _insert(self,data,curr_node):
        if data<curr_node.data:
            if curr_node.left is None:
                curr_node.left=Node(data)
            else:
                self._insert(data,curr_node.left)
        elif data>curr_node.data:
            if curr_node.right is None:
                curr_node.right=Node(data)
            else:
                self._insert(data,curr_node.right)
        else:
            print("Duplicate not allow ")
    def find(self,data):
        if self.start:
            is_found=self._find(data,self.start)
            if is_found:
                return True
            return False
        else:
            return None
    def _find(self,data,current):
        if data>current.data and current.right:
            return self._find(data,current.right)
        elif data<current.data and current.left:
            return self._find(data,current.left)
        if data==current.data:
            return True
bst = BST()
bst.insert(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)
if bst.find(2):
    print("present in the BST ")
else:
    print("Not present ")
