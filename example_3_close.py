file_obj = open("data1.txt", "r")
file_obj.close()

#The following line yield an error because the file is already closed
print(file_obj.read())
