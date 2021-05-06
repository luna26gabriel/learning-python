# WHILE LOOPs

# name = ""
# while len(name) == 0:

# name = None
# while not name:
#     name = input("Name: ")

# print("Hello: " + name)


#  FOR LOOPs
# import time
# for i in range(10):
#     print(i)

# for i in range(50, 100, 10):
#     print(i)

# for i in "SrLuna":
#     print(i)

# for seconds in range(10, 0, -1):
#     print(seconds)
#     time.sleep(1)
# print("Happy new year")


#  NESTED LOOP
# rows = int(input("How many rows:"))
# columns = int(input("How many columns:"))
# symbol = input("Enter a symbol to use:")

# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")
#     print()




#  LOOP CONTROL
# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break

# phone_number = "123-141-1245"

# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")

# for i in range(1, 21):
#     if i == 13:
#         pass
#     else:
#         print(i)

name = "Gabriel Luna"

for i in name:
    if i == " ":
        print()
        continue
    print(i, end="")