# Заводим словарики

d = {
    "key": 123
}

maria = {
    "name": "Maria",
    "age": 18,
    "hobbies": []
}

oleg = {
    "name": "Oleg",
    "age": 18,
    "hobbies": []
}

users = [maria, oleg]


print(maria["name"])
print(maria["age"])
# print(maria["pets"])

# Функции словарей

print(maria.get("pets", "No pets"))
print(maria.get("name", "Default name"))


print(list(maria.keys()))
print(list(maria.values()))
print(list(maria.items()))
