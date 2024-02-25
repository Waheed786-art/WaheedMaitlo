# In programming languages, mainly there are two approaches which are used to write programs.
# 1: Procedural Programmingk
# 2: Object Oriented Programming 

# Examples

# !: Procedural Programming
def hello():
    print("Hello")
hello()

def hi():
    return "Hi"
print(hi())

sales1 = 6000
profit1 = 2000
ad1= 1000

sales2 = 6000
profit2 = 2000
ad2 = 1000

sales3 = 6000
profit3 = 2000
ad3 = 1000

# 2: Object Oriented Programming
# In simple words, it means to make templates like if we want to fill forms the simple information is already written like Name, F/Name, Caste , etc so this is due to OOP. It makes easy for us to code.
# RailwayForm ---> Class[blueprint]
# In railwayform we have different portions/gaps left like Passenger Name, Train Name, Passenger seat name etc so these portions are known as template or OOP. It will make easy for everyone to understand the information.
# Waheed --> waheed ki info wala form --> Object [Entity]
# Sajid --> Sajid ki info wala form --> Object [Entity]
# Naveed --> Naveed ki info wala form --> Object [Entity]
# Naveed.changeName("Navi")

# Inheritance in OOP
# make additional things in OOP like If I make Railway form for VIP's only so this is known as Inheritance.
# Real life example can be: If you have a cycle and you install an engine in it means we've added additional features in it then it'll be known as Inheritance.


marks = [24, 56 ,86 ,98]

for index, mark in enumerate(marks, start = 1):# start =1 prints after the defined index.
    print(mark)
    if index == 3:
        print("Hey bruhh how are you!")





