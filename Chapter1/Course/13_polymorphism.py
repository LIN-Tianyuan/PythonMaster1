class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("Woof woof woof")


class Cat(Animal):
    def speak(self):
        print("Miaou Miaou Miaou")


def make_noise(animal: Animal):
    animal.speak()


dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)