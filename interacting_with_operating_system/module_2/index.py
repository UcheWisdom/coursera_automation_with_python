# file =open("./spider.txt")
# print(file.readline())
# file.close()

# with open("./spider.txt") as file:
#     for line in file:
#         print(line.strip().upper())

# file = open("./spider.txt")
# lines = file.readlines()
# file.close()
# lines.sort()
# print(lines)

# with open("./novel.txt", "w") as file:
#     file.write(("It was a dark and stormy night"))

import os
import datetime
# os.remove("./novel.txt")
# os.remove("./novel.txt")

# os.rename("./spider_renamed.txt", "./spider.txt")

# os.path.exists("./spider_renamed.txt")

# #This code will provide the file size
# print(os.path.getsize("spider.txt"))

# #This code will provide a unix timestamp for the file unix timestamps
# print(os.path.getmtime("spider.txt"))

# #This code will provide the date and time for the file in an 
# #easy-to-understand format
# timestamp = os.path.getmtime("spider.txt")
# print(datetime.datetime.fromtimestamp(timestamp))


# #This code takes the file name and turns it into an absolute path
# print(os.path.abspath("spider.txt"))

#This code snippet returns the current working directory.
print(os.getcwd())


#The os.mkdir("new_dir") function creates a new directory called new_dir
os.mkdir("new_dir")

#This code snippet changes the current working directory to new_dir. 
#The second line prints the current working directory.
os.chdir("new_dir")
os.getcwd()


#This code snippet creates a new directory called newer_dir. 
#The second line deletes the newer_dir directory.
os.mkdir("newer_dir")
os.rmdir("newer_dir")

#This code snippet returns a list of all the files and 
#sub-directories in the website directory.
import os
os.listdir("website")

dir = "website"
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))

        
