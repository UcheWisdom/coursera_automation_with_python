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

# os.remove("./novel.txt")
# os.remove("./novel.txt")

os.rename("./spider_renamed.txt", "./spider.txt")

os.path.exists("./spider_renamed.txt")