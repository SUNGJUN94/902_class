class Student:
    def __init__(self, name , grade):
        self.name = name
        self.grade = grade

student1 = Student("sam", 10)
student2 = Student("robin", 11)

print(student1.name , student1.grade)
print(student2.name , student2.grade)
print("*"*50)
