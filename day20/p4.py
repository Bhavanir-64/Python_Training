n=int(input())
list=[]
for i in range(n):
  name=input()
  id=int(input())
  dict = {'name': name, 'id': id}
  list.append(dict)
print(list)
key=input()
data=[]
for i in list:
  if key.lower() in i['name'].lower():
    data.append(i)
print(data)