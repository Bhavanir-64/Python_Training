posts=[
  {'user':'alice','post':'hi'},
  {'user':'bob','post':'hello'},
  {'user':'alice','post':'again'},
  {'user':'x','post':'xyz'},
  {'user':'bob','post':'again'}
]
count = {}
for i in posts:
    if i['user'] in count:
      count[i['user']] += 1
    else:
      count[i['user']] = 1
print(count)
name=input()
if name in count:
    print(f"{name}: {count[name]}")