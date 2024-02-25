dic = {"name": "Waheed", "age" : 20, "Eligible": True}     # First values means ("name", "age" and so on) are known as keys.

print(dic.get("name2")) # says None if it is not present in Dictionary
print(dic.keys())
print(dic.items()) # Gives everything
print(dic.values())  # prints values of keys
# print(dic["name2"]) Throws error because it is used when we want our program to throw error.

for key in dic.keys():
    print(f"The value corresponding to the key {key} is {dic[key]}")  # prints the value of keys..

for key, value in dic.items():
    print(f"The value corresponding to the key {key} is {value}")
    