myPizzas=['Veggie', 'Cheese', 'Chicken']
for count in range(3):
    print(f'{myPizzas[count]} is my favorite pizza.')
print("I like all kinds of pizza.")
friend_pizzas=myPizzas[:]
myPizzas.append('Beef')
friend_pizzas.append('Pork')

#print(f' My favorite pizzas are: {myPizzas}')
for count in range(4):
    print(f'My favorite pizzas are: {myPizzas[count]}')

#print(f' My friend\'s favorite pizzas are: {friend_pizzas}')
for count in range(4):
    print(f'My friend\'s favorite pizzas are: {friend_pizzas[count]}')
