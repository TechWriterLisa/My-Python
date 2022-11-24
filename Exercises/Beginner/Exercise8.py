myList = ['Red', 'Green', 'White', 'Black']
print(myList[0] + ' and ' + myList[-1])

#Format Specifiers
#Old
#'%s %s' % ('one', 'two')
#New
#'{} {}'.format('one', 'two')

print('{} {}'.format(myList[0], myList[1]))

