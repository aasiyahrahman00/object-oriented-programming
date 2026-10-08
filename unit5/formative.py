try: 
    total_bill = float(input("Enter thr total bill: "))
    num_people = int(input("Enter the number of people: "))
    amount_each = total_bill / num_people
except ValueError:
    print("Enter numbers only")
except ZeroDivisionError:
    print("Number of people cannot be 0")
else:
    print(f"Each person should pay: £{amount_each:.2f}")
    
    
def read_marks(filename):
    marks = []
    
    try:
        with open(filename, "r") as file:
            for line in file:
                mark = int(line.strip())
                marks.append(mark)
    except FileNotFoundError:
        print(f"{filename} was not found")
        raise
    return marks

    try:
       marks = read_marks("marks.txt")
       print("Marks: ", marks)
    except FileNotFoundError:
       print("marks.txt not found")
    except ValueError:
       print("A mark in the filr is invalid")
       
       

class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self):
        self.__balence = 0
        
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount   
        
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        
        if amount > self.__balence:
            raise InsufficientFundsError("Insufficent funds. Current balance is £{self.__balance:.2f}, " f"but you tried to withdraw £{amount:.2f}.")
        self.__balence -= amount 
        
    def get_balence(self):
        return self.__balence

account = BankAccount()

account.deposit(100)
print("Current balance:", account.get_balance())

try:
    account.withdraw(150)
except InsufficientFundsError as error:
    print("Withdraw failed:", error)
    
print(f"Final balance: £{account.get_balance():.2f}")




def log_message(filename, message):
    try:
        with open(filename, "a") as file:
            file.write(message + "\n")
    except IOError:
        print("Could not write to log file")
    finally:
        print("finished log attempt")