user = {"name": "Ricardo", "age": 29, "greet": "Hola Mundo", "numbers": [1, 2, 3]}

# .copy()

user_copy = user.copy()
user_copy["age"] = 20
# print(user)
# print(user_copy)

# .pop()
# user.pop("age")
# print(user)

# .popitem()     -elimina el ultimo elemento de una lista no ordenada
# user.popitem()
# print(user)

# .update()
user.update({"name": "Fernando"})  # si esta llave no existiese la crea
user.update({"cats": 2})
print(user)

# .append()
user["skills"] = user.get("skills", [])
user["skills"].append("Python")
user["skills"].append("Django")
print(user)
