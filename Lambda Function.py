 # Lambda is a small anonymous function with no name.
twox = lambda x: x*2

print(twox(4))

cube = lambda x: pow(x, 3)
print(cube(3))

avg = lambda x , y , z: (x + y + z)/3
print(avg(5 , 3 , 10))

new = lambda x , y : print(f"{x} * {y} = {x*y}")
print(new(4 , 7))