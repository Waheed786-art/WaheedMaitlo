
def home(fm):
    def office(*args, **kwargs):
        print("Start")
        fm(*args, **kwargs)
        print("Ending Now.")
    return office

@home
def hm(a):
    for i in range(10):
        i+=1
        print(f"{a} x {i} = {a*i}")
hm(3)
# home(hm)(3)        

def age(a):
    if a > 10 and a < 18:
        print("You are still a child so you can't drive a car.")
    elif a >= 18:
        print("Yes you can drive now.")
    else: 
        print("Invalid Age.")
home(age)(18)

class ef():
    def __init__(self , n ,fn,ca ,cl, s , gr ) -> None:
        self.n = n
        self.fn = fn
        self.ca = ca
        self.s = s
        self.gr = gr
        self.cl = cl
    def new(self):
        print(f"""
Name       =      {self.n}
F/Name     =      {self.fn}
Caste      =      {self.ca}
Class      =      {self.cl}
School     =      {self.s}
Group      =      {self.gr}      
""")
        
a = ef("Waheed" , "A.Razzaq" , "Maitlo","XI" , "School of Excellence" , "Science" )
a.new()


def sch(gh):
    def sc(*args, **kwargs):
        print("First Page")
        gh(*args , ** kwargs)
        print("Last Page")
    return sc

def speech(a):
    print(f"{a}")
    
sch(speech)("Start with the beautiful name of ALLAH who is the most merciful and the most beneficent. So, today the topic of my speech is Online Learning don't worry I won't take more than 2 minutes.")