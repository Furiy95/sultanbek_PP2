class animal:
    def __init__(self, name, age):
        self.name = name  
        self.age = age

    def sound(self):
        print(f"{self.name} makes the sound {self.sound}") 


class dog(animal):
    def __init__(self, name, age, sound):
        super().__init__(name, age)
        self.sound = sound

    def sound(self):
        super().sound()
        print("Woof woof")


class cat(animal):
    def __init__(self, name, age, sound):
        super().__init__(name, age)
        self.sound = sound

    def sound(self):
        super().sound()
        print("Meow meow")

n = animal("Dog",  9)
d = dog("Rex", 5, "Woof")
c = cat("kit", 4, "Meow")

print(n.name, n.age)
print(d.name, d.age, d.sound)
print(c.name, c.age, c.sound)
