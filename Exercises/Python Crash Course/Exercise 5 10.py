currentUsers=['admin', 'Lisa','Rita','Dan','Dee']
newUsers=['admin', 'Lisa','Sam','Boo','Tina']
#Convert Lists to Strings
currentUsers=' '.join(currentUsers)
newUsers=' '.join(newUsers)
#Change Strings to lower case
currentUsers=currentUsers.lower()
newUsers=newUsers.lower()
#Change Strings back to List
currentUsers=list(currentUsers.split(' '))
newUsers=list(newUsers.split(' '))
#Check to see if each newUser is in CurrentUsers
for count in range(len(newUsers)):
    if newUsers[count] in currentUsers:
        print('Enter a new username.')
    else:
        print('That username is available.')
#Check to see if each newUser is in CurrentUsers
for count in range(len(newUsers)):
    if newUsers(count) in currentUsers:
        print('Enter a new username.')
    else:
        print('That username is available.')
