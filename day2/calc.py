n1 = float(input())
while True:
  operator = input()
  if operator!='=':
    n2 = float(input())
    if operator == '+':
      n1=n1+n2
    elif operator == '-':
      n1=n1-n2
    elif operator == '*':
      n1=n1*n2
    elif operator == '/':
      n1=n1/n2
    else:
      exit
  else:
    print(n1)
