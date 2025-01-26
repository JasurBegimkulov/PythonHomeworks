class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Amphibian(Animal):
    def __init__(self, name):
        super().__init__(name, "Amphibian")

    def swim(self):
        print(f"{self.name} is swimming.")

    def breathe_underwater(self):
        print(f"{self.name} is breathing underwater.")

class Frog(Amphibian):
    def jump(self):
        print(f"{self.name} is jumping.")

class Salamander(Amphibian):
    def regenerate_tail(self):
        print(f"{self.name} is regenerating its tail.")

class Caecilian(Amphibian):
    def burrow(self):
        print(f"{self.name} is burrowing underground.")

if __name__ == "__main__":
    print("Welcome to the Amphibian Farm!")

    frog = Frog("Freddy")
    salamander = Salamander("Sally")
    caecilian = Caecilian("Cecil")

    frog.eat()
    frog.jump()
    
    salamander.sleep()
    salamander.regenerate_tail()

    caecilian.swim()
    caecilian.breathe_underwater()
    caecilian.burrow()