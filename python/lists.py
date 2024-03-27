class StudentDatabase:
    def __init__(self):
        self.head = None

    def add_student(self, student_id, name, age, gpa):
        new_student = Student(student_id, name, age, gpa)
        if not self.head:
            self.head = new_student
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_student

        def display_students(self):
            current = self.head
            while current:
                print(f"Student ID: {current.student_id}, Name: {current.name}, Age: {current.age}, GPA: {current.gpa}

