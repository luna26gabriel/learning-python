friends = [("Anna Flavia", 11, 20),
           ("Raissa", 21, 50),
           ("Anthonny", 30, 20),
           ("Helena", 21, 15),
           ("Davi", 20, 23)]

age = lambda data:data[1] >= 18

drink_buddies = list(filter(age, friends))

for i in drink_buddies:
    print(i)