# course.py
class Course:
    def __init__(self, course_code, course_name, teacher, students):
        self.course_code = course_code
        self.course_name = course_name
        self.teacher = teacher
        self.students = students

    def __str__(self):
        return f"Course Code: {self.course_code}, Name: {self.course_name}, Teacher: {self.teacher}, Students: {self.students}"
