a,b,c,d=map(int,input().split())
if a>=b and a>=c and a>=d:
  print("a is maximum number")
elif b>=c and b>=d:
  print("b is maximum number")
elif c>=d:
  print("c is maximum number")
else:
  print("d is maximum number")