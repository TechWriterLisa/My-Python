### * **3-5** You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.

### 1. Start with your program from Exercise 3-4. Add a print statement at the end of your program stating the name of the guest who can’t make it.
### 2. Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
### 3. Print a second set of invitation messages, one for each person who is still in your list.

invitesList=['Lisa Adams', 'Dee Adams', 'Rita Adams', 'Dan Adams']
for count in range(len(invitesList)):
    print(f'{invitesList[count]}, you are invited to dinner.')
print("Lisa Adams can't attend.")
invitesList[0]='Denise Adams'
for count in range(len(invitesList)):
    print(f'{invitesList[count]}, you are invited to dinner.')
