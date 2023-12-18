import os,random
if os.path.isdir("C:\\Users\\vasil\\task 7.2.1")==False:
   os.mkdir("C:\\Users\\vasil\\task 7.2.1")
os.chdir("C:\\Users\\vasil\\task 7.2.1")
f = open("random.txt", "w")
x=int(input("Enter an integer number :"))

if isinstance(x,int)==True:
    for i in range(x):
      f = open("random.txt", "a")
      f.write(' '+str(random.randrange(0, 100)))
    f.close()
    f = open("random.txt", "r")
    print(f.read())
else:
   print("Not integer number")
