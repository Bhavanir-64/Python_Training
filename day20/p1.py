Email=input()
p=Email[1:len(Email)-1]
#print(p)
if '@' and '.' in p:
  print('True')
else:
  print('False')