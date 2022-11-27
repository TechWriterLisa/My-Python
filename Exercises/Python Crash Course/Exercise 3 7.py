invitesList=['Lisa Adams', 'Dee Adams', 'Rita Adams', 'Dan Adams']
for count in range(len(invitesList)):
    print(f'{invitesList[count]}, you are invited to dinner.')
print("Lisa Adams can't attend.")
invitesList[0]='Denise Adams'
for count in range(len(invitesList)):
    print(f'{invitesList[count]}, you are invited to dinner.')
print("I found a bigger table.")
invitesList.insert(1,'Pam')
invitesList.insert(3,'Milli')
invitesList.append('Mom')
for count in range(len(invitesList)):
    print(f'{invitesList[count]}, You are invited to dinner.')   
print("Sorry guys, that table won't arrive in time. I can only invite 2 people.")
for count in range(5):
    item=invitesList.pop(0)
    print(item + ", You can't attend.")
for count in range(len(invitesList)): 
    print(f'{invitesList[count]}, You are still invited.')
del invitesList[0]
del invitesList[0]
print(invitesList)
