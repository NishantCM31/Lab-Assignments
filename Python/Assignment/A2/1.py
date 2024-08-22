# Control Structure In Python

# Problem : 1
# Sales Data Analysis for a Retail Store
# Background:

# A retail store wants to analyze its monthly sales date to understand trends, identity top-selling products, and make data-driven decisions. The store collects data on the number of units sold for each product, along with the prices and categories of the products. The management wants to automate the analysis process using a Python script.

# Objective:
# Create a Python program that reads sales data, processes it, and provides insights such as total sales, average sales per product, top-selling products and sales by category. The program should use appropriate data types and control structures (loops, conditionbls, etc.) to accomplish these tasks.

# Sales Data Format:
# The sales data is stored in a list of dictionaries, where each dictionary contains information about a Single product's sales. The keys in each dictionary are:


# "product_name": The name of the product(string)
# "category": The category the product belongs to (string).
# "units_sold": The number of units sold (integer).
# "unit_price•: The price per unit (float}. 

# Sample Sales Data
sales_data = [
    {"product_name": "Laptop", "category": "Electronics", "units_sold": 30, "unit_price": 1000.00},
    {"product_name": "Headphones", "category": "Electronics", "units_sold": 120, "unit_price": 50.00},
    {"product_name": "Smartphone", "category": "Electronics", "units_sold": 80, "unit_price": 700.00},
    {"product_name": "Blender", "category": "Home Appliances", "units_sold": 50, "unit_price": 150.00},
    {"product_name": "Vacuum Cleaner", "category": "Home Appliances", "units_sold": 40, "unit_price": 200.00},
    {"product_name": "Coffee Maker", "category": "Home Appliances", "units_sold": 70, "unit_price": 100.00},
    {"product_name": "Book", "category": "Books", "units_sold": 200, "unit_price": 15.00},
    {"product_name": "Novel", "category": "Books", "units_sold": 150, "unit_price": 20.00},
]

# Initialize variables
total_sales = 0
category_sales = {}
product_sales = {}
total_units_sold = 0

# Processing sales data
for item in sales_data:
    product_name = item["product_name"]
    category = item["category"]
    units_sold = item["units_sold"]
    unit_price = item["unit_price"]
    
    # Calculate total sales for the product
    sales_for_product = units_sold * unit_price
    total_sales += sales_for_product
    total_units_sold += units_sold
    
    # Track sales by product
    product_sales[product_name] = sales_for_product
    
    # Track sales by category
    if category in category_sales:
        category_sales[category] += sales_for_product
    else:
        category_sales[category] = sales_for_product

# Calculate average sales per product
average_sales_per_product = total_sales / len(sales_data)

# Identify top-selling product
top_selling_product = max(product_sales, key=product_sales.get)
top_selling_amount = product_sales[top_selling_product]

# Display results
print(f"Total Sales: ${total_sales:.2f}")
print(f"Average Sales per Product: ${average_sales_per_product:.2f}")
print(f"Top-Selling Product: {top_selling_product} with ${top_selling_amount:.2f} in sales")

print("\nSales by Category:")
for category, sales in category_sales.items():
    print(f"{category}: ${sales:.2f}")
