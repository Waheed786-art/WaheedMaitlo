def Gmean(a,b):  # def is used for Function
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a, b):
    if(a>b):
        print("First number is greater")
    else:
        print("Second number is greater")
def isLesser(a,b):
    if(b<a):
        print("Second number is lesser")
    else:
        print ("First number is lesser")
def isEqual(a,b):
    pass;  # means leave this for a while   and process the program after pass


a = 30
b = 20
Gmean(a , b) # First Method 
Gmean(10,30) # Second Method
isGreater(a,b)
isGreater(20,40)
isLesser(a,b)
isLesser(20,40)


