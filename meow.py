class Parrot:
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age
woo = Parrot("Woo", 5)
print("Woo name is " + woo.name)   
print("Woo age is " + str(woo.age))     
blu = Parrot("Blu", 10)
print("Blu name is " + blu.name)
print("Blu age is " + str(blu.age))