userNames=['admin', 'Lisa','Rita','Dan','Dee']
num = userNames.index('admin')
if userNames[num]:
        print('Hello admin, Would you like to see a status report?')
for count in range(len(userNames)): 
    if userNames[count] != userNames[0]:
        print(f'Hello, {userNames[count]}, Thank you for loggin in again.')
  