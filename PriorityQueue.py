class Queue:
    def __init__(self):
        self.queue=[]
    def printf(self):
        return ' '.join([str(i) for i in self.queue])
    def isEmpty(self):
        return len(self.queue) == 0
    def insertion(self,data):
        self.queue.append(data)
    def delete(self):
        max=0
        for i in range(len(self.queue)):
            if self.queue[i]>self.queue[max]:
                max=i
        item=self.queue[max]
        del self.queue[max]
        return item
q=Queue()
q.insertion(12)
q.insertion(1)
q.insertion(14)
q.insertion(7)
print(q.printf())
while not q.isEmpty():
    print(q.delete())
