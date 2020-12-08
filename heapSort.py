class MaxHeap:
    def __init__(self):
        self.heap=[]
        self.sort=[]
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
        print('Heap Sort:',end=' ')
        print(self.sort)
    def delete(self):
        while True:
            element = self.heap.pop(0)
            self.sort.append(element)
            if len(self.heap) > 0:
                self.heap.insert(0, self.heap.pop())
                i = 0
                while True:
                    left = 2 * i + 1
                    right = (2 * i) + 2

                    if left >= len(self.heap) and right >= len(self.heap):
                        break
                    if right >= len(self.heap):
                        if self.heap[left] > self.heap[i]:
                            self.heap[left], self.heap[i] = self.heap[i], self.heap[left]
                            i = left
                        else:
                            break
                    elif left >= len(self.heap):
                        if self.heap[right] > self.heap[i]:
                            self.heap[right], self.heap[i] = self.heap[i], self.heap[right]
                            i = right
                        else:
                            break
                    else:
                        if self.heap[left] > self.heap[right] and self.heap[left] > self.heap[i]:
                            self.heap[left], self.heap[i] = self.heap[i], self.heap[left]
                            i = left
                        elif self.heap[right] > self.heap[left] and self.heap[right] > self.heap[i]:
                            self.heap[right], self.heap[i] = self.heap[i], self.heap[right]
                            i = right
                        else:
                            break
            else:
                break







h=MaxHeap()
h.insertion(32)
h.insertion(31)
h.insertion(43)
h.insertion(76)
h.delete()
h.view()
