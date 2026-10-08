class Task:
    def __init__(self, name: str, done: bool = False) -> None:
            self.name = name 
            self.done = done
            
    def mark_done(self) -> None: 
            self.done = True
    


class TodoList:
    def __init__(self) -> None:
        self.tasks: list[Task] = []

    def add_task(self, name: str) -> None:
        new_task = Task(name)
        self.tasks.append(new_task)
        

    def mark_done(self, index: int) -> None:
        selected_task = self.tasks[index]
        selected_task.mark_done()
    



    def show_tasks(self) -> None:
        for task in self.tasks:
            if task.done:
                status = "✓"
            else:
                status = "✗"
            
            print(status, task.name)
    
if __name__ == "__main__":
    todo = TodoList()
    todo.add_task("Buy milk")
    todo.add_task("Finish assignment")
    
    todo.mark_done(0)
    todo.show_tasks()
    
    
    
    
    
