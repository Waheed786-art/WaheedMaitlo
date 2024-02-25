# Order doesn't matter in Sets.

s1 = {6 , 7 , 8 , 9 ,10}
s2 = {1, 2 ,3 ,4 ,5}
s1.update(s2)
print(s1.union(s2))
print(s1, s2)

cities1 = {"Karachi", "Lahore", "Sukkur","Hyderabad"}
cities2 = {"Karachi", "Panoaqil" , "Larkana", "Sukkur"}
cities3 = cities1.union(cities2)
cities4 = cities1.intersection(cities2)
cities5 = cities1.difference(cities2)
print(cities3)
print(cities4)
print(cities5)
cities1.intersection_update(cities2)
print(cities1)


countries1 = {"Pakistan" , "India" , "Afghanistan"}
countries2 = {"Russia" , "Thailand" , "Singapore"}
countries3 = countries1.isdisjoint(countries2)
print(countries3)

bigcities1 = {"Moscow", "Bangkok", "Kuala Lumpur" , "Jakarta" , "Dushanbe" , "Santiago"}
bigcities2 = {"Moscow", "Bangkok", "Kuala Lumpur"}
bigcities2.add("Santiago")
bigcities3 = bigcities1.issuperset(bigcities2)
bigcities4 = bigcities2.issubset(bigcities1)
print(bigcities3)
print(bigcities4)



a = {1 , 2 ,3 , 4 ,5 }
b = {6 , 7 ,  8 ,9 ,10 }
a.update(b)
print(a)

a2 = {21 , 22 ,23 ,24 ,25,26}
# a2.remove(27) Error because 27 is not present in a2
a2.discard(27) # discard method doesn't throw error even if the element is not present in the set but if it is present then it'll remove it from the set(a2).
print(a2)

d = bigcities1.pop() # pop method will pop means takes out any of the element in set(bigcities1).
print(d)

e = {"Riyadh" , "Abu Dhabi" , "Kabul" , "Cairo" , "Athens" , "Damascus"}
del(e)
# print(e) # throws an error because "e" is already deleted.