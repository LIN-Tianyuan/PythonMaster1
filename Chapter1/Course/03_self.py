class Student:
    name = None
    age = None

    def say_hi(self):
        print(f"Bonjour à tous, je m'appelle {self.name} et j'ai {self.age} ans.")

    def say_hi2(self, msg):
        print(f"Bonjour à tous, {msg}")


stu = Student()
stu.name = 'Maxime'
stu.age = 12
stu.say_hi()
stu.say_hi2("je suis là.")
