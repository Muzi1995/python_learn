# Product Class

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.original_price = price

    def apply_discount(self, discount_percentage):
        discount_amount = self.original_price * (discount_percentage/100)
        self.price = self.original_price - discount_amount

        print(f"Original price: ${self.original_price}\n")
        print(f"Discount amount: ${discount_amount}\n")
        print(f"Price after {discount_percentage}% discount: ${self.price}\n")

    def __str__(self):
        return f"{self.name} will cost ${self.price}.\n"


# Customer Class

class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet_customer(self):
        print(f"\nHello! {self.name}, Welcome to Tesco.\n")

    def __str__(self):
        return f"{self.name} ({self.age} years old)"


# Shopping Cart Class

class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"{product.name} added: (${product.price}).\n")

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            print(f"Removed {product.name} from the cart.\n")
        else:
            print(f"{product.name} not found in the cart.\n")

    def checkout(self):
        total_price = sum([product.price for product in self.products])
        print(f"Total Price: ${total_price}.\n")
        print(f"Thank You for shopping.\n")
        self.products = []


Product1 = Product('Tea', 250)
Product2 = Product('Cofee', 350)
Product3 = Product('Chicken', 1250)
Product4 = Product('Onion', 10)


customer = Customer("Muzi", 29)

customer.greet_customer()

cart = ShoppingCart()

cart.add_product(Product1)
cart.add_product(Product2)
cart.add_product(Product3)
cart.add_product(Product4)

Product3.apply_discount(20)

print(f"Price after discount: {Product3}\n")

cart.remove_product(Product2)

cart.checkout()
