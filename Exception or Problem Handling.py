a = input("Enter the number: ")   # If I enter string then 
print(f"Multiplication of number {a} is")
try:
    for i in range(1, 11):
        print(f"{int(a)} x {i} = {int(a)*i}")
except:     # it will generate error message and after this error the remaining code will run as usual.
    print("Invalid Input!") 

    
print("Some important lines of code")
print("End of Program")
try:
    num = int(input("Enter an integer: "))
    c = [6 , 3]
    print(c[num])

except ValueError:
    print("Number entered is not an integer")
    
except IndexError:
    print("Index Error") 
    
        
