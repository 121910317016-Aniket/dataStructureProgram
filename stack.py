"""B-17
Roll no-16
Aniket kumar
stack implementation
"""
"""Stack is a linear data structure which follows a particular order in which the operations are performed.
   The order may be LIFO(Last In First Out) or FILO(First In Last Out).
   stack can be implemented either by list or linked list
   
  Application of stack are:-

  1) Stacks can be used for expression evaluation.
  2) Stacks can be used to check parenthesis matching in an expression.
  3) Stacks can be used for Conversion from one form of expression to another.
  4) Stacks can be used for Memory Management.
  5) Stack data structures are used in backtracking problems.
"""
class stack:
    def __init__(self,limit):
        self.stack = []
        self.top = -1
        self.limit=limit
    def isEmpty(self):
        if self.top == -1:
            print("Stack is empty ")
        else:
            print("Stack has some data ")
    def isFull(self):
        if self.top == self.limit-1:
            print("stack is Full ")
        else:
            print("stack is not full ")
    def push(self,data):
        if self.top == self.limit-1:
            print("stack is Full ")
            return
        self.stack.append(data)
        self.top+=1
    def pop(self):
        if self.top == -1:
            print("stack is empty can't operate pop operation ")
        else:
            self.stack.pop()
            self.top = self.top-1
    def peek(self):
        if self.top == -1:
            print('stack is empty ')
        else:
            print('Top element of stack is {} '.format(self.stack[self.top]))
limit=int(input('Enter the size of stack '))
object=stack(limit)
while True:
    print()
    print('1->isEmpty ')
    print('2->isFull ')
    print('3->Push ')
    print('4->Pop ')
    print('5->peek ')
    print('PRESS Anything To exit program ')
    option = int(input('Enter the option '))
    if option == 1:
        object.isEmpty()
    elif option == 2:
        object.isFull()
    elif option == 3:
        data=int(input('Enter the data '))
        object.push(data)
    elif option == 4:
        object.pop()
    elif option == 5:
        object.peek()
    else:
        print('Thank You ')
        break