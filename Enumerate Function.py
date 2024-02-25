a = ("Apple" , "Banana" , "Cat")

for index, fruits in enumerate(a):
    print(f"{index+1}: {fruits}") # +1 means starts from 1 if we don't add + with index then it will start numbering from 0
    
    
    
marks = [23 , 43 , 64 , 35 , 98 , 76]

for index, mark in enumerate(marks, start=1):  # "start=1" prints "Awesome Program!" first and then prints 3rd index.
    print(mark)
    if (index == 3):
        print("Awesome Program!")