class Student:
    school = "Sunrise School"

    def introduction(self):
        """A method: a function inside the class. self is the object it is called on."""
        return "Hi, I am a student at " + self.school
    
    def details(self):
        return f"My name is {self.name} and I study in grade {self.grade}."
    
anna = Student()
anna.name = input("Student name? ")
anna.grade = int(input("Grade? "))

print(anna.introduction())
print(anna.details())
print(Student.details(anna))

ryan = Student()
ryan.name = "Ryan"
ryan.grade = 9
print(ryan.details())
