studenst = ['Luna', 'Marcela', 'Helena', 'Lukinhas', 'Anna']

# studenst.sort()
# studenst.sort(reverse=True)
# for i in studenst:
#     print(i)

# sorted_students = sorted(studenst, reverse=True)

# for i in sorted_students:
#     print(i)


studenst = [('Luna', 21, 98), 
            ('Marcela', 21, 96), 
            ('Helena', 21, 78), 
            ('Lukinhas', 22, 78), 
            ('Anna', 11, 62)]

age = lambda ages: ages[1]
grade = lambda grades: grades[2]
# studenst.sort(key=grade)
sorted_students = sorted(studenst, key=grade, reverse=True)

for i in sorted_students:
    print("Name "+ str(i[0]) + ", Age : " + str(i[1]) + ", Grade: " + str(i[2]))