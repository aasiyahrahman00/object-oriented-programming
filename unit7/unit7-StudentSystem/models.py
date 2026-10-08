class Student:
    def __init__(self, student_id: int, name: str) -> None:
        self.student_id = student_id
        self.name = name
        
def add_student(students: list[Student], student: Student) -> None:
    students.append(student)
    



