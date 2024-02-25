class get():
    def __init__(self, name):
        self._name = name
    
    def gain(self):
        print(f"{self._name} becomes {a.hi} after converting")
        
    @property
    def hi(self):
        return "--" + self._name + "--"
    @hi.setter
    def hi(self , new):
        self._name = new
        
a = get("Waheed")
a.hi = "Sajid"
a.gain()
        
class practice():
    def __init__(self, num):
        self._num = num
    def add(self):
        print(f"{self._num} becomes {b.old_value} after multiplying with 12.")
    @ property
    def old_value(self):
        return 12 * self._num
    @old_value.setter
    def new_value(self , new_value):
        self._num = new_value
    
b = practice(7)
b.new_value = 12
b.add()

def new_one(mx):
    def olm(*args , **kwargs):
        print("Start")
        mx(*args , **kwargs)
        print("End")
    return olm

# @ new_one
def hi (a , b):
    print(f"{a} {b}")
# hi("Waheed" , "Ahmed")
new_one(hi)("Waheed" , "Ahmed")
   
        
        
        
        
        
        