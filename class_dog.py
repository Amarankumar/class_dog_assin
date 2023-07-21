class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"{self.name} is {self.age} years old.")

    def get_info(self):
        print(f"{self.name}'s coat color is {self.coat_color}.")


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color, activity_level):
        super().__init__(name, age, coat_color)
        self.activity_level = activity_level

    def bark(self):
        print(f"{self.name} is barking!")

    def fetch(self):
        print(f"{self.name} is fetching the ball!")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color, weight):
        super().__init__(name, age, coat_color)
        self.weight = weight

    def snore(self):
        print(f"{self.name} is snoring loudly!")

    def eat(self):
        print(f"{self.name} is eating a bone!")


if __name__ == "__main__":
    # Create a Dog object and implement its functionalities
    dog1 = Dog("Buddy", 3, "Brown")
    dog1.description()
    dog1.get_info()

    # Create a JackRussellTerrier object and implement its functionalities
    jack_russell = JackRussellTerrier("Rusty", 2, "White and Brown", "High")
    jack_russell.description()
    jack_russell.get_info()
    jack_russell.bark()
    jack_russell.fetch()

    # Create a Bulldog object and implement its functionalities
    bulldog = Bulldog("Rocky", 4, "Grey", "Heavy")
    bulldog.description()
    bulldog.get_info()
    bulldog.snore()
    bulldog.eat()
