# Створити клас Rectangle:
# -він має приймати дві сторони x,y
# -описати поведінку на арифметичні методи:
#   + сума площ двох екземплярів ксласу
#   - різниця площ двох екземплярів ксласу
#   == площ на рівність
#   != площ на не рівність
#   >, < меньше більше
#   при виклику метода len() підраховувати суму сторін

# class Rectangle:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'{self.x} {self.y}'
#
#     def __add__(self, other):
#         return self.x * self.y + other.x * other.y
#
#     def __sub__(self, other):
#         return self.x * self.y - other.x * other.y
#
#     def __eq__(self, other):
#         return self.x * self.y == other.x * other.y
#
#     def __lt__(self, other):
#         return self.x * self.y < other.x * other.y
#
#     def __len__(self):
#         return (self.x + self.y) * 2
#
#
# rec = Rectangle(2, 3)
# rec2 = Rectangle(4, 5)
#
# print(rec + rec2, "add")
# print(rec - rec2, "sub")
# print(rec == rec2, "eq")
# print(rec < rec2, "lt")
# print(len(rec), "len")
#
# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір ноги
# у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок, та шукати ту саму
#
# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення

# class Human:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Prince(Human):
#
#     def __init__(self, name, age, size):
#         super().__init__(name, age)
#         self.size = size
#
#     def search(self, arr_cinderellas):
#         c = [i for i in arr_cinderellas if i.size == self.size]
#         print(c)
#
#     def __str__(self):
#         return f'{self.name} {self.age} {self.size}'
#
#
# class Cinderella(Human):
#     count = 0
#
#     def __init__(self, name, age, size):
#         super().__init__(name, age)
#         self.size = size
#         Cinderella.count += 1
#
#     def __str__(self):
#         return f'{self.name} {self.age} {self.size}'
#
#     def __repr__(self):
#         return self.__str__()
#
#     @classmethod
#     def count_Cinderellas(cls):
#         print(cls.count)
#
#     # @staticmethod
#     # def count_cinderellas():
#     #     nonlocal count
#     #     print(count)
#
#
# arr_cinderellas = [
#     Cinderella("A", 23, 23),
#     Cinderella("B", 24, 2),
#     Cinderella("C", 25, 30),
#     Cinderella("D", 26, 37),
# ]
#
# prince = Prince("n", 34, 37)
#
# prince.search(arr_cinderellas)
# print(prince)
# Cinderella.count_Cinderellas()


# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
# 3) Створити клас Main в якому буде: - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають
# є класом Book або Magazine інакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу
#
# Приклад:
#
# Main.add(Magazine('Magazine1'))
# Main.add(Book('Book1'))
# Main.add(Magazine('Magazine3'))
# Main.add(Magazine('Magazine2'))
# Main.add(Book('Book2'))
#
# Main.show_all_magazines()
# print('-' * 40)
# Main.show_all_books()
#
# для перевірки ксассів використовуємо метод isinstance, приклад:
#
# user = User('Max', 15)
# shape = Shape()
#
# isinstance(max, User) -> True
# isinstance(shape, User) -> False

from abc import ABC, abstractmethod


class Printable(ABC):

    @abstractmethod
    def print(self):
        pass


class Book(Printable):

    def print(self):
        print(f'{self.name}+ book')

    def __init__(self, name):
        self.name = name


class Magazine(Printable):

    def print(self):
        print(f'{self.name}')

    def __init__(self, name):
        self.name = name


class Main:
    __printable_list: list[Book | Magazine] = []

    @classmethod
    def add(cls, item: Book | Magazine) -> None:
        if isinstance(item, Magazine) or isinstance(item, Book):
            cls.__printable_list.append(item)

    @classmethod
    def show_all_magazines(cls) -> None:
        magazine = [item for item in cls.__printable_list if isinstance(item, Magazine)]
        for i in magazine:
            i.print()

    @classmethod
    def show_all_books(cls) -> None:
        book = [item for item in cls.__printable_list if isinstance(item, Book)]
        for i in book:
            i.print()


Main.add(Magazine('Magazine1'))
Main.add(Book('Book1'))
Main.add(Magazine('Magazine3'))
Main.add(Magazine('Magazine2'))
Main.add(Book('Book2'))

Main.show_all_magazines()
print('-' * 40)
Main.show_all_books()