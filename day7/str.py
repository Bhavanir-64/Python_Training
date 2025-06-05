class Person:
  def __init__(self):
    self.name = input('Enter the name:')
    self.age = int(input('Enter the age:'))
  def __str__(self):
    return f"{self.name} ({self.age} years old)"
p1 = Person()
print(p1)