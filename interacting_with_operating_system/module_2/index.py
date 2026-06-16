file =open("./spider.txt")
print(file.readline())

file.close()

with open("spider.txt") as file:
    print(file.readline())