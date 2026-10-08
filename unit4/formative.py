class patient:
    def __init__(self, name, age, medical_history):
        self.name = name
        self._age = age
        self.__medical_history = medical_history
        
    
    def get_medical_summary(self):
        print(self.name)
        print("Sensitive medical history hidden")
        
    def add_medical_note(self, note):
        self.__medical_history.append(note)
        
        
patient = Patient("Adam", 57, ["Disbetes"])

patient.add_medical_note("High blood pressure")

patient.get_medical_summary()




class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.__balance = 0
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Amount can't be negative")
        
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")
            
    def get_balance():
        return self.__balance
    
    
acc1 = BankAccount("Adam")

acc1.__balance = 9999
print("Direct access does not modify the private balance")

acc1.diposit(500)
print(acc1.get_balence())

acc1.withdraw(200)
print(acc1.get_balance())




from abc import ABC, abstractmethod

class TaskCollection(ABC):
    @abstractmethod
    def add_task(self, task):
        pass
    
    @abstractmethod
    def get_next_task():
        pass
        
    @abstractmethod
    def has_tasks():
        pass
    
    
class TaskQueue(TaskCollection):
    self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
        
    def get_next_task(self):
        return self.tasks.pop(0)
        
    def has_tasks(self):
        return len(self.tasks) > 0

        
        
class TaskStack(TaskCollection):
    self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
        
    def get_next_task(self):
        self.tasks.pop()
        
    def has_tasks(self):
        return len(self.tasks) > 0
    
    
queue = TaskQueue()
stack = TaskStack()

queue.add_task("Task A")
queue.add_task("Task B")
queue.add_task("Task C")       
  
stack.add_task("Task A")
stack.add_task("Task B")
stack.add_task("Task C")  

print("Queue Order")   

while queue.has_tasks():
    print(queue.get_next_task())  
    
print("Stack Order")

while stack.has_tasks():
    print(stack.get_next_task())
    
print("Queue uses FIFO")
print("Queue uses LIFO")