for i in range(6):
    print(i)
    if (i == 4):
        print("No 4")
        continue 
    
else:
    print("Sorry no i")  # if else is printed means loop ended successfully
    
j = 0;

while (j<6):
    print(j)
    j = j+1
    if (j == 5):
        break   # means loop is broken it'll not print further part of loop
else :
    print("Sorry no j")
    
    
for x in range(5):
    print("iteration no {} in for loop".format(x+1))
else:
    print("else block in loop")
print("Out of Loop")