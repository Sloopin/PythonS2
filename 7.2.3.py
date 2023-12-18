import os
if os.path.isdir("C:\\Users\\vasil\\task 7.2.1")==False:
 os.mkdir("C:\\Users\\vasil\\task 7.2.1")

os.chdir("C:\\Users\\vasil\\task 7.2.1")

filename1 = open("file_username.txt", "w")
filename1 = open("file_username.txt", "a")
print("For exit enter empty name")
username = input("Enter username:")
while username != "":
    filename1.writelines([username, "\n"])
    username = input("Enter username:")
filename1.close()
filename1 = open("file_username.txt", "r")
for x in filename1:
        print(x)

