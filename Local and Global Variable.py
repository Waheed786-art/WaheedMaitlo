x = 5  # Global variable because it is outside the function.

def hello():
    x = 3   # Local Variable
    print(f"The Local variable is {x}")
    print(f"The Global variable is {x}")
    
hello()
