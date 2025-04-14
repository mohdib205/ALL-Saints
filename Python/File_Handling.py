'''
 Python supports file handling and
users to read and
 write files, along with many other file
handling options,
 to operate on files.
'''

##my_file=open("myFile.txt", mode="r")
##print(my_file.read())
##print(my_file.readline())
##print(my_file.readlines())
##
##print(my_file.closed)
##print(my_file.mode)
##my_file.close()
##print(my_file.closed)





'''
Differences:
read(): Reads the entire file as one big string.
readline(): Reads one line at a time and
returns it as a string.

readlines(): Reads the entire file but returns it
as a list of strings, with each string
representing one line.

When to Use:
Use read() when you need the whole content of the file
at once.
Use readline() when we want to read the file one
line at a time.
Use readlines() when we need all the lines but want
them as a list to process individually.

'''
##
###to write in the file we use "w" mode
##
##my_file=open("myFile.txt" , mode="w")
##my_file.write("This is Python Class")
##my_file.close()
##print(my_file.closed)
##
###append
##
###write mode overwrite the content in the file
###so to add more content in the file without overwriting
####the existing text we use "a" mode
##myfile= open("myFile.txt" , mode="a")
##myfile.write("\nThis is File Handling")
##myfile.close()
##
###to create a new file we use "x" mode
##
####new=open("newFile.txt", mode="x")
##new=open("newFile.txt", mode="w")
##new.write("This is the new File")
##new.close()


#using with keyword we dont need to close the file 
with open("newFile.txt", "r") as my_file:
    print(my_file.read())


with open("newFile.txt" , "a") as myfile:
    myfile.write("This is line 2")











