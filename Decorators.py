def greet(fx):
    def mfx(*args , **kwargs):     # args and kwargs are used for entering arguments.
        print("Good Morning!")
        fx(*args , **kwargs)
        print("Hello Thanks for using this function.")
    return mfx
# greet(hello)() # OR
@greet   # can only be used with one function only like, hello function below                                             
def hello(a):
    print(f"{a}")

hello("Hello!")

def average(a , b , c):      # Args and kwargs are used for those functions in which arguments are required while working on decorators.
    print(f"{(a+b+c)/3}")
# greet(average)(3 , 9 ,5) 
greet(average)(3 , 3 ,3)
