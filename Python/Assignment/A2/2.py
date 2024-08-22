# Problem: 2
# Student Grades Management System
# A university wants to develop a system to manage and analyze student grades for different courses. The system should be able to store students grades, calculate their overall perfomance , determine the highest and lowest scores  and categorize students based on their performance.

# Objective:
# Create a Python program that manages student grades, performs various calculations. and provides insights such as average grade, the top performing students , and grade distribution.

# Student Data Format:
# The Student data is stored in a list of dictionaries , where each dictionary contains:

# "student_name": The name of the studenc (string).
# "grades": A dictionary with course names as keys and grades as values (float).

# Example
# {"student_name": "Ankur , "grades": {"Math": 85, "Science": 92, "English": 78}},

# Sample Student Data
students_data = [
    {"student_name": "Ankur", "grades": {"Math": 85, "Science": 92, "English": 78}},
    {"student_name": "Priya", "grades": {"Math": 88, "Science": 75, "English": 90}},
    {"student_name": "Rahul", "grades": {"Math": 95, "Science": 85, "English": 82}},
    {"student_name": "Sneha", "grades": {"Math": 70, "Science": 80, "English": 65}},
    {"student_name": "Kiran", "grades": {"Math": 80, "Science": 89, "English": 85}},
]

# Initialize variables for calculations
total_grades = 0
num_grades = 0
highest_grade = -1
lowest_grade = 101
top_performers = []
grade_distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

# Define grade categorization
def categorize_grade(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'

# Process student grades
for student in students_data:
    student_name = student["student_name"]
    grades = student["grades"]

    # Calculate the average grade for the student
    student_total = sum(grades.values())
    student_average = student_total / len(grades)

    # Update overall grade calculations
    total_grades += student_total
    num_grades += len(grades)
    
    # Track the highest and lowest grades
    highest_in_student = max(grades.values())
    lowest_in_student = min(grades.values())
    highest_grade = max(highest_grade, highest_in_student)
    lowest_grade = min(lowest_grade, lowest_in_student)
    
    # Track top performers
    if student_average >= 90:
        top_performers.append(student_name)
    
    # Categorize each grade for distribution
    for grade in grades.values():
        grade_category = categorize_grade(grade)
        grade_distribution[grade_category] += 1

# Calculate overall average grade
overall_average_grade = total_grades / num_grades

# Display results
print(f"Overall Average Grade: {overall_average_grade:.2f}")
print(f"Highest Grade: {highest_grade}")
print(f"Lowest Grade: {lowest_grade}")
print(f"Top Performers (Average >= 90): {', '.join(top_performers) if top_performers else 'None'}")

print("\nGrade Distribution:")
for category, count in grade_distribution.items():
    print(f"{category}: {count} students")
