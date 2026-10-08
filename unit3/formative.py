class Staff:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def show_info(self):
        print(self.name)
        print(self.email)
        
class Lecturer(Staff):
    def __init__(self, name, email, module):
        super().__init__(name, email)
        self.module = module
        
class Administrator(Staff):
    def __init__(self, name, email, department):
        super().__init__(name, email)
        self.department = department 
        
lecturer1 = Lecturer("Adam", "adam@uni.com", "Intro to mathematics")
admin1 = Administrator("Erik", "erik@uni.com", "IT")

lecturer1.show_info()
print(lecturer1.module)

admin1.show_info()
print(admin1.department)






class Vehicle:
    def __init__(self, base_fare):
        self.base_fare = base_fare
        
    def calculate_fare(self, distance):
        return self.base_fare * distance
        
class Bus(Vehicle):
    pass

class Taxi(Vehicle):
    def __init__(self, base_fare, starting_fee):
        super().__init__(base_fare)
        self.starting_fee = starting_fee
        
    def calculate_fare(self, distance):
        return self.starting_fee + (self.base_fare * distance)
        
bus1 = Bus(2)
taxi1 = Taxi(5, 2)

vehicles = [bus1, taxi1]

for vehicle in vehicles:
    print(vehicle.calculate_fare(10))
    
    
    
    
    
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    
    @abstractmethod
    def pay(self, amount):
        pass
    
class CardPayment(PaymentMethod):
    def __init__(self, last_4_digits):
       self.last_4_digits = last_4_digits
       
    def pay(self, amount):
        print(f"Paid {amount} using card ending with {self.last_4_digits}")
   
    
class PayPalPayment(PaymentMethod):
    def __init__(self,email):
        self.email = email
        
    def pay(self, amount):
        print(f"Paid {amount} using PayPal acount {self.email}")
        

        
payment_methods = [CardPayment("2937"), PayPalPayment("user@email.com")]

for payment in payment_methods:
    payment.pay(50)
       
       
       
       
       
       
       
from abc import ABC, abstractmethod 

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius ** 2
        
        
rec1 = Rectangle(4, 2)
rec2 = Rectangle(6, 3)
cir1 = Circle(5)

shapes = [rec1, rec2, cir1]

for shape in shapes:
    print(shape.area())



























