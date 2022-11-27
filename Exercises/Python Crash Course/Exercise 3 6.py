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
    print(f'{invitesList[count]}, you are invited to dinner.')