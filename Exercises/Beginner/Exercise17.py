'''
number = input("Enter a number from 1 to 2000: ")
number = int(number)
if (number < 2000) and (number > 1900):
    print("The number is within 100 of 2000.")
elif (number > 900) and (number < 1000):
    print("The number is within 100 of 1000")    
else:
    print("The number is not within 100 of 1000 or 2000.")    
    '''

#Using a function that I define
def myFun(number):
    return ((abs(1000 - number) <= 100) or (abs(2000 - number) <= 100))

print(myFun(900)) 
print(myFun(1900))