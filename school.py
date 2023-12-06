# school.py
from student import Student
from teacher import Teacher
from course import Course
from utils import display_menu, get_user_choice

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

    def display_info(self):
        print(f"\nSchool Name: {self.name}")
        print("\nStudents:")
        for student in self.students:
            print(student)

        print("\nTeachers:")
        for teacher in self.teachers:
            print(teacher)

        print("\nCourses:")
        for course in self.courses:
            print(course)

    def run(self):
        while True:
            display_menu()
            choice = get_user_choice()

            if choice == "1":
                student_id = input("Enter student ID: ")
                name = input("Enter student name: ")
                age = input("Enter student age: ")
                student = Student(student_id, name, age)
                self.add_student(student)

            elif choice == "2":
                teacher_id = input("Enter teacher ID: ")
                name = input("Enter teacher name: ")
                subject = input("Enter subject: ")
                teacher = Teacher(teacher_id, name, subject)
                self.add_teacher(teacher)

            elif choice == "3":
                course_code = input("Enter course code: ")
                course_name = input("Enter course name: ")
                teacher = input("Enter teacher ID for the course: ")
                students = input("Enter student IDs for the course (comma-separated): ").split(",")
                course = Course(course_code, course_name, teacher, students)
                self.add_course(course)

            elif choice == "4":
                self.display_info()

            elif choice == "5":
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please try again.")
