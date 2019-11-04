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