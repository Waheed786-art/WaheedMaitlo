class youtube():
    def __init__(self , name, goal , how):
        self.goal = goal
        self.how = how
        self.name = name
    def ne(self):
        print(f"{self.name}'s goal is to become a {self.goal} and he can achieve his goal by {self.how}.")

a = youtube("Waheed","Software Developer" , "Dedication and Hard Work")
a.ne()
b = youtube("Naveed" , "CSP" , "doing untiring efforts to improve his English writing skills.")
b.ne()

class jen():
    def __init__(self , name , gender) -> None:
        self.name = name
        self.gender = gender
    def he(self):
        print(f"{self.name} is my name and my gender is {self.gender}.")
        
a= jen("Waheed" , "Male")
a.he()

def akm(m4):
    def king():
        print("Starting.")
        m4()
        print("Ending")
    return king

def oi ():
    print("Drinking water is a good habit.")
    
akm(oi)()


class GN():
    def __init__(self , weight , height) -> None:
        self.weight = weight
        self.height = height
    def wc(self):
        a= 2
        print(f"{(self.weight/pow(self.height , 2))}")
        
a = GN(70 , 1.70688)
a.wc()

def nem(m5):
    def get(*args, **kwargs):
        print("Shuroo karo")
        m5(*args,**kwargs)
        print("Khatam bhi karo yrr jaldi")
    return get
@nem
def chej(x , se):
    print(f"{x} : {se}")
chej("Hi" , "Bruhh")

class jef():
    def __init__(self, dog , typ):
        self.dog = dog
        self.typ = typ
    def hi(self):
        print(f"The name of the dog is {self.dog} and it's a {self.typ}.")
        
        
a = jef("German Shepherd" , "Guard Dog")
a.hi()
        

    