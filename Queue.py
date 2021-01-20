# Python3 program for array implementation of queue 

# Class Queue to represent a queue 
class Queue:

    # __init__ function
    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.Q = [None] * capacity
        self.capacity = capacity

    # Queue is full when size becomes
    # equal to the capacity
    def isFull(self):
        return self.size == self.capacity

    # Queue is empty when size is 0
    def isEmpty(self):
        return self.size == 0

    # Function to add an item to the queue.
    # It changes rear and size
    def EnQueue(self, item):
        if self.isFull():
            print("Full")
            return
        self.rear = (self.rear + 1) % (self.capacity)
        self.Q[self.rear] = item
        self.size = self.size + 1
        print("% s enqueued to queue" % str(item))

    # Function to remove an item from queue.
    # It changes front and size
    def DeQueue(self):
        if self.isEmpty():
            print("Empty")
            return

        print("% s dequeued from queue" % str(self.Q[self.front]))
        self.front = (self.front + 1) % (self.capacity)
        self.size = self.size - 1

    def que_front(self):
        if self.isEmpty():
            print("Queue is empty")

        print("Front item is", self.Q[self.front])

        # Function to get rear of queue

    def que_rear(self):
        if self.isEmpty():
            print("Queue is empty")
        print("Rear item is", self.Q[self.rear])


queue = Queue(30)
while True:
    print('1->Enqueue ')
    print('2->dequeue ')
    print('3-> isEmpty ')
    print('4->isFull ')
    print('5->Rear item ')
    print('6->Front item')
    print('Press anything to exit Program')
    option = int(input('Enter the option '))
    if option==1:
        item=int(input('Enter the item '))
        queue.EnQueue(item)
    elif option==2:
        queue.DeQueue()
    elif option==3:
        if queue.isEmpty():
            print('Empty ')
        else:
            print('Not empty ')
    elif option==4:
        if queue.isFull():
            print('Full')
        else:
            print('Not full')
    elif option==5:
        queue.que_rear()
    elif option==6:
        queue.que_front()
    else:
        break


