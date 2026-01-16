class Animal:
  def __init__(self, name: str, age: int):
    self.name = name
    self.age = age

  def speak(self) -> str:
    return f"{self.name} macht ein Geräusch."

  def info(self) -> str:
    return f"{self.name}, {self.age} Jahre"

class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str = "unbekannt"):
        super().__init__(name, age)
        self.breed = breed

    def speak(self) -> str:
        return f"{self.name} bellt."

    def fetch(self, item: str) -> str:
        return f"{self.name} bringt {item} zurück."

if __name__ == "__main__":
  a = Animal("Leon", 5)
  d = Dog("Julian", 3, "Labrador")

  print(a.info())
  print(a.speak())

  print(d.info())
  print(d.speak())
  print(d.fetch("Ball"))