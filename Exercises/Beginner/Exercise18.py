#Use a function that I define.
#return

def calcSum(numList):
  if myList[0] == myList[1] == myList[2]:
    sum1 = (myList[0] + myList[1] + myList[2]) * 3
    return sum1
  else:
    sum2 = (myList[0] + myList[1] + myList[2])
    return sum2
    
myList = [1, 1, 1]
print(calcSum(myList))