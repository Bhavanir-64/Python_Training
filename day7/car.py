class Car:
  wheels = 4  
  def __init__(self):
    self.brand = input('Enter brand name:')  
    self.model = input('Enter model name:')
c1 = Car()
print(f'The brand is {c1.brand},and the type is {c1.model} has {c1.wheels} Wheels.')
