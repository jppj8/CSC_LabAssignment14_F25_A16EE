file_obj = open("data2.txt", "r")
file_obj.write("Hellow, World!")
file_obj.close()
#You would see an error because we used the wrong open mode "r"
#In order to write a file, "w" or "a" should be used