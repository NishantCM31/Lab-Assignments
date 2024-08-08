# Program to compute Simple Interest
def compute_simple_interest():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest: "))
    time = float(input("Enter the time (in years): "))

    simple_interest = (principal * rate * time) / 100

    print(f"The Simple Interest is: {simple_interest}")

compute_simple_interest()
