from models import Student
from services import add_student, find_student 

if __name__ == "__main__":
    students: list[Student] = []
    
    student_one = Student(101, "Adam")
    student_two = Student(102, "Alice")
    
    add_student(students, student_one)
    add_student(students, student_two)
    
    result = find_student(students, 102)
    
    if result is not None:
        print(result.student)