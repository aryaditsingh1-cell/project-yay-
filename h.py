class familyguy:
    def __init__(self,name, job,height):
        self.name = name
        self.job = job
        self.height = height
    def show_traits(self):
        print(f"Name: {self.name}")
        print(f"Job: {self.job}")
        print(f"Height: {self.height} cm")
class baby(familyguy):
    def __init__(self,name, job,height, age):
        super().__init__(name, job, height)
        self.age = age
    def show_traits(self):
        print(f"Name: {self.name}")
        print(f"Job: {self.job}")
        print(f"Height: {self.height} cm")
        print(f"Age: {self.age} years")
        super().show_traits()
    def favorite_thing_to_do(self, hobby):
        print(f"{self.name} loves to {hobby}.")
child = baby("Stewie", "Baby Genius", 30, 1)
child.show_traits()
child.favorite_thing_to_do("invent gadgets")
print("lets check if stevie is adopted or not", issubclass(baby, familyguy))
if issubclass(baby, familyguy) == True:
    print("Stewie is adopted")
else:
    print("Stewie is not adopted phew")