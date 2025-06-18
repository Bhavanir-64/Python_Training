l=input().split(" ")
print(l)
keyword=input()
fl=[]
for i in l:
  if keyword in i:
    fl.append(i)
print(fl)