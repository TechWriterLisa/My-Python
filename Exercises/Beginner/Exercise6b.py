myList=[]
while True:
   print('Enter a series of numbers or nothing to stop:')
   num=input()
   if num =='':
       break
   myList=myList + [num]
print(f'List: {myList} Tuple: {tuple(myList)}')   