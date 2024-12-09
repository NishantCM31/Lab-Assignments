from datetime import datetime

# Function to accept attendance data from the user
def get_attendance_data():
    attendance_data = []
    
    # Validate the number of employees
    while True:
        try:
            num_employees = int(input("Enter the number of employees: "))
            if num_employees <= 0:
                print("Please enter a positive number of employees.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter an integer.")

    # Input attendance for each employee
    for _ in range(num_employees):
        employee_name = input("Enter employee name: ")
        attendance = {}

        while True:
            # Validate date format
            while True:
                date = input(f"Enter attendance date for {employee_name} (YYYY-MM-DD): ")
                try:
                    datetime.strptime(date, "%Y-%m-%d")  # Validate date format
                    break
                except ValueError:
                    print("Invalid date format! Please use YYYY-MM-DD.")
            
            # Validate time format
            while True:
                clock_in = input(f"Enter clock-in time for {employee_name} on {date} (HH:MM): ")
                try:
                    datetime.strptime(clock_in, "%H:%M")  # Validate time format
                    break
                except ValueError:
                    print("Invalid clock-in time format! Please use HH:MM.")
            
            while True:
                clock_out = input(f"Enter clock-out time for {employee_name} on {date} (HH:MM): ")
                try:
                    datetime.strptime(clock_out, "%H:%M")  # Validate time format
                    break
                except ValueError:
                    print("Invalid clock-out time format! Please use HH:MM.")

            attendance[date] = (clock_in, clock_out)

            # Check if the user wants to add more dates
            more_days = input("Do you want to add another day for this employee? (yes/no): ").lower()
            if more_days != 'yes':
                break

        attendance_data.append({"employee_name": employee_name, "attendance": attendance})
        
    return attendance_data

# Function to display results
def display_results(total_hours_worked, perfect_attendance, most_absences, most_hours, least_hours, most_attendance_employee, least_attendance_employee):
    print("\nTotal Hours Worked Per Employee:")
    for employee, hours in total_hours_worked.items():
        print(f"{employee}: {hours:.2f} hours")

    print(f"\nEmployees with Perfect Attendance: {', '.join(perfect_attendance) if perfect_attendance else 'None'}")
    print(f"\nEmployees with the Most Absences: {', '.join(most_absences) if most_absences else 'None'}")
    print(f"\nEmployee(s) with the Highest Attendance: {', '.join(most_attendance_employee)} with {most_hours:.2f} hours worked")
    print(f"Employee(s) with the Lowest Attendance: {', '.join(least_attendance_employee)} with {least_hours:.2f} hours worked")

# Main program
def main():
    attendance_data = []
    
    while True:
        print("\nMenu:")
        print("1. Enter Employee Attendance Data")
        print("2. View Attendance Summary")
        print("3. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            # Input attendance data
            attendance_data = get_attendance_data()
        elif choice == "2":
            if not attendance_data:
                print("No attendance data available. Please enter data first.")
                continue

            # Initialize variables for tracking
            total_hours_worked = {}
            perfect_attendance = []
            most_absences = []
            all_dates = set()

            # Calculate total hours worked for each employee
            for employee in attendance_data:
                employee_name = employee["employee_name"]
                attendance = employee["attendance"]
                
                # Initialize total hours worked for this employee
                total_hours_worked[employee_name] = 0
                days_worked = len(attendance)
                
                # Track all dates to check for perfect attendance
                for date in attendance:
                    all_dates.add(date)
                    
                    # Parse clock-in and clock-out times
                    clock_in, clock_out = attendance[date]
                    clock_in_time = datetime.strptime(clock_in, "%H:%M")
                    clock_out_time = datetime.strptime(clock_out, "%H:%M")
                    
                    # Calculate hours worked for the day
                    hours_worked = (clock_out_time - clock_in_time).total_seconds() / 3600  # Convert seconds to hours
                    total_hours_worked[employee_name] += hours_worked
                
                # Check for perfect attendance
                if days_worked == len(all_dates):
                    perfect_attendance.append(employee_name)
                else:
                    most_absences.append(employee_name)

            # Determine employees with the highest and lowest attendance
            most_hours = max(total_hours_worked.values())
            least_hours = min(total_hours_worked.values())

            most_attendance_employee = [employee for employee, hours in total_hours_worked.items() if hours == most_hours]
            least_attendance_employee = [employee for employee, hours in total_hours_worked.items() if hours == least_hours]

            # Display results
            display_results(total_hours_worked, perfect_attendance, most_absences, most_hours, least_hours, most_attendance_employee, least_attendance_employee)
        
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please select a valid option.")

# Run the main program
if __name__ == "__main__":
    main()
