
# Estrutura do IF/ELSE/ELSE IF

# age = int(input("Age: "))
# if age == 21:
#     print("You have my age")
# elif age >= 18:
#     print("Adult")
# elif age <= 4:
#     print("Baby")
# else:
#     print("Child")

temp = int(input("What is the temperature outside? "))

and -> todas tem que ser positivas para ser positivo
or -> uma tem que ser positiva para ser positivo
not -> inverte o condição

if temp >= 0 and temp <= 30:
    print("the temperature is good, go outsite")
elif temp < 0 or temp > 30:
    print("the temperature is not good, stay inside")
