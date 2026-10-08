from abc import ABC, abstractmethod

# ============================================================
# USER CLASSES
# ============================================================

class User(ABC):
    """
    Abstract parent class for all user types

    Stores common user information and requires subclasses
    to provide their own implementation of view_details()
    """

    def __init__(self, user_id, name, email):
        # Private attributes protect user information from direct modification
        self.__user_id = user_id
        self.__name = name
        self.__email = email

    @property
    def user_id(self):
        return self.__user_id

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @abstractmethod
    def view_details(self):
        """Display information for the relevant user type"""
        pass


class Customer(User):
    """
    Represents a standard customer

    Inherits common user information from User and provides
    standard customer behaviour with no discount
    """

    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)

    def view_details(self):
        """Display the standard customer's details"""
        print("\nUser Information: ")
        print(f"\nUser ID: {self.user_id}")
        print(f"User Name: {self.name}")
        print(f"User Email: {self.email}")

    def get_discount_rate(self):
        """Standard customers do not receive a discount"""
        return 0


class PremiumCustomer(Customer):
    """
    Represents a premium customer

    Extends Customer by adding a discount rate and overrides
    customer behaviour where appropriate
    """

    def __init__(self, user_id, name, email, discount_rate):
        super().__init__(user_id, name, email)
        self.__discount_rate = discount_rate

    @property
    def discount_rate(self):
        return self.__discount_rate

    def view_details(self):
        """Display premium customer details and discount rate"""
        print("\nUser Information: ")
        print(f"\nPremium User ID: {self.user_id}")
        print(f"Premium User Name: {self.name}")
        print(f"Premium User Email: {self.email}")
        print(f"Premium User Discount Rate: {self.discount_rate}%")

    def get_discount_rate(self):
        """
        Override the standard customer discount behaviour
        and return the premium customer's discount rate
        """
        return self.__discount_rate


# ============================================================
# PRODUCT CLASS
# ============================================================

class Product:
    """
    Represents a product available in the online shop

    Stores product information and manages stock while maintaining
    a class-level count of the number of products created
    """

    product_count = 0

    def __init__(self, name, price, stock):
        self.__name = name
        self.__price = price
        self.stock = stock

        # Shared class variable tracks all Product objects created
        Product.product_count += 1

    @property
    def stock(self):
        return self._stock

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @stock.setter
    def stock(self, quantity):
        """Prevent the product from being given negative stock"""
        if quantity >= 0:
            self._stock = quantity
        else:
            print("\nStock cannot be negative")

    @classmethod
    def total_products(cls):
        """Display the total number of products created"""
        print(f"\nTotal products in system: {cls.product_count}")

    def display_product(self):
        """Display the product's current information"""
        print(f"Product Name: {self.name}")
        print(f"Price: £{self.price}")
        print(f"Stock: {self.stock}")

    def update_stock(self, quantity):
        """Update stock through the validated stock property"""
        self.stock = quantity

    def __del__(self):
        """Display a message when a Product object is destroyed"""
        print(f"\nProduct '{self.name}' has been removed from the system")


# ============================================================
# ORDER INTERFACE AND ORDER CLASS
# ============================================================

class Orderable(ABC):
    """
    Abstract interface for order-like classes

    Any class implementing Orderable must provide methods for
    placing an order and calculating its total
    """

    @abstractmethod
    def place_order(self):
        pass

    @abstractmethod
    def calculate_total(self):
        pass


