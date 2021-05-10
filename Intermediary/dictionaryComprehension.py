# capitals_C = {'BH': 20,'SP': 25,'SV': 34,'RJ': 30}

# # (°C * 1.8) + 32 = °F
# capitals_F = {key: ((value * 1.8) + 32) for (key,value) in capitals_C.items()}
# print(capitals_F)

# --------------------------------------------------
# weather = {'BH':"limpo", 'Sp':"nublado", 'SV':"ensolarado", 'Rj':"ensolarado"}
# ensolarados = {key: value for (key,value) in weather.items() if value == "ensolarado"}
# print(ensolarados)

# --------------------------------------------------
# capitals_C = {'BH': 20,'SP': 25,'SV': 34,'RJ': 30}
# desc = {key: ("Frio" if value <= 26 else "Quente") for (key,value) in capitals_C.items()}
# print(desc)

# --------------------------------------------------
capitals_C = {'BH': 20,'SP': 25,'SV': 34,'RJ': 30}
def check_temp(value):
    if value <= 26:
        return "Frio"
    else:
        return "Quente"
desc_c = {key: check_temp(value) for (key,value) in capitals_C.items()}
print(desc_c)

