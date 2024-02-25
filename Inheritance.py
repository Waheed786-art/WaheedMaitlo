
class employee():
    def __init__(self, name , id):
        self.name = name
        self.id = id
    # def show_details(self):
    #     print(f"The name of the employee: {self.id} is {self.name}")
class Programmer(employee):           # This is Inheritance(it is used to change the name of class/constructor and it is very useful)
    def show_details(self):          # After changing name.
        print(f"The name of the employee: {self.id} is {self.name}")
e = Programmer ("Sajid" , 420)
e.show_details()
e1 = Programmer("Waheed" , "20")
e1.show_details()


class care():
    def __init__ (self , name , gender):
        self._name = name
        self._gender = gender    
    def care_1(self):
        print(f"{self._name} becomes {a.one_value} and his gender is {self._gender}")
    @property
    def one_value (self):
        return "--" + self._name + "--"
    @one_value.setter
    def one_value(self , new_value):
        self._name = new_value
    
a = care("Waheed" , "Male")
a.one_value = "Sajid"
a.care_1()
    
        
    
class student():
    def __init__(self, name , clas):
        self.name = name
        self.clas = clas
        
class pupil(student):  # Inheritance
        def sef(self):
            print(f"{self.name} is currently in {self.clas} class")
            
t = pupil("Waheed" , "First Year")
t.sef()

