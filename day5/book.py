import grade 
gradebook={}
while True:
  print('Choices:')
  print('1.Add student')
  print('2.View student')
  print('3.Search student')
  print('4.Update student')
  print('5.Remove student')
  print('6.Exit')
  choice=int(input())
  if choice==1:
    grade.add_student(gradebook)
  elif choice==2:
    grade.view_students(gradebook)
  elif choice==3:
    grade.search_student(gradebook)
  elif choice==4:
    grade.update_student(gradebook)
  elif choice==5:
    grade.remove_student(gradebook)
  else:
    break
