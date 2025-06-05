try:
  n1=int(input())
  n2=int(input())
  result=n1/n2
  #print(result)
except Exception as e:
  print(f'Error is {e}')
else:
  print(f'The result is:{result}')