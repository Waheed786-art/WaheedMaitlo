
class MyClass():
    def __init__(self, value):
        self._value = value
        
    def show(self):
        print(f"After dividing {a.ten_value} by 10 it'll become {self._value}")
    
    @property              # This is Getter.
    def ten_value(self):
        return 10*self._value
    @ten_value.setter         # this setter and it is used to change the value of arguments.
    def ten_value (self , new_value):
        self._value = new_value/10

    
a  = MyClass(6)
a.ten_value = 87
print(a.ten_value)
a.show()

# print(f"10 x {a._value} = {a.ten_value} ")

class Farhan():
    def __init__ (self, name):
        self._name = name
    
    def nam(self):
        print(f"{b._name} becomes {self.value} after adding Hi in the beginning.")
    @property
    def value(self):
        return "Hi" + self._name
    @value.setter
    def value(self, new):
        self._name = new

b = Farhan("Waheed")
b.nam()
b._name = "Farhan"
b.nam()

class jason():
    def __init__(self, valu):
        self._valu = valu
    def je(self):
        print(f"{h.ke}g becomes after {(self._valu)/1000} converting it to kg")
    @property
    def ke(self):
        return 10*self._valu
    @ke.setter
    def ke(self, nem):
        self._valu = nem

h = jason(23)
h.ke = 46
print(h.ke)
h.je()