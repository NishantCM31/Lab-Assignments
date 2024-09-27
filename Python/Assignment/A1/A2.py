""" # Program to swap two variables
def swap_variables():
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    print(f"Before swap: a = {a}, b = {b}")
    
    # Swapping logic
    a, b = b, a
    
    print(f"After swap: a = {a}, b = {b}")

swap_variables()
 """

def swap_variables():
    while True:
        try:
            a = int(input("Enter First Number: "))
            b = int(input("Enter Second Number: "))
            break
        except ValueError:
            print("Invalid input! Please enter integers only.")
    print(f"Before swap: a = {a}, b = {b}")
    a, b = b, a
    print(f"After swap: a = {a}, b = {b}")
swap_variables()
