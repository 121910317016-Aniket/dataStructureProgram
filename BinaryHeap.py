class MaxHeap:
    def __init__(self):
        self.heap=[]
    def insertion(self,data):
        self.heap.append(data)
        i=len(self.heap)-1
        while i>0:
            parent=int((i-1)/2)
            if self.heap[parent]<self.heap[i]:
                self.heap[parent],self.heap[i]=self.heap[i],self.heap[parent]
                i=parent
            else:
                return

    def view(self):
        print(self.heap)
    def delete(self):
        element=self.heap.pop(0)
        self.heap.insert(0,self.heap.pop())
        i=0
        while True:
            left=2*i+1
            right=(2*i)+2
            if left>=len(self.heap) and right>=len(self.heap):
                return
            if len(self.heap)==1:
                self.heap.pop()
            if right>=len(self.heap):
                if self.heap[left]>self.heap[i]:
                    self.heap[left],self.heap[i]=self.heap[i],self.heap[left]
                    i=left
                else:
                    return
            elif left>=left(self.heap):
                if self.heap[right]>self.heap[i]:
                    self.heap[right],self.heap[i]=self.heap[i],self.heap[right]
                    i=right
                else:
                    return
            else:
                if self.heap[left] > self.heap[right] and self.heap[left] > self.heap[i]:
                    self.heap[left], self.heap[i] = self.heap[i], self.heap[left]
                    i = left
                elif self.heap[right] > self.heap[left] and self.heap[right] > self.heap[i]:
                    self.heap[right], self.heap[i] = self.heap[i], self.heap[right]
                    i = right
                else:
                    return





h=MaxHeap()
h.insertion(32)
h.insertion(31)
h.insertion(43)
h.insertion(76)
h.view()
