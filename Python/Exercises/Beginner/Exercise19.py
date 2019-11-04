def newString(str):
    if len(str) >= 2 and str[:2] == "Is":
        return str
    return "Is" + str

myString = input("Enter a string: ")
print(newString(myString))

#print(new_string("Array"))
#print(new_string("IsEmpty"))        
