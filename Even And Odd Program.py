
def even_or_odd():
    a = 21
    print("Even") if (a%2) == 0 else print("Odd") if (a%2) == 1 else print("")
    
even_or_odd()
    
    
a = 5
for i in range(0, 10):
    i+=1
    print(f"{a} x {i} = {a*i}")
    

from functools import reduce

def function_filter(x):
    return 5<x<10
g = (2 , 4 ,1 ,6 ,7 , 9 , 11 , 13)
h = list(filter(function_filter,g))
print(h)

numbers = (2 , 3 , 6 ,1)
def mysum(x, y):
    return x+y

a = reduce(mysum, numbers)
print(a)

l = (4 , 7 , 9 ,10 ,12)

b = list(map(lambda x: x*x*x , l))
print(b)

i = 0
while (i<=9):
    a = 6
    i += 1 
    print(f"{a} x {i} = {a*i}")
    
a = 234
b = 932
print(f"{a+b}")