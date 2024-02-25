a = int(input("Enter your age: "))

print("Your age is:",a)
# Conditional Operators    <,>,<=,>=,==,!=
if (a>=18):
    print("You can drive") # Space before print is known as indentation.
elif(a<18):
    print("You cannot drive") 
else:
    print("You are still a child")
    
applePrice = int(input("Enter the price of 1kg of Apples: "))
budget = int(input("Enter your budget: "))

if(applePrice<=budget):
    print("You can buy")

elif(applePrice>budget):
    print("You cannot buy")
    
elif(budget-applePrice>=50):
    print("It's okay you can still buy")
else:
    print("You cannot buy")

if (budget-applePrice>0):
    print("Your remaining money is:",budget-applePrice)
elif (budget-applePrice<0):
    print("You need more money:",applePrice-budget)



no = int (input("Enter the number: "))

if (no < 0):
    print("The number is negative")

elif(no>0):
    if(no<=10):
        print("The number is between 1-10")
    elif(no<=20):
        print("The number is between 1-20")
    elif(no<=30):
        print("The number is between 1-30")
else:
    print("Number is zero")