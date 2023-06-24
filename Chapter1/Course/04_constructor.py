class Student:
    name = None
    age = None
    tel = None

    """
    1.La méthode __init__ est automatiquement exécutée 
    lors de la construction de la classe.
    2.Les paramètres passés lors de la construction d'une classe
    sont automatiquement fournis à la méthode __init__.
    """
    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("La classe student crée un objet.")

    def say_hi(self):
        print(f"Bonjour je m'appelle {self.name} et j'ai {self.age} ans.")

stu = Student("Laurent", 15, "0123456789")
stu.say_hi()
print("-----------")
stu1 = Student("Lucas", 13, "08287378723")
stu1.say_hi()
print("-----------")
stu2 = Student("Maxime", 12, "27262827282")