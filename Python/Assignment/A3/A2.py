class Product:
    def __init__(self, name, price, stock_quantity):
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

    def __str__(self):
        return f"Product: {self.name}, Price: ${self.price:.2f}, Stock: {self.stock_quantity}"


class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def get_total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.name}: {self.quantity} @ ${self.product.price:.2f} each = ${self.get_total_price():.2f}"


class ShoppingCart:
    def __init__(self):
        self.cart_items = []

    def add_item(self, product, quantity):
        if product.stock_quantity >= quantity:
            for item in self.cart_items:
                if item.product == product:
                    item.quantity += quantity
                    product.stock_quantity -= quantity
                    return
            self.cart_items.append(CartItem(product, quantity))
            product.stock_quantity -= quantity
        else:
            print(f"Sorry, not enough stock for {product.name}. Available: {product.stock_quantity}.")

    def remove_item(self, product):
        for item in self.cart_items:
            if item.product == product:
                product.stock_quantity += item.quantity
                self.cart_items.remove(item)
                return
        print(f"{product.name} not found in the cart.")

    def view_cart(self):
        if not self.cart_items:
            print("Your cart is empty.")
        else:
            print("Items in your cart:")
            for item in self.cart_items:
                print(item)
            print(f"Total Price: ${self.get_total_price():.2f}")

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.cart_items)

    def checkout(self):
        if not self.cart_items:
            print("Your cart is empty. Add items before checkout.")
        else:
            print(f"Checkout completed. Total amount: ${self.get_total_price():.2f}")
            self.cart_items.clear()


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.cart = ShoppingCart()

    def __str__(self):
        return f"User: {self.username}"


# Main program
def display_menu():
    print("\nMenu:")
    print("1. View Products")
    print("2. Add Item to Cart")
    print("3. Remove Item from Cart")
    print("4. View Cart")
    print("5. Checkout")
    print("6. Exit")


def main():
    # Create some products
    products = [
        Product("Laptop", 999.99, 10),
        Product("Headphones", 199.99, 5),
        Product("Mouse", 49.99, 20)
    ]

    # Create a user
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    user = User(username, password)
    print(f"\nWelcome, {user.username}!\n")

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6): ")

        if choice == '1':
            print("\nAvailable Products:")
            for i, product in enumerate(products, 1):
                print(f"{i}. {product}")

        elif choice == '2':
            print("\nSelect a product to add to your cart:")
            for i, product in enumerate(products, 1):
                print(f"{i}. {product}")

            try:
                product_choice = int(input("\nEnter the product number: ")) - 1
                if 0 <= product_choice < len(products):
                    quantity = int(input(f"Enter the quantity for {products[product_choice].name}: "))
                    user.cart.add_item(products[product_choice], quantity)
                else:
                    print("Invalid product selection.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '3':
            print("\nItems in your cart:")
            if not user.cart.cart_items:
                print("Your cart is empty.")
            else:
                for i, item in enumerate(user.cart.cart_items, 1):
                    print(f"{i}. {item}")

                try:
                    item_choice = int(input("\nEnter the item number to remove from your cart: ")) - 1
                    if 0 <= item_choice < len(user.cart.cart_items):
                        user.cart.remove_item(user.cart.cart_items[item_choice].product)
                    else:
                        print("Invalid selection.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        elif choice == '4':
            print("\nViewing Cart:")
            user.cart.view_cart()

        elif choice == '5':
            user.cart.checkout()

        elif choice == '6':
            print("\nThank you for shopping with us! Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()

""" class Product:
    def __init__(self, name, price, stock_quantity):
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

    def __str__(self):
        return f"Product: {self.name}, Price: ${self.price:.2f}, Stock: {self.stock_quantity}"

    


class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def get_total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.name}: {self.quantity} @ ${self.product.price:.2f} each = ${self.get_total_price():.2f}"


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.cart = ShoppingCart()

    def __str__(self):
        return f"User: {self.username}"


class ShoppingCart:
    def __init__(self):
        self.cart_items = []

    def add_item(self, product, quantity):
        if product.stock_quantity >= quantity:
            for item in self.cart_items:
                if item.product == product:
                    item.quantity += quantity
                    product.stock_quantity -= quantity
                    return

            new_item = CartItem(product, quantity)
            self.cart_items.append(new_item)
            product.stock_quantity -= quantity
        else:
            print(f"Sorry, not enough stock for {product.name}. Available: {product.stock_quantity}.")

    def remove_item(self, product):
        for item in self.cart_items:
            if item.product == product:
                product.stock_quantity += item.quantity
                self.cart_items.remove(item)
                return
        print(f"{product.name} not found in the cart.")

    def view_cart(self):
        if not self.cart_items:
            print("Your cart is empty.")
        else:
            print("Items in your cart:")
            for item in self.cart_items:
                print(item)
            print(f"Total Price: ${self.get_total_price():.2f}")

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.cart_items)

    def checkout(self):
        if not self.cart_items:
            print("Your cart is empty. Add items before checkout.")
        else:
            print(f"Checkout completed. Total amount: ${self.get_total_price():.2f}")
            self.cart_items.clear()



# Function to display the menu
def display_menu():
    print("\nMenu:")
    print("1. View Products")
    print("2. Add Item to Cart")
    print("3. Remove Item from Cart")
    print("4. View Cart")
    print("5. Checkout")
    print("6. Exit")


# Main program
def main():
    # Create some products
    products = [
        Product("Laptop", 999.99, 10),
        Product("Headphones", 199.99, 5),
        Product("Mouse", 49.99, 20),
        Product("Keyboard", 79.99, 15),
        Product("Monitor", 249.99, 7)
    ]

    # Create a user
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    user = User(username, password)
    print(f"\nWelcome, {user.username}!\n")

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6): ")

        if choice == '1':
            print("\nAvailable Products:")
            for i, product in enumerate(products, 1):
                print(f"{i}.{product}")

        elif choice == '2':
            print("\nSelect a product to add to your cart:")
            for i, product in enumerate(products, 1):
                print(f"{i}. {product}")
            
            try:
                product_choice = int(input("\nEnter the product number: ")) - 1
                if 0 <= product_choice < len(products):
                    quantity = int(input(f"Enter the quantity for {products[product_choice].name}: "))
                    user.cart.add_item(products[product_choice], quantity)
                else:
                    print("Invalid product selection.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '3':
            print("\nItems in your cart:")
            if not user.cart.cart_items:
                print("Your cart is empty.")
            else:
                for i, item in enumerate(user.cart.cart_items, 1):
                    print(f"{i}. {item}")

                try:
                    item_choice = int(input("\nEnter the item number to remove from your cart: ")) - 1
                    if 0 <= item_choice < len(user.cart.cart_items):
                        user.cart.remove_item(user.cart.cart_items[item_choice].product)
                    else:
                        print("Invalid selection.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        elif choice == '4':
            print("\nViewing Cart:")
            user.cart.view_cart()

        elif choice == '5':
            user.cart.checkout()

        elif choice == '6':
            print("\nThank you for shopping with us! Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")
main()
 """