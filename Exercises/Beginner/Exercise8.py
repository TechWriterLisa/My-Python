myList = ['Red', 'Green', 'White', 'Black']
print(myList[0] + ' and ' + myList[-1])

#Format Specifiers
#Old
#'%s %s' % ('one', 'two')
#New
#'{} {}'.format('one', 'two')

print('{} {}'.format(myList[0], myList[1]))

'''
color_list=[]
color_list = ["Red","Green","White" ,"Black"]
print(f'The first color is {color_list[0]} and the last color is {color_list[3]}')
'''