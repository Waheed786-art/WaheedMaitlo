
marks = [98 , 56 , 47 , 86]

for index, mark in enumerate(marks , start = 1):  # prints Hello everyone before index no. 3
    print(f"{index+1}: {mark}")
    if index == 3:
        print("Hello Everyone!")
        
        
x = ( 1 , 2 , 3 , 4)
new = list(map(lambda x:x*x*x , x))
print(new)

cube = [3 , 2 ,7 , 9]
newl = []
for item in cube:
    newl.append(pow(item , 3))
print(newl)

def function_name(x):
    return x > 6

a = (2 , 5, 8, 3 ,7 , 9 , 10)

new = list(filter(function_name , a))
print(new)

b = 3 

newk = lambda b : b*b
print(newk(3))

from functools import reduce

d = [3 , 2 ,6 ,5]
def mymulti(x , y):
    return x/y

e = reduce(mymulti , d)
print(e)

f = 2

match f:
    case 1:
        print("1 is stored in F")
    case 2:
        print("2 is stored in F")
    case 3:
        print("3 is stored in F")
    case 6:
        print(f)
    case _:
        print("F is not equal to 2")
    

i = 4
print("Hello") if i == 2 else print("HI") if i == 1 else print("What's up!") if i == 3 else  print("Nothing")



h = "Waheed Ahmed Maitlo"
j = h.replace(" ","")
print(j)

k = "WaheedMaitlo"
y = k[-5: -1]
print(y)

u = "Sajid"
i = u[::-1]
print(i)

o = "Waheed"
print(o[::-1])

se = [ 2, 3 , 5, 7 , 0 , 10 ]
uet = (3 , 5 ,1 ,9 , 12 , 9)
re = se.index(7) # to locate any number.
re2 = se.count(9)
se[1] = 8
uet1 = uet[3]
print(re)
print(uet1)
print(re2)

oi = se[-2::-1]
oi2 = [1 , 4 ,2]
oi1 = [32 , 13 , 15 , 87]
print(oi2+oi+oi1)