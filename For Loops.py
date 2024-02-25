name = "Asfandyar"
for i in name:
    print(i)
    if(i=='A'):
        print("This is only for A")
    elif(i=='d'):
        print("This is only for d")
        
colors = ["Red", "Blue" , "Orange", "Green"] # Square bracket means List
print(type(colors)) # List

for color in colors:
    print(color)
    for i in color:
        print(i)
# These were for Strings

for k in range(8):  # this is for integers  0-7
    print(k)
    print(k+1)
    
for t in range(1, 20):
    print(t)
    

for f in range(1, 12, 2):  # here 3rd number means difference b/w 1 to 12
    print(f)