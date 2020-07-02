from bleach._vendor.html5lib._ihatexml import name
x = 1
y = 2

class Dog:

  def __init__(self, name, age):
    self.name = name
    self.age =  age

  def get_name(self):
    return self.name
  
  def get_age(self):
    return self.age

  def set_age(self, age):
    self.age = age 

  def bark(self):
    print("bark")

  def meow(self):
    return "meow"

  def add_one(self, x):
    return x + 1

### Open the bracket if u wanna try first version ####
# d = Dog()
# d.bark()
# d.meow()
# print(type(d))
# print(d.add_one(5))

### After adding init self name
d = Dog ("panpan", 20)
### u can also use this to print out the name
print(d.get_name())
print(d.get_age())
d2 = Dog ("raisa", 22)
print(d2.get_name())
print(d2.get_age())

### Setting age panpan and raisa
d.set_age(23)
print(d.get_age())