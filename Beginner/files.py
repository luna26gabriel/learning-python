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

with open('test.txt') as myfile:
    print(myfile.read())

print(myfile.closed)