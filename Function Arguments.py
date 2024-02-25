def average(a = 5 , b = 1): # variables inside the parenthesis are known as arguments  these are default argument type 
    print("The average is:", (a+b)/2)
    
average()
average(b = 21 , a = 9) # This is known as keyword Argument

def name(fname, mname = "Ahmed", lname = "Maitlo"):
    print("Hello,", fname, mname,lname)
    
name("Waheed")  # Waheed will automatically be initialized in fname..

def ave(*numbers): # Arbitrary Arguments
    sum =0
    for i in numbers:
        sum = sum + i
        print(sum)
    
    print("The average is ", sum/len(numbers))
    return sum/len(numbers)

c = ave (2, 4 , 6)    # used in return function only
print(c)
ave(5, 1)

def menu(*food):
    for foods in food:
        print(foods)
    
menu ("Pakore","Biryani","Samose")
