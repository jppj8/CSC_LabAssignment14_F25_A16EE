#create a file object of file "data1.txt", with mode "r" which is "read"
file_object = open("data1.txt", "r")
print(file_object)

#You will see an error "FileNotFoundError" since file "data101.txt" not exist
file_object_error = open("data101.txt", "r")
print(file_object_error)