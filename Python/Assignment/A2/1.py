# Function to collect input from the user
def get_sales_data_from_user():
    sales_data = []
    
    while True:
        try:
            num_products = int(input("How many products do you want to enter? "))
            if num_products <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid positive integer for the number of products.")
    
    for i in range(num_products):
        print(f"\nEnter details for product {i + 1}:")
        
        # Input product name
        while True:
            product_name = input("Product Name: ").strip()
            if product_name:
                break
            print("Product name cannot be empty.")
        
        # Input category
        while True:
            category = input("Category: ").strip()
            if category:
                break
            print("Category cannot be empty.")
        
        # Input units sold
        while True:
            try:
                units_sold = int(input("Units Sold: "))
                if units_sold > 0:
                    break
                print("Units sold must be a positive integer.")
            except ValueError:
                print("Invalid input. Please enter a valid positive integer for units sold.")
        
        # Input unit price
        while True:
            try:
                unit_price = float(input("Unit Price: "))
                if unit_price > 0:
                    break
                print("Unit price must be a positive number.")
            except ValueError:
                print("Invalid input. Please enter a valid positive number for unit price.")
        
        product = {
            "product_name": product_name,
            "category": category,
            "units_sold": units_sold,
            "unit_price": unit_price
        }
        sales_data.append(product)
    return sales_data

# Function to calculate total sales
def calculate_total_sales(data):
    total_sales = 0
    for item in data:
        total_sales += item["units_sold"] * item["unit_price"]
    return total_sales

# Function to calculate average sales per product
def calculate_average_sales(data, total_sales):
    return total_sales / len(data) if len(data) > 0 else 0

# Function to find the top-selling product
def find_top_selling_product(data):
    if len(data) == 0:
        return None, 0
    top_product = data[0]
    for item in data:
        if item["units_sold"] * item["unit_price"] > top_product["units_sold"] * top_product["unit_price"]:
            top_product = item
    return top_product["product_name"], top_product["units_sold"] * top_product["unit_price"]

# Function to calculate sales by category
def calculate_sales_by_category(data):
    category_sales = {}
    for item in data:
        category = item["category"]
        sales = item["units_sold"] * item["unit_price"]
        if category in category_sales:
            category_sales[category] += sales
        else:
            category_sales[category] = sales
    return category_sales

# Function to display sales by category
def display_sales_by_category(category_sales):
    print("\n===== Sales by Category =====")
    for category, sales in category_sales.items():
        print(f"{category}: ${sales:.2f}")
    print("=================================")

# Menu to display options
def display_menu():
    print("\n===== MENU =====")
    print("1. Add New Products")
    print("2. View Total Sales")
    print("3. View Average Sales per Product")
    print("4. View Top-Selling Product")
    print("5. View Sales by Category")
    print("6. Exit")
    print("=================")

# Main function to orchestrate the analysis
def main():
    sales_data = []  # This will store the list of products
    while True:
        display_menu()
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == 1:  # Add New Products
            new_data = get_sales_data_from_user()
            sales_data.extend(new_data)
            print("\nProducts have been added successfully!")

        elif choice == 2:  # View Total Sales
            total_sales = calculate_total_sales(sales_data)
            print(f"\nTotal Sales: ${total_sales:.2f}")

        elif choice == 3:  # View Average Sales per Product
            total_sales = calculate_total_sales(sales_data)
            average_sales = calculate_average_sales(sales_data, total_sales)
            print(f"\nAverage Sales per Product: ${average_sales:.2f}")

        elif choice == 4:  # View Top-Selling Product
            if len(sales_data) > 0:
                top_product_name, top_product_sales = find_top_selling_product(sales_data)
                print(f"\nTop-Selling Product: {top_product_name} with sales of ${top_product_sales:.2f}")
            else:
                print("\nNo product data available to determine the top-selling product.")

        elif choice == 5:  # View Sales by Category
            if len(sales_data) > 0:
                category_sales = calculate_sales_by_category(sales_data)
                display_sales_by_category(category_sales)
            else:
                print("\nNo product data available to calculate sales by category.")

        elif choice == 6:  # Exit
            print("\nExiting the program. Goodbye!")
            break

        else:
            print("invalid input")

        

# Run the program
main()
