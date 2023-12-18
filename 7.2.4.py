import os
if os.path.isdir("C:\\Users\\vasil\\task 7.2.1")==False:
 os.mkdir("C:\\Users\\vasil\\task 7.2.1")

os.chdir("C:\\Users\\vasil\\task 7.2.1")

class Person:

    def __init__(self, fname):
        self.name = fname

    def getName(self):
        return self.name

    def setName(self, new_name):
        self.name = new_name

    def printname(self):
        print(self.name)



filename1 = open("log.txt", "w")
filename1 = open("log.txt", "w")

pers=Person("Vasile Glodici")
pers1=Person("AAA")
pers.printname()
pers1.getName()
pers1.printname()

#pers1.name.getName()
pers1.printname()
filename1.writelines([pers.name, "\n"])
#pers.fname("Vasile Glodici")
#pers.printname()
filename1.close()
filename1 = open("log.txt", "r")
for x in filename1:
        print(x)