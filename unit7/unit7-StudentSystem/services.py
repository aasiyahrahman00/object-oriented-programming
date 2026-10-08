def find_student(students: list[Student], student_id: int) -> Student | None: 
    for student in students:
        if self.student_id == student_id:
            return student
    return None