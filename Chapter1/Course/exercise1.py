
class Student:
    name = None
    age = None
    tel = None
    def say_hi(self):
        print(f"Bonjour je m'appelle {self.name} et j'ai {self.age} ans.")

    def say_tel(self):
        print(f"Mon numéro c'est {self.tel}.")

stu = Student()
stu.name = 'Laurent'
stu.age = 15
stu.tel = '01 23 45 67 89'
stu.say_hi()
stu.say_tel()



