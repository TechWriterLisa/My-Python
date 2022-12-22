myList=[1,2,3,4,5,6,7,8,9]
for count in range(9):
    if myList[count]==1:
         print(str(myList[count]) + 'st' + '\n')
    elif myList[count]==2:
         print(str(myList[count]) + 'nd' + '\n')
    else:
        print(str(myList[count]) + 'th' + '\n')
