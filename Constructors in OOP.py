class Person():
    # Name = "Waheed"            Without using these I can user Dundar Method(__init__)
    # Occupation = "Developer"
    def __init__(self ,name ,occ ,gender):  # __init__ is known as Dundar Method which is special kind of method to use in classes efficiently. With only self argument then it'll be said as Default Constructor.
        self.name = name
        self.occupation = occ
        self.gender = gender
        # print(f"Hey I'm a Developer.") init only return none so only print can be used.
    def info(self):
        if self.occupation[0] == "A" or self.occupation[0] == "E" or self.occupation[0] == "I"or self.occupation[0] == "O" or self.occupation[0] == "U":
            print(f"{self.name} is an {self.occupation} whose gender is {self.gender}.")
        else:
            print(f"{self.name} is a {self.occupation} whose gender is {self.gender}.")
    
a = Person("Waheed" , "Developer" , "Male")   # Self argument is already passed so we can't initialize anything in self.
b = Person("Naveed" , "Civil Engineer" , "Male")
c = Person("Sajid" , "Artist", "Male")
a.info()
b.info()
c.info()
# print(b.info())
# a.Name = "Naveed"            Without using this again and again
# a.Occupation = "Civil Engineer"
# a.info()


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