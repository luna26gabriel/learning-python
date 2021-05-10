# squares = []
# for i in range(1, 11):
#     squares.append(i * i)
# print(squares)

# squares = [i * i for i in range(1,11)]
# print(squares)


stundents = [100,90,80,70,60,50,40,30,20,10]
# passed = list(filter(lambda x: x >= 60, stundents))

# passed = [i for i in stundents if i >=60]
passed = [i if i >= 60 else "failed" for i in stundents]
print(passed)