class ObjectStoring:
    def __init__(self,id,deadLine,profit):
        self.id=id
        self.deadline=deadLine
        self.profit=profit
    def __lt__(self, other):
        return self.profit<other.profit
class JobSchedulingUsingGreedyApproch:
    def __init__(self,deadline):
        self.v=deadline+1
    def Sort(self,ival):
        ival.sort(reverse=True)
    def Algorithm(self,ival):
        slots=[[False,"JOB"]]*(self.v-1)
        for i in ival:
            k=i.deadline-1
            while k>=0:
                if slots[k][0] == False:
                    slots[k]=[True,i.id]
                    break
                else:
                    k-=1
        for i in range(len(slots)):
            if slots[i][0] == True:
                print(slots[i][1],end=' ')

Job=JobSchedulingUsingGreedyApproch(4)
ival = []
for i in range(4):
    ival.append(ObjectStoring(input("enter the IDs "), int(input("Enter the DeadLine ")),
                                      int(input("Enter the profit "))))
Job.Sort(ival)
Job.Algorithm(ival)