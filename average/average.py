
from student_dict import students


for student_id, grades in students.items():
    average_grade = sum(grades) / len(grades)
    
    if average_grade < 40:
        print(f"Student ID: {student_id}, Average: {average_grade:.2f}")
