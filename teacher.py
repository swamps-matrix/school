# teacher.py
class Teacher:
    def __init__(self, teacher_id, name, subject):
        self.teacher_id = teacher_id
        self.name = name
        self.subject = subject

    def __str__(self):
        return f"Teacher ID: {self.teacher_id}, Name: {self.name}, Subject: {self.subject}"
