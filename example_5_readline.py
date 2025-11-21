file_obj = open("data1.txt", "r")

#method 'readline()' would remember the position that has been read
#next ' readline()' would not return the same line

first_line = file_obj.readline() # first line of the file
second_line = file_obj.readline() # second line of the file
third_line = file_obj.readline() # third line of the file

print(first_line)
print(second_line) #second line is empty
print(third_line)
