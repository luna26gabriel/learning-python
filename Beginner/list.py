# #  LIST
# food = ["pizza", "hamburguer", "milkshake"]

# print(food[1])

# print(len(food))

# food.append("sushi") / Acrecentar
# food.remove("pizza") / Remover
# food.pop() / Remove the last element
# food.insert(0, "cake") / Acresenta no index informado
# food.sort() / Ordem alfabetica
# food.clear() / Remove os elementos


# for i in food:
#     print(i)


# #  2D list
# drinks = ["coffe", "soda", "water"]
# dinner = ["pizza", "hamburguer"]
# dessert = ["cake", "ice cream"]

# food = [drinks, dinner, dessert]

# print(food[1][0])



# #  TUPLE
# student = ("Luna", 21, "male")
# print(student.count("Luna"))
# print(student.index("male"))

# for x in student:
#     print(x)

# if "Lun" in student:
#     print("Luna esteve aqui")




# # #  SET - array sem ordenação, não aceita repetidos e sem index
# utensils = {"fork", "spoon", "knife"}
# dishes = {"bowl", "plate", "cup", "knife"}

# # utensils.add("napkin")
# # utensils.remove("fork")
# # utensils.clear()

# # utensils.update(dishes)
# # dinner_table = utensils.union(dishes)

# # print(dishes.difference(utensils))
# print(utensils.intersection(dishes))

# # for x in dinner_table:
# #     print(x)




# # Dictionary - semelhante ao SET mas possui key:value

# capitals = {'MG':'Belo Horizonte',
#             'SP':'São Paulo',
#             'BA':'Salvador'}

# capitals.update({'RJ':'Rio de Janeiro'})
# capitals.update({'SP':'Sei la'})
# capitals.pop('SP')
# capitals.clear()

# print(capitals['MG'])
# print(capitals.get('MG'))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

# for key, value in capitals.items():
#     print(key, value)



# # INDEX OPERATOR
# name = "sr Luna!"
# if(name[0].islower()):
#     name = name.capitalize()

# first_name = name[:2].upper()
# last_name = name[3:].lower()
# last_Character = name[-1]


# print(first_name + " " + last_name)
# print(last_Character)
