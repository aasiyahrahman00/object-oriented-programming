from typing import List, Tuple, Optional 
class GradeManager: 
    """Manages student names and grades, and can compute averages.""" 
    def __init__(self) -> None: 
        self._students: List[Tuple[str, float]] = [] 
        
    def add_student(self, name: str, grade: float) -> None: 
        self._students.append((name, grade)) 
        
    def average_grade(self) -> Optional[float]: 
        if not self._students: 
            return None 
        total = sum(grade for _, grade in self._students) 
        return total / len(self._students) 
    
if __name__ == "__main__": 
    manager = GradeManager() 
    manager.add_student("Alice", 80) 
    manager.add_student("Bob", 40) 
    avg = manager.average_grade() 
    if avg is not None: 
        print(f"Average grade: {avg}") 
    else: 
        print("No students available to calculate an average.") 
