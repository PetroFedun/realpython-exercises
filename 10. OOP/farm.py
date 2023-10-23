# Требования задачи открыты для интерпретации, но постарайтесь придержи­
# ваться следующих рекомендаций.
# 1.В программе должно быть по крайней мере четыре класса: родительский
# класс Animal и не менее трех производных классов животных, наследу­ющих от Animal.
# 2.Каждый класс должен содержать несколько атрибутов и по крайне 
# мере один метод, моделирующий поведение, присущее конкретному
# животному или всем животным, -они должны ходить, бегать, есть, спать и т. д.
# 3.Не усложняйте. Используйте наследование. Предусмотрите воэможность
# вывода подробной информации о животных и их поведении.

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        return f"{self.name} is eating."

    def sleep(self):
        return f"{self.name} is sleeping."

    def info(self):
        return f"{self.name} is a {self.species}."

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def bark(self):
        return f"{self.name} is barking."

    def info(self):
        return f"{super().info()} It's a {self.breed}."

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Cat")
        self.color = color

    def meow(self):
        return f"{self.name} is meowing."

    def info(self):
        return f"{super().info()} It's {self.color}."

class Fish(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Fish")
        self.color = color

    def swim(self):
        return f"{self.name} is swimming."

    def info(self):
        return f"{super().info()} It's {self.color}."

dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Tabby")
fish = Fish("Nemo", "Orange")

print(dog.info())
print(dog.eat())
print(dog.bark())
print(dog.sleep())

print(cat.info())
print(cat.eat())
print(cat.meow())
print(cat.sleep())

print(fish.info())
print(fish.eat())
print(fish.swim())
print(fish.sleep())
