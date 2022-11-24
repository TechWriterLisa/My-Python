'''number = input("Enter a positive number: ")
newNum = int(number)

if newNum > 17:
    print((newNum - 17) * 2)
else:
    print(17 - newNum)    
'''
#Using a function that I define.
def difference(num):
    if num <= 17:
        return 17 - num
    else:
       return (num - 17) * 2  

print(difference(22))
print(difference(14))

#10 & 3
"""def check(var):
    if var > 17:
        var=(var-17)
        var=var*2
        print('The integer is greater than 17:')
        print(var)
    elif var < 17:
        var=17 - var
        print('The integer is less than 17:')
        print(var)
    elif var == 17:
        print('The number is equal to 17.')
    else:
        print('Something broke.')            

num=input('Enter an integer number: ')
num=int(num)
check(num)"""
