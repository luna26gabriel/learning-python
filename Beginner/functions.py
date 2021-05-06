# def hello(first_name, last_name):
#      print("Hello " + first_name + " " + last_name)
#      print("Have a nice a day")

# # hello("Gabriel")
# # hello("Luna")
# first_name = "Gabriel"
# last_name = "Luna"
# hello(first_name, last_name) 

#=============================
# # return functions
# def sum(num1, num2):
#     return num1 + num2

# res = sum(1, 6)
# print(res)

#================================
# # key arguments
# def hello(first, middle, last):
#     print("Hello: " + first + " " + middle + " " + last)

# hello(first="Gabriel", last="Luna", middle="Sr")

#=============================
# # Nasted function calls
# num = input("Enter a positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

# print(round(abs(float(input("Number: ")))))

# #=====================
# # SCOPE
# def display_name():
#     name = "Luna"
#     print(name)

# print(name) #Erro 
# display_name()

#===================
# ARGS
# def add(*args):
#     sum = 0
#     args = list(args)
#     args[0] = 0
#     for i in args:
#         sum += i
#     return sum

# print(add(1, 2, 6))

# #=================
# # KWARGS
# def hello(**kwargs):
#     # print("Hello " + kwargs['first'] + " " + kwargs['last'])
#     print("Hello", end=" ")
#     for key, value in kwargs.items():
#         print(value, end=" ")

# hello(first="Gabriel", last="Luna", title="Sr.")









