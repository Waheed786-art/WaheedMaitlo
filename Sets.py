s = {1 , 2 , 3 , 4 , 5 , 6}  # set is defined with Braces/Curly Brackets.
print(type(s), s)

s2 = {2 ,2 , 3, 3 , 1, 4, 5 , 6, 5} # it'll remove duplicate items/elements because set cannot contain duplicate items. And sets are unchangeable/immutable. Furthermore sets don't guarantee order maintainenance.
print(s2)

info = {"Carla", 19 , 5.9 , False , 19}
print(info)

harry = set()  # For making empty set
print(type(harry))

for value in info:  # For in sets
    print(value)