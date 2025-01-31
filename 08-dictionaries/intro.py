student_grades = {}

student_grades['john'] = 45
student_grades['ann'] = 47
student_grades['peter'] = 67
student_grades['mike'] = 60
student_grades['mary'] = 48

#for k in student_grades:
#    print(k, student_grades[k])

name = input("student name: ")
if name in student_grades:
    print(student_grades[name])
else:
    print("student not found")