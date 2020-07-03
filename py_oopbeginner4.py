class Person: 
  number_of_people = 0
  GRAVITY = -9.8

  def __init__(self, name):
    self.name = name
    Person.add_person()
  
  @classmethod
  def number_of_people(cls):
    return cls.number_of_people

  @classmethod
  def add_person(cls):
    cls.number_of_people += 1

p1 = Person("Panpan")
p2 = Person("Raisa")
print(Person.number_of_people())