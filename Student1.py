class Student:
    print("Python read the Student blueprint.")
    school = "Sunrise School"

    grade = 10
    print("Class variable grade:", grade)
    
anna = Student()
ryan = Student()
print("anna is a", type(anna))

print("anna's school:", anna.school, "| ryan's grade:", ryan.grade)
new_grade = int(input("New class grade?"))
Student.grade = new_grade
print("After changing the class grade: anna", anna.grade, "| ryan", ryan.grade)

anna.grade = 12
print("anna", anna.grade, "| ryna", ryan.grade, "| Student", Student.grade)