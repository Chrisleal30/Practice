## A simple attempt to model a dog.

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is sitting now.")

    def roll_over(self):
        print(f"{self.name} rolled over!")

smeagol = Dog("Smeagol", 7)

print(smeagol.age)
print(smeagol.name)
smeagol.roll_over()