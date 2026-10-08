class Member: 
    """Gym membership managemnet"""
    
    def __init__(self, name, membership_type, is_active):
        self.name = name
        self.membership_type = membership_type
        self.is_active = is_active
        
    def describe(self):
        print(f"{self.name} is on a {self.membership_type} membership. Active: {self.is_active}")
        
member1 = Member("John", "Gold", True)
member2 = Member("Alice", "Bronze", True)
member3 = Member("Abby", "Platinum", False)
        
members = [member1, member2, member3]
        
for member in members:
    member.describe()





products = {
    "Bunny Teddy": {
        "name": "bunny teddy",
        "price": 20,
        "quantity": 3
    },

    "Bear Teddy": {
        "name": "bear teddy",
        "price": 20,
        "quantity": 2
    },

    "Mini Bunny Teddy": {
        "name": "mini bunny teddy",
        "price": 15,
        "quantity": 1
    },

    "Mini Bear Teddy": {
        "name": "mini bear teddy",
        "price": 15,
        "quantity": 3
    },
}

cart = [
    products["Bunny Teddy"],
    products["Mini Bunny Teddy"]
]

def calculate_total(cart):
    total_cost = 0

    for item in cart:
        total_cost += item["price"] * item["quantity"]
    return total_cost

print(f"\nYour total is: {calculate_total(cart)}")





class CartItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item: CartItem):
        self.items.append(item)

    def calculate_total(self):
        total = 0

        for item in self.items:
            total += item.price * item.quantity
        return total

cart = ShoppingCart()

item1 = CartItem("Bunny Teddy", 20, 2)
item2 = CartItem("Mini Bunny Teddy", 15, 1)
item3 = CartItem("Bear Teddy", 20, 3)

cart.add_item(item1)
cart.add_item(item2)
cart.add_item(item3)

cart.calculate_total()
print(f"\nYour total is: {cart.calculate_total()}")






students = [
    ("Alice", 80),
    ("John", 78),
    ("Abby", 86)
]

total_grades = 0
student_count = len(students)
passed_students = []

for student in students:
    name = student[0]
    grade = student[1]

    total_grades += grade

    if grade >= 50:
        passed_students.append(name)


average = total_grades / student_count

print(f"\nThe average garde is: {average}")
print("Students who passed")

for student in passed_students:
    print(student)