class Student:
    def __init__(self):
        self.MCAS1 = []
        self.MCAS3 = []

    def add_to_MCAS1(self, student, position=None):
        if position:
            self.MCAS1.insert(position, student)
        else:
            self.MCAS1.append(student)

    def add_to_MCAS3(self, student):
        self.MCAS3.append(student)

    def search_in_MCAS1(self, student_name):
        if student_name in self.MCAS1:
            return True
        else:
            return False

    def display_all_students(self):
        all_students = self.MCAS1 + self.MCAS3
        print("All Students in MCA:", all_students)


student_data = Student()
student_data.add_to_MCAS1("Alice")
student_data.add_to_MCAS1("Bob")
student_data.add_to_MCAS1("Chris", position=2)  
student_data.add_to_MCAS1("David")
student_data.add_to_MCAS3("Charlie")
student_data.add_to_MCAS3("Emily")



student_data.display_all_students()
