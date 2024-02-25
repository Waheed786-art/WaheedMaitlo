a = (input("Enter the number between 5 and 9: "))


# if(a == int and int(a)<5 or int(a)>9):

#     raise ValueError("Value should be between 5 and 9")
if (a != "quit"):
    try:
        if(int(a)<5 or int(a)>9):
            raise ValueError("Value must be between 5 and 9")
    except:
        raise ValueError("Either enter a number between 5 and 9 or quit")
       
salary = int(input("Enter your salary: "))

if not 2000<salary<5000:
    raise ValueError("Invalid Salary")