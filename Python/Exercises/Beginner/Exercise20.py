'''
def larger_string(str, n):
   result = ""
   for i in range(n):
      result = result + str
   return result

print(larger_string('abc', 2))
print(larger_string('.py', 3))
'''

def answer(str, n):
# Set result equal to an empty string & set to true.    
    result = ""

    for count in range(n):
        result = result + str
    return result

# print(answer('abc', 2))
# print(answer('.py', 3))

part1 = input("Enter a string: ")
part2 = input("Enter quantity: ")
part2 = int(part2)

print(answer(part1,part2))
