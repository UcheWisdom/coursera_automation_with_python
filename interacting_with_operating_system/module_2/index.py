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

#This code will provide the file size
print(os.path.getsize("spider.txt"))

#This code will provide a unix timestamp for the file unix timestamps
print(os.path.getmtime("spider.txt"))

#This code will provide the date and time for the file in an 
#easy-to-understand format
timestamp = os.path.getmtime("spider.txt")
print(datetime.datetime.fromtimestamp(timestamp))


#This code takes the file name and turns it into an absolute path
print(os.path.abspath("spider.txt"))
