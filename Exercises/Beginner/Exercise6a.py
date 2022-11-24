NumGroup=[]
while True:
    print('Enter numbers' + '(or enter nothing to stop.):')
    info=input()
    if info=='':
        break
    NumGroup=NumGroup + [info]
print('List:' + str(NumGroup))
NumGroup=tuple(NumGroup)
print('Tuple:',NumGroup)
