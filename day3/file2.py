import file1 as f1
n1=int(input())
while True:
  op=input()
  if op!='=':
    n2=int(input())
    if op=='+':
      n1=f1.add(n1,n2)
    elif op=='-':
      n1=f1.sub(n1,n2)
    elif op=='*':
      n1=f1.mul(n1,n2)
    elif op=='/':
      n1=f1.div(n1,n2)
    elif op=='**':
      n1=f1.pow(n1,n2)
    elif op=='%':
      n1=f1.mod(n1,n2)
    else:
      break
  print(n1)
