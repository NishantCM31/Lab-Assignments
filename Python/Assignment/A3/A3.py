class Person:
    def __init__(self, name, age, person_id):
        self.name = name
        self.age = age
        self.person_id = person_id

    def __str__(self):
        return f"{self.name}, Age: {self.age}, ID: {self.person_id}"


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age, student_id)
        self.grade = None  # Default grade, to be assigned later
        self.enrolled_courses = []

    def enroll_in_course(self, course):
        self.enrolled_courses.append(course)
        course.enroll_student(self)

    def __str__(self):
        return f"Student: {super().__str__()}, Grade: {self.grade}"


class Teacher(Person):
    def __init__(self, name, age, teacher_id, subject):
        super().__init__(name, age, teacher_id)
        self.subject = subject
        self.assigned_courses = []

    def assign_course(self, course):
        self.assigned_courses.append(course)
        course.assign_teacher(self)

    def __str__(self):
        return f"Teacher: {super().__str__()}, Subject: {self.subject}"


class Course:
    def __init__(self, course_name, course_id):
        self.course_name = course_name
        self.course_id = course_id
        self.enrolled_students = []
        self.teacher = None

    def enroll_student(self, student):
        self.enrolled_students.append(student)

    def assign_teacher(self, teacher):
        self.teacher = teacher

    def calculate_average_grade(self):
        total_grades = 0
        num_students = len(self.enrolled_students)
        for student in self.enrolled_students:
            if student.grade is not None:
                total_grades += student.grade
        return total_grades / num_students if num_students > 0 else 0

    def view_students(self):
        if not self.enrolled_students:
            print(f"No students enrolled in {self.course_name}.")
        else:
            print(f"Students enrolled in {self.course_name}:")
            for student in self.enrolled_students:
                print(student)

    def __str__(self):
        teacher_info = self.teacher.name if self.teacher else "None"
        return f"Course: {self.course_name}, ID: {self.course_id}, Teacher: {teacher_info}"


class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_course(self, course):
        self.courses.append(course)

    def enroll_student_in_course(self, student, course):
        student.enroll_in_course(course)

    def assign_teacher_to_course(self, teacher, course):
        teacher.assign_course(course)

    def view_students_in_course(self, course):
        course.view_students()

    def view_courses_for_student(self, student):
        if not student.enrolled_courses:
            print(f"{student.name} is not enrolled in any courses.")
        else:
            print(f"Courses for {student.name}:")
            for course in student.enrolled_courses:
                print(course)

    def calculate_average_grade_for_course(self, course):
        avg_grade = course.calculate_average_grade()
        print(f"Average grade for {course.course_name}: {avg_grade:.2f}")

    def __str__(self):
        return f"School: {self.name}"


# Menu-driven interface
def main():
    school_name = input("Enter the name of the school: ")
    school = School(school_name)

    while True:
        print("\n--- School Management System ---")
        print("1. Add Student")
        print("2. Add Teacher")
        print("3. Add Course")
        print("4. Enroll Student in Course")
        print("5. Assign Teacher to Course")
        print("6. View Students in Course")
        print("7. View Courses for a Student")
        print("8. Calculate Average Grade for a Course")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            student_id = int(input("Enter student ID: "))
            student = Student(name, age, student_id)
            school.add_student(student)
            print(f"Student {name} added successfully.")

        elif choice == '2':
            name = input("Enter teacher name: ")
            age = int(input("Enter teacher age: "))
            teacher_id = int(input("Enter teacher ID: "))
            subject = input("Enter teacher subject: ")
            teacher = Teacher(name, age, teacher_id, subject)
            school.add_teacher(teacher)
            print(f"Teacher {name} added successfully.")

        elif choice == '3':
            course_name = input("Enter course name: ")
            course_id = int(input("Enter course ID: "))
            course = Course(course_name, course_id)
            school.add_course(course)
            print(f"Course {course_name} added successfully.")

        elif choice == '4':
            student_id = int(input("Enter student ID: "))
            course_id = int(input("Enter course ID: "))
            student = next((s for s in school.students if s.person_id == student_id), None)
            course = next((c for c in school.courses if c.course_id == course_id), None)
            if student and course:
                school.enroll_student_in_course(student, course)
                print(f"Student {student.name} enrolled in {course.course_name}.")
            else:
                print("Student or course not found.")

        elif choice == '5':
            teacher_id = int(input("Enter teacher ID: "))
            course_id = int(input("Enter course ID: "))
            teacher = next((t for t in school.teachers if t.person_id == teacher_id), None)
            course = next((c for c in school.courses if c.course_id == course_id), None)
            if teacher and course:
                school.assign_teacher_to_course(teacher, course)
                print(f"Teacher {teacher.name} assigned to {course.course_name}.")
            else:
                print("Teacher or course not found.")

        elif choice == '6':
            course_id = int(input("Enter course ID: "))
            course = next((c for c in school.courses if c.course_id == course_id), None)
            if course:
                school.view_students_in_course(course)
            else:
                print("Course not found.")

        elif choice == '7':
            student_id = int(input("Enter student ID: "))
            student = next((s for s in school.students if s.person_id == student_id), None)
            if student:
                school.view_courses_for_student(student)
            else:
                print("Student not found.")

        elif choice == '8':
            course_id = int(input("Enter course ID: "))
            course = next((c for c in school.courses if c.course_id == course_id), None)
            if course:
                school.calculate_average_grade_for_course(course)
            else:
                print("Course not found.")

        elif choice == '9':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 9.")


if __name__ == "__main__":
    main()
