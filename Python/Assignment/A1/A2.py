# Program to swap two variables
def swap_variables():
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    print(f"Before swap: a = {a}, b = {b}")
    
    # Swapping logic
    a, b = b, a
    
    print(f"After swap: a = {a}, b = {b}")

swap_variables()
