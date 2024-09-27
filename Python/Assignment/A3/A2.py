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
            # Check if the product is already in the cart, if so, update the quantity
            for item in self.cart_items:
                if item.product == product:
                    item.quantity += quantity
                    product.stock_quantity -= quantity
                    return

            # Otherwise, add a new cart item
            new_item = CartItem(product, quantity)
            self.cart_items.append(new_item)
            product.stock_quantity -= quantity
        else:
            print(f"Sorry, not enough stock for {product.name}. Available: {product.stock_quantity}.")

    def remove_item(self, product):
        for item in self.cart_items:
            if item.product == product:
                # Restore the product stock when removed from the cart
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
            # Empty the cart after checkout
            self.cart_items.clear()


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.cart = ShoppingCart()

    def __str__(self):
        return f"User: {self.username}"


# Test the shopping cart system
if __name__ == "__main__":
    # Create some products
    product1 = Product("Laptop", 999.99, 10)
    product2 = Product("Headphones", 199.99, 5)
    product3 = Product("Mouse", 49.99, 20)

    # Create a user
    user1 = User("john_doe", "password123")

    # Add items to the cart
    user1.cart.add_item(product1, 2)
    user1.cart.add_item(product2, 1)
    user1.cart.add_item(product3, 3)

    # View cart items
    user1.cart.view_cart()

    # Remove an item from the cart
    user1.cart.remove_item(product3)

    # View cart after removal
    user1.cart.view_cart()

    # Checkout
    user1.cart.checkout()

    # Try to view the cart after checkout
    user1.cart.view_cart()
