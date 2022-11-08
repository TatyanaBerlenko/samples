number = 10  # Создание числа
string = "Hello, World"  # Создание строки
fruits = ['apple', "orange", "banana"]  # Создание списка строк


def magic_sum(a, b,
              c=100):  # Определение функции с именем magic_sum и аргументами a, b, c. с имеет значение по умолчанию 100
    result = a + b + c
    print("{} + {} + {} = {}".format(a, b, c, result))
    return result  # Возврат результата работы функции после вызова


magic_sum(1, 2)  # вызов функции со значениями аргументов a == 1, b == 2, c == 100
magic_sum(1, 2, 3)  # вызов функции со значениями аргументов a == 1, b == 2, c == 3
magic_sum(number, 15)  # вызов функции со значениями аргументов a == 10, b == 15, c == 100


class Person:  # Определение класса с именем Person
    def __init__(self, name, age):  # Определение конструктора класса Person. Задаются поля объекта name и age
        self.name = name
        self.age = age

    def __str__(self):  # Определение метода класса Person. Метод нужен, чтобы задать вывод объекта с помощью print
        return "Name: {}, Age: {}".format(self.name, self.age)


anna = Person('Anna', 20)  # Создание объекта класса Person
print(anna)  # Вывод объекта класса Person
