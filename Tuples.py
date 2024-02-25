tup  = (1,  23 ,43 ,24,  53, "evergreen") # Tuple is unchangeable/immutable and it must requires a comma even if it contains single element.
print(tup[1:5])
print(tup)
print(type(tup), tup)
print(len(tup))

print(tup[1])
print(tup[3])
 
if "Evergreen" in tup:
     print("Yes Evergreen is present in Tup")
else:
    print("Evergreen is not present in Tup")
    
tup2 = tup[1:4]  # It will make another tuple
print(tup2)

countries = ("Pakistan", "India", "Italy", "Germany")
temp = list(countries) # New tuple
temp.append("Russia")
temp.pop(3) # remove item
temp[2]= "Finland"  # Replace
print(temp)

countries = tuple(temp)
print(countries)


one = ("Thailand", "Moscow", "Paris")
two = ("Islamabad", "Karachi", "Sukkur")

concate = one + two
print(concate)

counte = (1,4,6,2,7,1,6, 2 , 3 ,7,1,3)
res = counte.count(1)   # counts how many times particular number (in parenthesis) is repeated
res2 = counte.index(3) # index is used to locate the particular number/element/item (in parenthesis) where it is located(means on which number)
res3 = counte.index(3, 9, 20) # 3 is where located between number 9 to  20 in counte
print(res)
print(res2)
print(res3)
