# Function to categorize the grade into A, B, C, D, or F
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

# Function to process student grades
def process_student_grades(students):
    if not students:
        print("\nNo student data available to process.")
        return 0, 0, 0, {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    
    total_grades = 0
    num_grades = 0
    highest_grade = -1
    lowest_grade = 101
  
    grade_distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

    for student in students:
        student_name = student["student_name"]
        grades = student["grades"]

        # Calculate the total and average grade for the student
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

        # Track top performers based on average grade
       

        # Categorize grades and update distribution
        for grade in grades.values():
            grade_category = categorize_grade(grade)
            grade_distribution[grade_category] += 1

    overall_average_grade = total_grades / num_grades if num_grades > 0 else 0

    return overall_average_grade, highest_grade, lowest_grade,  grade_distribution

# Function to display the results
def display_results(overall_avg, highest, lowest, top_students, distribution):
    print(f"\nOverall Average Grade: {overall_avg:.2f}")
    print(f"Highest Grade: {highest}")
    print(f"Lowest Grade: {lowest}")
    print(f"Top Performers (Average >= 90): {', '.join(top_students) if top_students else 'None'}")
    
    print("\nGrade Distribution:")
    for category, count in distribution.items():
        print(f"{category}: {count} students")

# Function to accept user input for student data
def get_student_data():
    students = []
    
    while True:
        try:
            num_students = int(input("Enter the number of students to add: "))
            if num_students <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid positive integer for the number of students.")
    
    for i in range(num_students):
        print(f"\nEnter details for student {i + 1}:")
        
        while True:
            student_name = input("Enter student name: ").strip()
            if student_name:
                break
            print("Student name cannot be empty. Please enter a valid name.")
        
        grades = {}
        for subject in ["Math", "Science", "English"]:
            while True:
                try:
                    grade = int(input(f"Enter {subject} grade (0-100) for {student_name}: "))
                    if 0 <= grade <= 100:
                        grades[subject] = grade
                        break
                    print("Please enter a grade between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a valid integer for the grade.")
        
        students.append({"student_name": student_name, "grades": grades})
    
    return students

# Function to view all student details


# Function to display the menu
def display_menu():
    print("\n--- Student Grades Management System ---")
    print("1. Add New Students")
    print("2. Process and View Overall Results")
    print("3. Exit")

# Main function to execute the program
def main():
    students_data = []
    
    while True:
        display_menu()
        
        choice = input("Enter your choice (1-3): ")

        if choice == 1:  # Add new students
            new_students = get_student_data()
            students_data.extend(new_students)
            print(f"\n{len(new_students)} student(s) added successfully.")
        
        
        
        elif choice == 2:  # Process and view overall results
            overall_average, highest_grade, lowest_grade, grade_distribution = process_student_grades(students_data)
            display_results(overall_average, highest_grade, lowest_grade, grade_distribution)
        
        elif choice == 3:  # Exit
            print("\nExiting the program. Goodbye!")
            break

# Run the program
if __name__ == "__main__":
    main()