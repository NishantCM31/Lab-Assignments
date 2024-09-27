""" # Program to compute Simple Interest
def compute_simple_interest():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest: "))
    time = float(input("Enter the time (in years): "))

    simple_interest = (principal * rate * time) / 100

    print(f"The Simple Interest is: {simple_interest}")

compute_simple_interest()
 """


def compute_simple_interest():
    while True:
        try:
            principal = float(input("Enter the principal amount: "))
            if principal <= 0:
                raise ValueError("Principal amount must be positive.")
            rate = float(input("Enter the rate of interest: "))
            if rate <= 0:
                raise ValueError("Rate of interest must be positive.")
            time = float(input("Enter the time (in years): "))
            if time <= 0:
                raise ValueError("Time must be positive.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}")

    simple_interest = (principal * rate * time) / 100
    print(f"The Simple Interest is: {simple_interest}")

compute_simple_interest()