class Order(Orderable):
    """
    Represents a customer order

    Maintains the selected customer, basket contents and order
    status while providing basket, pricing and ordering behaviour
    """

    def __init__(self, order_id):
        self.__order_id = order_id
        self.__products = []
        self.__customer = None
        self.__status = "Pending"

    @property
    def order_id(self):
        return self.__order_id

    @property
    def products(self):
        return self.__products

    @property
    def customer(self):
        return self.__customer

    @property
    def status(self):
        return self.__status

    def set_customer(self, customer):
        """Associate a registered customer with this order"""
        self.__customer = customer

    def view_basket(self):
        """Display all products currently in the basket"""
        if len(self.products) == 0:
            print("\nYour basket is empty.")
        else:
            print("\nBasket Contents: ")
            for product in self.products:
                print(f"- {product.name} £{product.price:.2f}")

    def add_product(self, product):
        """Add a selected Product object to the basket"""
        self.__products.append(product)
        print(f"\n{product.name} added to basket")

    def remove_product(self, product):
        """
        Remove a selected product from the basket and return
        one unit to the product's available stock
        """
        if product in self.products:
            self.__products.remove(product)
            product.update_stock(product.stock + 1)
            print(f"\n{product.name} removed from basket")
        else:
            print("\nProduct not found in basket")

    def calculate_total(self):
        """Calculate and return the subtotal before discounts"""
        total = 0

        for product in self.products:
            total += product.price

        return total

    def calculate_discount(self):
        """
        Calculate the customer's discount

        Polymorphism allows the Order to call get_discount_rate()
        without checking whether the customer is standard or premium
        """
        total = self.calculate_total()

        if self.__customer is not None:
            discount = total * (self.customer.get_discount_rate() / 100)
            return discount

        return 0

    def place_order(self):
        """
        Place the order if it has not already been placed
        and the basket contains at least one product
        """
        if self.__status == "Placed":
            print("\nThis order has already been placed")
            return

        if len(self.products) == 0:
            print("\nCannot place an empty order")
            return

        subtotal = self.calculate_total()
        discount = self.calculate_discount()
        total = subtotal - discount

        print("\nOrder Details:")
        print(f"\nOrder ID: {self.__order_id}")
        print(f"Subtotal: £{subtotal:.2f}")

        if discount > 0:
            print(f"Premium Customer Discount (10%): -£{discount:.2f}")

        print(f"Total Cost: £{total:.2f}")
        print("Order Placed")

        # Clear the basket and update the order state once completed.
        self.__products.clear()
        self.__status = "Placed"

    def track_order(self):
        """Display the current order status """
        print(f"\nOrder ID: {self.order_id}")
        print(f"Order Status: {self.status}")

    def __del__(self):
        """Display a message when an Order object is destroyed"""
        print(f"\nOrder {self.order_id} has been removed from the system")


# ============================================================
# MAIN PROGRAM
# ============================================================

# Create the initial products available when the application starts 
product1 = Product("Bunny Teddy", 29.99, 20)
product2 = Product("Bear Teddy", 34.99, 25)
product3 = Product("Elephant Teddy", 32.99, 15)

products = [product1, product2, product3]

# Store registered customers
customers = []

# No active customer exists until registration is completed
customer1 = None

# Create the order used during the current shopping session
order1 = Order(101)

running = True


# ============================================================
# MENU LOOP
# ============================================================

