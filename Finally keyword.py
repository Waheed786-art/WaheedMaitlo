def func1():
 try:
    l = [ 3 , 5 , 7 , 1]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
    
 except:
    print("Invalid index")
    return 0 
    

 finally:
    print("I'm always executed!")  # Whatever happens it'll execute means it'll execute even if any error occurred before it. Mostly used in functions
    
x = func1()
print(x)