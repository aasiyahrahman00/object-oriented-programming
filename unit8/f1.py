class Habit:
    def __init__(self, name: str, minutes: int = 0) -> None:
        self.name = name
        self.minutes = minutes
        
    def add_minutes(self, minutes: int) -> None:
        if minutes > 0:
            self.minutes += minutes
            
            
class HabitTracker:
    def __init__(self) -> None:
        self.habit = List[habit] = []
        
    def add_habit(self, name: str) -> None:
        self.habits.append(Habit(name))
        
    def find_habit(self, name: str) -> [Habit]:
        for habit in self.habits:
            if habit.name == name:
                return habit     
        return none
    
    
def log_time(self, minutes: int) -> None:
    habit = self.find.habit(name)
    if habit is None:
        print("Habit not found")
    else:
        habit.add_minutes(minutes)
        
        
def show_report(self) -> None:
    print("Habit Report")
    for habit in self.habits:
        print(f"{habit.name}: {habit.minutes} minutes")

if __name__ == "__main__":
    traker = HabitTracker()















