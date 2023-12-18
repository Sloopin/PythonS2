import os

print(os.getcwd())

os.chdir("C:\\Users\\vasil\\PythonFilesTest2")

print(os.getcwd())

print(os.listdir("C:\\Users\\vasil\\PythonFilesTest2"))

os.mkdir("C:\\Users\\vasil\\PythonFilesTest2\\new folder for python")

os.chdir("C:\\Users\\vasil\\PythonFilesTest2\\new folder for python")

os.mkdir("C:\\Users\\vasil\\PythonFilesTest2\\new folder for python\\my second folder")

os.chdir("C:\\Users\\vasil\\PythonFilesTest2\\new folder for python\\my second folder")

#os.rmdir("C:\\Users\\vasil\\PythonFilesTest2\\new folder for python\\my second folder") #have to change to parent directory 1st

os.chdir("C:\\Users\\vasil\\PythonFilesTest2")

print(os.getcwd())

os.rmdir("C:\\Users\\vasil\\PythonFilesTest2\\new folder for python\\my second folder")