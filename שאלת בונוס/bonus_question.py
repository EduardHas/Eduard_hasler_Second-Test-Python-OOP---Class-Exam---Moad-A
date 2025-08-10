from abc import ABC, abstractmethod

# Abstract class Animal
class Animal(ABC):
    def __init__(self, legs: int):
        self.legs = legs

    def walk(self):
        print(f"This animal walks on {self.legs} legs.")

    @abstractmethod
    def eat(self):
        pass

# Pet interface
class Pet(ABC):
    @abstractmethod
    def getName(self) -> str:
        pass
    @abstractmethod
    def setName(self, name: str):
        pass
    @abstractmethod
    def play(self):
        pass

# Spider class

class Spider(Animal):
    def __init__(self):
        super().__init__(8)

    def eat(self):
        print("Spider eats insects.")

# Cat class
class Cat(Animal, Pet):
    def __init__(self, name: str = ""):
        super().__init__(4)
        self.name = (name
    @property)
        def getName(self) -> str:
          return (self.name
    @getName.setter)
        def setName(self, name: str):
            self.name = name
        def play(self):
            print(f"{self.name} is playing with a ball of yarn.")
        def eat(self):
            print(f"{self.name} eats cat food.")

# Fish class
class Fish(Animal, Pet):
    def __init__(self):
        super().__init__(0)
        self.name = ""
    def getName(self) -> str:
        return self.name
    @property
    def setName(self, name: str):
        self.name = name
    @setName.setter
    def setName(self, name: str):
        self.name = name
    def play(self):
        print(f"{self.name} is swimming around playfully.")

    def walk(self):
        print("Fish can't walk!")
    def eat(self):
        print(f"{self.name} eats fish flakes.")