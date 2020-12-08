class heapfy:
    def __init__(self):
        self.heap=[]
    def insertion(self,data):
        self.heap.append(data)
        i=len(self.heap)-1
        while i>0:
            parent=int((i-1)/2)
            left=2*parent+1
            right=(2*parent)+2
            if right>=len(self.heap):
                if self.heap[left]>self.heap[parent]:
                    self.heap[parent], self.heap[left] = self.heap[left], self.heap[parent]
                    i = parent
                else:
                    return
            elif left >= len(self.heap):
                if self.heap[right] > self.heap[parent]:
                    self.heap[parent], self.heap[right] = self.heap[right], self.heap[parent]
                    i = parent
                else:
                    return

            elif self.heap[left]>self.heap[right] and self.heap[left]>self.heap[parent]:
                self.heap[parent],self.heap[left]=self.heap[left],self.heap[parent]
                i=parent
            elif self.heap[right]>self.heap[left] and self.heap[right]>self.heap[parent]:
                self.heap[parent],self.heap[right]=self.heap[right],self.heap[parent]
                i=parent
            else:
                return
    def view(self):
        print(self.heap)
h=heapfy()
h.insertion(32)
h.insertion(31)
h.insertion(43)
h.insertion(76)
h.view()

