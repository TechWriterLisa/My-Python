name = []
firstname = input('Enter first name: ')
name.append(firstname)

lastname = input('Enter Last name: ')
name.append(lastname)

print(name[1] + ' ' + name[0])

'''
Easy way
fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)

This is Not how you populate a list

name = []
name[0]='Lisa'
name[1] = 'Adams'
print(name[1] + ' ' + name[0])
'''
'''
#firstName=input('Enter your first name: ')
#lastName=input('Enter your last name: ')
#print(f'{lastName} {firstName}')
myList=[]
firstName=input('Enter your first name: ')
lastName=input('Enter your last name: ')
myList.append(lastName)
myList.append(firstName)
print(f'{myList[0]} {myList[1]}')
'''