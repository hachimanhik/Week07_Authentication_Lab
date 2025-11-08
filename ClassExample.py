class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def personDetails(self):
        print(f"Name: {self.name} Age: {self.age}")
        print(f"Address: {self.address}")

class Student(Person):
    # course, misis no, year of study
    def __init__(self,name, gender, age, address, course, misis, academic_year):
        super().__init__(name, gender, age, address)
        self.course = course
        self.misis = misis
        self.year = academic_year
        def personDetails(self):
            super().personDetails()
            print(f"Course: {self.course}" "Academic Year: {self.academic_year}")
            print(f"Misis: {self.misis}")
