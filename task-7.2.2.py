import os,random
#if os.path.isdir("C:\\Users\\vasil\\task 7.2.2")==False:
#  os.mkdir("C:\\Users\\vasil\\task 7.2.2")
os.chdir("C:\\Users\\vasil\\task 7.2.1")
filerandom = open("random.txt", "r")
x=filerandom.read()
x = x.split()
filerandom1 = open("random2.txt", "w")
filerandom1 = open("random2.txt", "a")
for x1 in x:
     filerandom1.writelines([x1,"\n"])
filerandom1.close()
filerandom1 = open("random2.txt", "r")
for x in filerandom1:
     print(x)




