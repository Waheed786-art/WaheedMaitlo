# Here a and b are mutable(changeable) b/c these are lists, so "is" is used for exact same means constant and "==" gives true if value of "a and b" is same
a = [2 , 3 , 45]
b = [2 , 3 , 45]

print(a is b) # Exact location of object in memory. for example if my mobile breaks then it doesn't mean that other mobiles with the same model break too.
print(a == b) # Value
 # here output will be true for both because c and d are tuple(constant) means these are immutable/unchangeable.
c = 4
d = 4
print (c is d)
print (c == d) 
 # here tuple is immutable means constant unchangeable so it will return true for both
e = ( 4 , 5)
f = ( 4 , 5)
print (e is f)
print (e == f) 

