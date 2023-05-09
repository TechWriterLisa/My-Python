''' Input 4 numbers Output a list with 4 numbers Output a tuple with 4
numbers 

outputlist=[]

count starts at 0 and will go up to but not include 4, so 0, 1, 2, 3.

for count in range(4):
    num=str(input('Enter number: '))
    outputlist.append(num)
  
print('Here is my list: ')
print(outputlist)
print()
print('Here is my tuple: ')
tupp = tuple([outputlist])
print(tupp)

'''
values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)
'''
This doesn't work because stop is a string and num is an integer.

outputlist=[]
stop = ''
num=0

while num !=stop:
    
    num=int(input('Enter number: '))

    outputlist.append(num)
print(outputlist)
'''
'''
NumGroup=[]
while True:
    print('Enter numbers' + '(or enter nothing to stop.):')
    info=input()
    if info=='':
        break
    NumGroup=NumGroup + [info]
print('List:' + str(NumGroup))
NumGroup=tuple(NumGroup)
print('Tuple:',NumGroup)
'''
'''
myList=[]
while True:
   print('Enter a series of numbers or nothing to stop:')
   num=input()
   if num =='':
       break
   myList=myList + [num]
print(f'List: {myList} Tuple: {tuple(myList)}')   

'''