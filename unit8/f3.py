from typing import List


class MenuItem:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price


class OrderItem:
    def __init__(self, menu_item: MenuItem, quantity: int) -> None:
        self.menu_item = menu_item
        self.quantity = quantity

    def line_total(self) -> float:
        return self.menu_item.price * self.quantity


class Order:
    def __init__(self, customer_name: str) -> None:
        self.customer_name = customer_name
        self.items: List[OrderItem] = []

    def add_item(self, menu_item: MenuItem, quantity: int) -> None:
        self.items.append(OrderItem(menu_item, quantity))

    def total(self) -> float:
        return sum(item.line_total() for item in self.items)

    def print_receipt(self) -> None:
        print(f"Order for {self.customer_name}")
        print("-" * 30)

        for item in self.items:
            print(
                f"{item.menu_item.name} x{item.quantity} "
                f"= £{item.line_total():.2f}"
            )

        print("-" * 30)
        print(f"Total: £{self.total():.2f}")


if __name__ == "__main__":
    burger = MenuItem("Burger", 6.99)
    fries = MenuItem("Fries", 3.99)
    drink = MenuItem("Milkshake", 3.50)

    order = Order("Alice")

    order.add_item(burger, 2)
    order.add_item(fries, 3)
    order.add_item(drink, 2)

    order.print_receipt()