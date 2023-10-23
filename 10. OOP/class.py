# 1. Измените класс Dog и включите в него третий атрибут экземпляра с име­
# нем coat_color, в котором будет храниться цвет шерсти собаки в виде
# строки. Сохраните новый класс в файле и протестируйте его, добавив
# следующий фрагмент в конец программы:
# philo = Dog("Philo", 5, "brown")
# print(f"{philo.name}'s coat is {philo.coat_color}.")
# Программа должна выводить следующий результат:
# Philo's coat is brown

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


philo = Dog("Philo", 5, "brown")
print(f"{philo.name}'s coat is {philo.coat_color}.")  # Philo's coat is brown

# 2. Создайте класс Car с двумя атрибутами экземпляров: .color для хранения
# цвета машины в виде строки и .mileage для хранения пробега в милях
# в виде целого числа. Создайте два объекта Car - синюю машину с про­
# бегом 20 ООО и красную с пробегом 30 ООО. Выведите данные на каждую
# машину. Результат должен выглядеть так:
# The blue car has 20000 miles.
# The red car has 30000 miles.

# 3. Измените класс Car и добавьте в него метод экземпляра .drive(), который
# получает числовой аргумент и прибавляет его к атрибуту . mileage. Убе­
# дитесь в том, что ваше решение работает; создайте экземпляр с нулевым
# пробегом, вызовите .drive(100) и выведите атрибут .mileage, чтобы
# убедиться в том, что он принял значение 100.

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    
    def drive(self, a):
        self.mileage = self.mileage + a
        

c1 = Car('blue', 20000)
c2 = Car('red', 30000)
c1.drive(10000)

print(f'The {c1.color} car has {c1.mileage} miles')
print(f'The {c2.color} car has {c2.mileage} miles')

# 4. Создайте класс GoldenRetriever, наследующий от класса Dog. Задайте
# аргументу sound метода GoldenRetriever. speak () значение по умолча­
# нию "Bark".

class GoldenRetriever(Dog):
    def speak(self, sound='Bark'):
        return f"{self.name} says {sound}" 

d1 = GoldenRetriever("HHH", 4, "brown")
print(d1.speak())

# 5. Напишите класс Rectangle, представляющий прямоугольник. Экзем­
# пляры класса должны создаваться с двумя атрибутами: . length и . width.
# Добавьте в класс метод . аrea (), который возвращает площадь прямо­
# угольника (length * width).
# Затем напишите класс Square, представляющий квадрат. Этот класс дол­
# жен наследовать от класса Rectangle и создаваться с одним атрибутом
# . side_length. Протестируйте класс Square: создайте экземпляр Square
# с атрибутом . side_length, равным 4. Вызов . area () должен возвращать 16.242
# Задайте свойству . width вашего экземпляра Square значение 5. Затем
# снова вызовите . area (). Метод должен вернуть значение 20.
# Этот пример показывает, что наследование классов не всегда наилучшим
# образом моделирует отношения между подмножествами. В математике
# любой квадрат является прямоугольником, но в компьютерных про­
# граммах это не всегда так.
# Хорошо продумывайте варианты поведения, чтобы они выполняли
# именно то, что вы задумали, и используйте иерархии классов с осто­рожностью.

class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

square = Square(4)
print(square.area())

square.width = 5
print(square.area())
    
        
