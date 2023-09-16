class Student:
    name = None # Nom de l'élève
    age = None  # Âge de l'élève

    def say_hi(self):
        print(f"Bonjour à tous, je m'appelle {self.name} et j'ai {self.age} ans.")


stu = Student()
stu.name = 'Alex'
stu.age = 18
stu.say_hi()

stu2 = Student()
stu2.name = 'Lucas'
stu2.age = 13
stu2.say_hi()

stu3 = Student()
stu3.name = 'Laurent'
stu3.age = 1
stu3.say_hi()

stu4 = Student()
stu4.name = 'Maxime'
stu4.age = 12
stu4.say_hi()