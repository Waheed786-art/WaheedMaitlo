from functools import reduce
# Objective = Make the number negative
# 1st Method
def make_negative(number):
    return -number if number>0 else number

print(make_negative(-34))
# 2nd Method
def mak_negative(num):
    return -abs(num)
print(mak_negative(199))

# 3rd Method
def ne_negative(nu):
    if nu >= 0:
        return -nu
    else:
        return nu
print(ne_negative(-7))

# 4th Method

def no_negative(no):
    if no < 0:
        return no
    else:
        return no * -1
print(no_negative(-87))

# 5th Method

def nm_negative(nm):
    return nm if nm <= 0 else -nm

print(nm_negative(-7))

a = 56
print("a is between 0 to 10") if a >= 0 and a<=10 else print("a is between 10 to 20") if a>=10 and a <= 20 else print("I don't know!")


g = [2 , 5 ,1 ,7, 9, 0]
for index, ge in enumerate(g , start=1):
    print(ge)
    if index == 3:
        print("Awesome Program!")
        
with open("file.txt" , 'r') as a:
    print(type(a))
    a.seek(10)  # starts after 10
    print(a.tell()) # tells us about number.
    data = a.read(10) # Reads specific number of bytes.
    print(data)
    
with open("sample.txt" , 'w') as f:
    f.write("Hi Buddy!")
    f.truncate(5)  # truncate means specific number of characters written in parenthesis.
    
with open("sample.txt" , 'r') as j:
    print(j.read())
    

with open("sample1.txt", 'w') as k:
    k.write("What's up bruhhh")
    k.truncate(10)
with open("sample1.txt", 'r') as l:
    b = l.read()
    print(b)
    
two = lambda x: pow(x, 3)
print(two(2))

avg = lambda x, y ,z: (x+y+z)/3
print(avg(3 , 5 ,4))

new = lambda fx , value: 6+(fx * value)
print(new(two(4) ,3))

j = 8
for i in range(10):
    y = lambda j , i:j*i
    i+=1
    print(f"{j} x {y(1,i)} = {y(j , i)}")
    # i+=1
    # print(f"{j} x {i} = {i*j}")
    
    
def cube(x):
    return x*x*x

o = [1 , 4 , 7, 1 ,8]
newl = []
for item in o:
    newl.append(cube(item))
print(newl)

t = list(map(lambda x : x*x*x , o))
print(t)
    
# Using Filter
def function_filter(x):
    return x > 2

w = list(filter(function_filter,o))
print(w)
    
def red(x):
    return x>6

te = list (filter(red, o))
print(te)

# Using Reduce
def reduc(x , y):
    return x+y

yr = reduce(reduc, o)
print(yr)

# Using map
def ma(x):
    return x*x*x

ui = list(map(ma, o))
print(ui)

uy = "Waheed"
io = uy[::-1]
print(io)

class One():
    Movie = "Mission Impossible"
    Release = 2023
    Genre = "Action"
    Hero = "Tom Cruise"
    def info(self):
        print(f"The name of the movie is {self.Movie}, the hero is {self.Hero}, movie is released in {self.Release} and the genre of the movie is {self.Genre}.")
o = One()
o.info()
print(o.Movie)   
  
lp = [2 , 4 ,1 , 7, 9] 
def oop(x, y):
    return x+y

t = reduce(oop, lp)
print(t)

def greater(x):
    return x>2
y = list(filter(greater, lp))
print(y)

ti = list(map(lambda x: x*x*x, lp))
print(ti)


class Person():
    # Name = "Waheed"            Without using these I can user Dundar Method(__init__)
    # Occupation = "Developer"
    def __init__(self ,name ,occ):  # __init__ is known as Dundar Method which is special kind of method to use in classes efficiently. With only self argument then it'll be said as Default Constructor.
        self.name = name
        self.occupation = occ
        # print(f"{self.name} is a {self.occupation}") init only return none so only print can be used.
    def info(self):
        print(f"{self.name} is a {self.occupation}")
    
a= Person("Waheed" , "Developer")   # Self argument is already passed so we can't initialize anything in self.
b= Person("Naveed" , "Civil Engineer")
a.info()


