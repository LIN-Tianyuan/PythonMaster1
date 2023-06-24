class Student:
    name = None
    age = None
    address = None

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


for element in range(5):
    print(f"Actuellement en train de saisir le {element + 1}ème élève, 5 élèves au total doivent être saisis.")
    name = input("Veuillez saisir le nom de l'élève: ")
    age = input("Veuillez saisir l'âge de l'élève: ")
    address = input("Veuillez saisir l'address de l'élève: ")
    stu = Student(name, age, address)
    print(f"La saisie des informations sur l'étudiant {element + 1} est complète avec "
          f"les informations suivantes: [Nom : {stu.name}, Age : {stu.age},"
          f" Address : {stu.address}].")
