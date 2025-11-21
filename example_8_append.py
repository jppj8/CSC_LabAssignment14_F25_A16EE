# Please open "data3.txt" to see the file content
# There are 4 lines in the file, let's append one

file_obj = open("data3.txt", "a") # use mode "a" for append
file_obj.write("This is 5th line\n")
file_obj.write("This is 6th line")
file_obj.close()

#Please open "data3.txt" again after execution to see the file content
# It should have 6 lines now.