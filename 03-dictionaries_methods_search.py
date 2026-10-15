user = {"name": "Ricardo", "age": 29, "greet": "Hola Mundo", "numbers": [1, 2, 3]}

print(user["name"])

# .get()
print(user.get("name"))

# in
print("name" in user)  # solo busca keys
print("name" in user.keys())  # usa esto en default
print("name" in user.values())
