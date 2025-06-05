class person:
  def __init__(self):
    self.name=input('Enter the name:')
    #print(f'My name is {name}')
  def new_name(self):
    self.name=input('Enter new name:')
  def printname(self):
    print(f'My Name is {self.name}')
p=person()
#p.oldname('surya')
p.new_name()
p.printname()