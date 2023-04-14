# when handling text files we have three basic options on how to use them. note there are more.
# we can either open a tex file to write "w" data to it, read "r" data from it or to append "a" data to it(add data to the end of the file).
# in order to do any of these a textfile must be opened first and once all operations with the textfile are over it must be closed.



# WRITING to a text-file

# we first open the file using the open function which takes as its first input a string with the name of the file and the
# -second a string with the method on how the file should be handled
# we assign this file to a variable which in this case will be called "File". this variable will be used when methods are called. 
File = open("newfile.txt", "w")
# one such method is "write", which takes in a parameter of what we want to be wrtiiten on the file.
File.write("this is the first line\n")
File.write("this is the second line\n")
File.write("this is the third line\n")
File.write("this is the fourth line\n")
File.write("this is the fifth line\n")



# APPENDING to a text-file

# appending to textfile simply means we add some new context to the very end of an existing textfile.
# if there is no file existing in the name given in the "open" function a new file will be created.
File = open("newfile.txt", "a")
File.write("this is an appended line of code\n")



# READING from a text-file

# we assign this file to a variable which in this case will be called "File". this variable will be used when methods are called. 
File = open("newfile.txt", "r")
# the "readline" method will read out one line at a time starting from the first line in the text file by returing that line of text
# the "readline" method will also return a new line after returning each line in the text-file
print(File.readline())
print(File.readline())
# the line of text can even be stored in a variable and used later
output = File.readline()
print(output)
# the "read" fuction will return the whole text file if called first or whatever the content of the textfile that 
# -hasn't been returned before
print(File.read())
# finally we MUST close the file we just used.
File.close()

print("======================================\n")

#  the main difference between append and write mode is that while append adds to a file, write will overwrite the whole file,
# deleting any previous content it had stored.

# since we may forget to close the file at times, we can open the file using "with". this eliminates the 
# -need to explicitly close the file once we are done using it

with open("newfile.txt", "w") as F:
    F.write("this is the new first line\n")
    F.write("this is the new second line\n")

with open("newfile.txt", "r") as F:
    print(F.read())
