class Student:
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    """Contrôler le comportement des conversions de classes en chaînes de caractères"""
    def __str__(self):
        return f"name = {self.name}, age = {self.age}"

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


student = Student("Alex", 18)

# student.name = "Alex"
# student.age = 18
print(student)
"""
print(student.name)
print(student.age)
print(student)

student1 = Student("Alex", 18)
student2 = Student("Alex", 18)
# print(student2 < student1)
# print(student1 <= student2)
# print(student2 > student1)
# print(student2 >= student1)
print(student1 == student2)
"""