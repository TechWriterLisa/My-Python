filename = input("Input the Filename: ")

extension = filename.split(".")

print ("The extension of the file is: " + str(extension[-1]))
print ('This is also the extension of the file:  ' + str(extension[1]))
print ('The name of the file is: ' + str(extension[0]))



