class Person:
    Name = "Harry"
    Occupation = "Software Developer"
    NetWorth = 10    
    def info(self):
        print(f"The name is: {self.Name}.")
        print(f"And his Occupation is {self.Occupation}.")
a= Person()
b = Person()
c = Person()
c.Name = "G Nabi"
c.Occupation = "AI Expert"
b.Name = "Ali"
b.Occupation = "Artist"
a.Name = "Haji"
a.Occupation = "Accountant"
a.info()
b.info()
c.info()
