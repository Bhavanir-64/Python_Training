"""a, b ,c = map(int, input().split())
if a>b and a>c:
    print('The maximum number is:',a)
elif b>c:
    print('The maximum number is:',b)
else:
    print('The maximum number is:',c)"""

a, b ,c = map(int, input().split())
max_num = a if (a > b and a > c) else (b if b > c else c)
print(f"The maximum number is {max_num}")

