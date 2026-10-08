class Book:
    # Constructor method used to create a new Book object
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

# Create three separate Book objects using the Book class
book1 = Book("The Hobbit", "J.R.R. Tolkien", 1937)
book2 = Book("Noughts & Crosses", "Malorie Blackman", 2001)
book3 = Book("Frankenstein", "Mary Shelley", 1818)

# Print the details stored inside each Book object
print(f"Title: {book1.title}, Author: {book1.author}, Year: {book1.year}")
print(f"Title: {book2.title}, Author: {book2.author}, Year: {book2.year}")
print(f"Title: {book3.title}, Author: {book3.author}, Year: {book3.year}")



class BankAccount:
    # Constructor method, this runs automatically when a new BankAccount object is created.
    def __init__(self, name):
        self.name = name
        balence = 0
        print(f"Account created for {name}")

    # Destructor method, this runs when the object is deleted.
    def __del__(self):
        print(f"Account created for {name}")

# Create a BankAccount object. This automatically calls the constructor.
account1 = BankAccount("Aasiyah")

# Delete the BankAccount object. This should trigger the destructor.
del account1



class Student:
    # Class variable, this belongs to the Student class as a whole. It is shared by all Student objects.
    count = 0
    
    # Constructor method, this runs automatically whenever a new Student object is created.
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade 
        Student.count += 1

    # Class method, this works with the class itself rather than one specific object.
    @classmethod
    def show_count(cls):
        print(f"Total students: {cls.count}")

student1 = Student("Alice", 89)
student2 = Student("Abby", 92)
student3 = Student("Tom", 90)

# This prints the total number of students created.
Student.show_count()




class Product:
    # Class variable shared by all Product objects
    product_count = 0

    # Constructor method, runs when a new Product object is created
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.product_count += 1
 
    # Destructor method, runs when a Product object is deleted
    def __del__(self):
        Product.product_count -= 1
        print(f"Product/s Removed: {self.name}")

    # Class method, works with the class rather than one object
    @classmethod
    def total_products(cls):
        print(cls.products(cls))

product1 = Product("Bear Teddy", 20)
product2 = Product("Bunny Teddy", 25)
product3 = Product("Pengiune Teddy", 20)

print(f"Product: {product1.name}, Price: £{product1.price}")
print(f"Product: {product2.name}, Price: £{product2.price}")
print(f"Product: {product3.name}, Price: £{product3.price}")

# Show total products
Product.total_products()

# Delete one product
del product2

# Show updated total products
Product.total_products()