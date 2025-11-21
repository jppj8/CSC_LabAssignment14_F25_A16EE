file_obj = open("data1.txt", "r")
content = file_obj.read()


#You would see the entire poem "The Zen of Python"
#You can open the file "data1.txt" to see it.
print(content)

#Remember top close the file after file manipulation
file_obj.close()