ep1 = {122:69 , 98 : 76 , 76 : 54 , 120: 88}
ep2 = {35: 89 , 76: 91 , 43:64}

ep1.update(ep2)
print(ep1)
ep2.popitem()  # Removes last item from the dictionary(ep2)
print(ep2)
ep1.pop(98)  # Removes 98 from the dictionary ep1
print(ep1)

# del ep1 deletes whole dictionary
del ep2[76]  # Deletes only specific item
print(ep2)
ep1.clear()  # Empty dictionary/set
print(ep1)