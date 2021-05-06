# import os

# path = "C:\\Users\\gabri\\Documents\\Udemy\\Python\\Beginner\\teste.txt"

# if os.path.exists(path):
#     print("That location exist!")
#     if os.path.isfile(path):
#         print("That is a file")
#     elif os.path.isdir(path):
#         print("That is a directory!")
# else:
#     print("That location doesn't exist!")

# # ==================
# # Abrindo files 
# try:
#     with open('test.txt') as myfile:
#         print(myfile.read())
# except FileNotFoundError:
#     print("That file was not found")
# print(myfile.closed)

# # ==================
# # Write a File
# text = "\nTexto com conteudo"
# with open('text.txt', 'a') as myfile:
#     myfile.write(text)

# # ==================
# # Copying files
# import shutil
# shutil.copyfile('text.txt', 'copy.txt') #src, dest

# # ==================
# # Moving Files
# import os 

# # source = "text.txt"
# # destination = "C:\\Users\\gabri\\Documents\\Udemy\\Python\\Destination\\destination.txt"

# source = "folder"
# destination = "C:\\Users\\gabri\\Documents\\Udemy\\Python\\Destination\\folder"

# try:
#     if os.path.exists(destination):
#         print("There is already a file there")
#     else:
#         os.replace(source, destination)
#         print(source + " was moved")
# except FileNotFoundError:
#     print(source + " was not found")

# # # ==================
# # Deleting Files
# import os
# import shutil
# try:
#     path = 'Destination\\folder'
#     # os.remove(path) #deleting folder
#     # os.rmdir(path)  #deleting a empty folder
#     shutil.rmtree(path) # perigoso
# except FileNotFoundError:
#     print("That file doesn't exist")
# except PermissionError:
#     print("You do not have permission to delete that")
# except OSError:
#     print(path + " was not empty")
# else:
#     print(path + " was deleted")