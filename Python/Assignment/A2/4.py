# Problem no. 4:

# Employee Attendance Tracker
# Background:
# A company wants to monitor employee attendance and analyze attendance patterns. The company needs a system that records when employee clock in and clock out, calculates the total hours each day, and identifies employees with the highest and lowest attendance.

# Objective:
# Create a Python program that records and analyzes employee attendance, providing insights such as total hours worked, employees with perfect attendance, and those with the most absences.
# Attendance Data Format:

# The attendance data is Stored in a list of dictionaries, Where each dictionary contains:
# "employee_name": The name of the employee (String).
# "attendance": A dictionary with dates as keys and  tuples of clock-in and clock-out times as values (strings in HH:MM format).
# Example data:
# {"employee _name" : "Rajesh Deshpande", " attendance": {" 2024-08-15": ("09:00", "17:00"), "2024-08-16":{"09:15","17:10"}

from datetime import datetime

# Sample Employee Attendance Data
attendance_data = [
    {"employee_name": "Rajesh Deshpande", "attendance": {"2024-08-15": ("09:00", "17:00"), "2024-08-16": ("09:15", "17:10")}},
    {"employee_name": "Ayesha Khan", "attendance": {"2024-08-15": ("08:45", "16:45"), "2024-08-16": ("08:50", "17:00")}},
    {"employee_name": "John Doe", "attendance": {"2024-08-15": ("09:30", "16:30"), "2024-08-16": ("09:10", "17:00")}},
    {"employee_name": "Sneha Patil", "attendance": {"2024-08-15": ("08:50", "17:00")}},
    {"employee_name": "Priya Mehta", "attendance": {"2024-08-16": ("09:00", "17:00")}},
]

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
print("Total Hours Worked Per Employee:")
for employee, hours in total_hours_worked.items():
    print(f"{employee}: {hours:.2f} hours")

print(f"\nEmployees with Perfect Attendance: {', '.join(perfect_attendance) if perfect_attendance else 'None'}")

print(f"\nEmployees with the Most Absences: {', '.join(most_absences) if most_absences else 'None'}")

print(f"\nEmployee(s) with the Highest Attendance: {', '.join(most_attendance_employee)} with {most_hours:.2f} hours worked")
print(f"Employee(s) with the Lowest Attendance: {', '.join(least_attendance_employee)} with {least_hours:.2f} hours worked")
