def add_student(gradebook):
    name=input('Enter the student name:')
    marks=input('Enter student marks:')
    marks_list=list(map(int,marks.split(" ")))
    gradebook[name] = marks_list
  #print(gradebook)

def view_students(gradebook):
    for name, marks in gradebook.items():
        sum = 0
        for mark in marks:
            sum += mark
        avg = sum / len(marks)
        print(f'Name: {name}, Marks: {marks}, Average: {avg}')

def search_student(gradebook):
    stu_name = input('Enter the name of the student you want to search: ')
    if stu_name in gradebook:
        marks = gradebook[stu_name]
        total = 0
        for mark in marks:
            total += mark
        avg = total / len(marks)
        print(f'Name: {stu_name}, Marks: {marks}, Average Marks: {avg}')

def update_student(gradebook):
    name = input('Enter the name of the student whose marks you want to change: ')
    if name in gradebook:
        marks = input('Enter the new marks: ')
        marks_list = list(map(int, marks.split()))
        gradebook[name] = marks_list
        sum = 0
        for mark in marks_list:
            sum += mark
        avg = sum / len(marks_list)
        print('After updating the marks - Name:', name, 'Marks:', marks_list, 'Avg:', avg)

def remove_student(gradebook):
    name = input()
    if name in gradebook:
        del gradebook[name]
        print(f"{name} removed from gradebook.")