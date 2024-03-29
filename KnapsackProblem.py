class itemValue:
    def __init__(self,weight,profit):
        self.weight=weight
        self.profit=profit
        self.pw=profit/weight
    def __lt__(self, other):
        return self.pw<other.pw
class GreedyKnapSackProblem:
    def getMaxValue(self,weight,profit,capacity):
        ival=[]
        for i in range(len(weight)):
            ival.append(itemValue(weight[i],profit[i]))
        ival.sort(reverse=True)
        #for i in ival:
         #   print("profit {} weight {} pw {}".format(i.profit,i.weight,i.pw))
        totalValue = 0
        for i in ival:
            curwt=i.weight
            curval=i.profit
            if capacity-curwt>=0:
                capacity-=curwt
                totalValue+=curval
            else:
                fraction=capacity/curwt
                totalValue+=curval*fraction
                break
        return totalValue
knapsack=GreedyKnapSackProblem()
weight=[10,20,30]
profit=[60,100,120]
capacity = 50
maxValue=knapsack.getMaxValue(weight,profit,capacity)
print("Maximum value in Knapsack =", maxValue)