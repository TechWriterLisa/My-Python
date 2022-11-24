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
