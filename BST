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
            self.start=Node(data)
        else:
            self._insert(data,self.start)
        return self.start
    def _insert(self,data,curr):
        if data<curr.data:
            if curr.left is None:
                curr.left=Node(data)
            else:
                self._insert(data,curr.left)
        elif data>curr.data:
            if curr.right is None:
                curr.right=Node(data)
            else:
                self._insert(data,curr.right)
        else:
            print('Duplicate are not allow ')
    def search(self,data):
        if self.start is None:
            print('Empty ')
        else:
            if self._search(data,self.start):
                print('Element found ')
            else:
                print('Not found ')
    def _search(self,data,curr):
        if data==curr.data:
            return True
        elif data<curr.data and curr.left:
            return self._search(data, curr.left)
        elif data>curr.data and curr.right:
            return self._search(data, curr.right)
    def minValueNode(self,root):
        current = root
        # loop down to find the leftmost leaf
        while (current.left is not None):
            current = current.left

        return current
    def deletion(self,root,data):
        if root is None:
            return
        if data<root.data:
            root.left=self.deletion(root.left,data)
        elif data>root.data:
            root.right=self.deletion(root.right,data)
        else:
            if root.left is None:
                temp=root.right
                root=None
                return temp
            elif root.right is None:
                temp=root.left
                root=None
                return temp
            else:
                temp=self.minValueNode(root.right)
                root.data=temp.data
                root.right=self.deletion(root.right,data)
        return root




bst = BST()
bst.insert(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
root=bst.insert(10)
bst.deletion(root,8)
print(bst.search(8))
