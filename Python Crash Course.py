

a = "Waheed"
print(a)
b = a.replace("Waheed" , "Sajid")
print(b)

c = "Waheed ahmed maitlo"

print(c.title())
print(c.replace(" " , ""))

first_name = "naveed"
last_name = "ahmed"
full_name = "hello, " +first_name + " " +last_name + "!"
print(full_name.title())

rstr = "   Farhan Ahmed     "
rstr = rstr.rstrip()   # Skips spaces from right side
rstr = rstr.lstrip()   # skips spaces from left side
rstr = rstr.strip()    # skips spaces from both left and right side.
print(rstr)

# Lists

a = ["Ferrari" , "Civic" , "Corolla" , "Cultus"]
b = a.append("Alto") # adding element at the end
c = a.insert(3, "Audi")  # adding element in the list according to any index we want.
print(a)
del a[0]  # For deleting any element
print(a)

# Using Pop function
bikes = ["Yamaha" , "Honda CD" , "Unique" , "Crown"]
a_bikes = bikes.pop(1)   # pop kicks the element out of the list. like 1st index element in the list(bikes).
print(bikes)
print(a_bikes)   # the popped/kicked element.
print(f"The last motorbike I owned was a {bikes.pop(-1)}.")  # -1 means the last element if I leave it blank then it'll also print the last element.