while running:
    print("\nOnline Shopping System")
    print("Select an option from the menu below")

    print("\n---- Customer Options ----")
    print("1. View Products")
    print("2. Register")
    print("3. View Your Details")
    print("4. View Basket")
    print("5. Add product to order")
    print("6. Remove product from order")
    print("7. View Order Total")
    print("8. Place Order")
    print("9. Track Order")

    print("\n----- Admin Options -----")
    print("10. Add New Product")

    print("\n11. Exit")

    choice = input("\nEnter your choice: ")

    # --------------------------------------------------------
    # OPTION 1: VIEW PRODUCTS
    # --------------------------------------------------------

    if choice == "1":
        print("\nProducts available:")

        for product in products:
            print()
            product.display_product()

        Product.total_products()

    # --------------------------------------------------------
    # OPTION 2: REGISTER CUSTOMER
    # --------------------------------------------------------

    elif choice == "2":
        print("\nCustomer Registration")

        # Require a non-empty customer name.
        while True:
            name = input("Enter your name: ")

            if name == "":
                print("\nName cannot be empty. Please try again.")
            else:
                break

        # Perform basic validation of the email address.
        while True:
            email = input("Enter your email: ")

            if "@" not in email or "." not in email:
                print("\nInvalid email address. Please try again.")
            else:
                break

        # Allow registration as either a standard or premium customer.
        while True:
            customer_type = input(
                "Would you like to become a premium customer? yes/no? "
            ).lower()

            if customer_type == "yes":
                customer1 = PremiumCustomer(
                    len(customers) + 1,
                    name,
                    email,
                    10
                )

                customers.append(customer1)

                # Associate the registered customer with the current order.
                order1.set_customer(customer1)

                print(
                    "\nYou have successfully registered as a premium customer."
                )
                break

            elif customer_type == "no":
                customer1 = Customer(
                    len(customers) + 1,
                    name,
                    email
                )

                customers.append(customer1)
                order1.set_customer(customer1)

                print("\nYou have successfully registered.")
                break

            else:
                print("\nInvalid answer. Enter yes or no.")


    # --------------------------------------------------------
    # OPTION 3: VIEW CUSTOMER DETAILS
    # --------------------------------------------------------

    elif choice == "3":
        if customer1 is None:
            print("\nYou have not registered. Please register first.")
        else:
            # Polymorphism determines which view_details() implementation runs.
            customer1.view_details()


    # --------------------------------------------------------
    # OPTION 4: VIEW BASKET
    # --------------------------------------------------------

    elif choice == "4":
        order1.view_basket()


    # --------------------------------------------------------
    # OPTION 5: ADD PRODUCT TO ORDER
    # --------------------------------------------------------

    elif choice == "5":
        if customer1 is None:
            print("\nPlease register before adding products to your order.")
            continue

        print("Choose a product number: ")

        for index, product in enumerate(products, start=1):
            print(f"{index}. {product.name} - £{product.price:.2f}")

        # Protect the program from non-numeric menu input
        try:
            product_choice = int(input("\nEnter a product number: "))
        except ValueError:
            print("\nInvalid input. Enter a valid number.")
            continue

        if 1 <= product_choice <= len(products):
            selected_product = products[product_choice - 1]

            # Only add the item if stock is available
            if selected_product.stock > 0:
                order1.add_product(selected_product)

                # Reduce available stock after adding the item
                selected_product.update_stock(
                    selected_product.stock - 1
                )
            else:
                print("This product is out of stock.")

        else:
            print("\nInvalid product choice. Please enter a product number.")


    # --------------------------------------------------------
    # OPTION 6: REMOVE PRODUCT FROM ORDER
    # --------------------------------------------------------

    elif choice == "6":
        if len(order1.products) == 0:
            print("\nYour basket is empty.")
            continue

        print("\nChoose a product to remove: ")

        for index, product in enumerate(order1.products, start=1):
            print(f"{index}. {product.name} - £{product.price:.2f}")

        try:
            remove_choice = int(
                input("\nEnter product number to remove: ")
            )
        except ValueError:
            print("\nInvalid input. Enter a valid number.")
            continue

        if 1 <= remove_choice <= len(order1.products):
            selected_product = order1.products[remove_choice - 1]
            order1.remove_product(selected_product)
        else:
            print("\nInvalid product choice.")


    # --------------------------------------------------------
    # OPTION 7: VIEW ORDER TOTAL
    # --------------------------------------------------------

    elif choice == "7":
        if len(order1.products) == 0:
            print("\nYour basket is empty.")

        else:
            subtotal = order1.calculate_total()
            discount = order1.calculate_discount()
            final_total = subtotal - discount

            print(f"\nSubtotal: £{subtotal:.2f}")

            if discount > 0:
                print(
                    f"Premium Customer Discount (10%): "
                    f"-£{discount:.2f}"
                )

            print(f"Current order total: £{final_total:.2f}")


    # --------------------------------------------------------
    # OPTION 8: PLACE ORDER
    # --------------------------------------------------------

    elif choice == "8":
        if customer1 is None:
            print("\nPlease register before placing an order.")
        else:
            order1.place_order()


    # --------------------------------------------------------
    # OPTION 9: TRACK ORDER
    # --------------------------------------------------------

    elif choice == "9":
        order1.track_order()


    # --------------------------------------------------------
    # OPTION 10: ADD NEW PRODUCT
    # --------------------------------------------------------

    elif choice == "10":
        print("\nAdd New Product")

        # Product names cannot be empty
        while True:
            product_name = input("Enter product name: ")

            if product_name == "":
                print(
                    "\nProduct name cannot be empty. "
                    "Please try again."
                )
            else:
                break

        # Validate that price is numeric and non-negative
        while True:
            try:
                product_price = float(
                    input("Enter product price: £")
                )

                if product_price < 0:
                    print(
                        "\nPrice cannot be negative. "
                        "Please try again."
                    )
                else:
                    break

            except ValueError:
                print(
                    "\nInvalid input. Price must be a number. "
                    "Please try again."
                )

        # Validate that stock is a non-negative whole number
        while True:
            try:
                product_stock = int(
                    input("Enter product stock: ")
                )

                if product_stock < 0:
                    print(
                        "\nStock cannot be negative. Please try again."
                    )
                else:
                    break

            except ValueError:
                print(
                    "\nInvalid input. Stock must be a whole number. Please try again."
                )

        # Create the new Product object and add it to the catalogue
        new_product = Product(
            product_name,
            product_price,
            product_stock
        )

        products.append(new_product)

        print(
            f"\n{new_product.name} has been added to the product list."
        )

    # --------------------------------------------------------
    # OPTION 11: EXIT
    # --------------------------------------------------------

    elif choice == "11":
        print("\nYou have exited the Online Shopping System.")
        running = False


    # --------------------------------------------------------
    # INVALID MENU OPTION
    # --------------------------------------------------------

    else:
        print(
            "\nInvalid menu choice. Please enter a number from 1 to 11."
        )














