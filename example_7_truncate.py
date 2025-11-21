# Please open "data2.txt" to see the file content because it will be overwritten
file_obj = open("data2.txt", "w")

#Method 'write()' would overwrite the existing content of the file
file_obj.write("Hello World")
file_obj.write("!")

#There is no blank space between the written contents in above two lines

file_obj.close()

#Please open "data2.txt" again to see the file content