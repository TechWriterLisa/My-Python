### * **3-2** Greetings: Start with the list you used in 
# Exercise 3-1, but instead of just printing each person's 
# name, print a message to them. The text of each message 
# should be the same, but each message should be 
# personalized with the person's name. 
namesList=['lisa', 'rita', 'dan', 'dee']
for count in range(4):
    print(f'{namesList[count].title()}, Hello!')