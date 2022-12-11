'''
newCar=''
car='Hyundai'
input(newCar)
print(car==newCar)
'''

'''
car='Hyundai'
print(car.islower())
'''

myList=['small']
age='fifteen'
newAge='twenty'
newAge1='fifteen'
newAge2=15
newAge3=20
newAge4=40
print(f'Question 1a: {age==newAge}')
print(f'Question 1b: {age==newAge1}')
print(f'Question 2: {age.islower()}')
print(f'Question 3a: {newAge2==newAge3}')
print(f'Question 3b: {newAge2!=newAge3}')
print(f'Question 3c: {newAge2 < newAge3}')
print(f'Question 3d: {newAge2 > newAge3}')
print(f'Question 4: {(newAge2 < newAge3) and (newAge4 > newAge3)}')
print(f'Question 4: {(newAge2 < newAge3) or (newAge4 > newAge3)}')
print('small' in myList)
print('big' in myList)
