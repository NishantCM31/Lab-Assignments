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


# Test the School Management System
if __name__ == "__main__":
    # Create a school
    school = School("Greenfield High")

    # Create students
    student1 = Student("Alice Johnson", 16, 1001)
    student2 = Student("Bob Smith", 17, 1002)

    # Create teachers
    teacher1 = Teacher("Ms. Rose", 35, 2001, "Mathematics")
    teacher2 = Teacher("Mr. Thompson", 40, 2002, "Physics")

    # Create courses
    course1 = Course("Algebra", 3001)
    course2 = Course("Physics", 3002)

    # Add students, teachers, and courses to the school
    school.add_student(student1)
    school.add_student(student2)
    school.add_teacher(teacher1)
    school.add_teacher(teacher2)
    school.add_course(course1)
    school.add_course(course2)

    # Enroll students in courses
    school.enroll_student_in_course(student1, course1)
    school.enroll_student_in_course(student2, course1)
    school.enroll_student_in_course(student2, course2)

    # Assign teachers to courses
    school.assign_teacher_to_course(teacher1, course1)
    school.assign_teacher_to_course(teacher2, course2)

    # Assign grades to students
    student1.grade = 85
    student2.grade = 90

    # View students in a course
    school.view_students_in_course(course1)

    # View all courses a student is enrolled in
    school.view_courses_for_student(student2)

    # Calculate the average grade for a course
    school.calculate_average_grade_for_course(course1)

    # View the course details
    print(course1)
