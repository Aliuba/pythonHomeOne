# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

# st = 'as 23 fdfdg544'
# l=[int(i) for i in st if i.isdigit()]
# print(*l, sep=',')

# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

# st = 'as 23 fdfdg544 34'
# st1= "".join((i.replace(i, "") if i.isalpha() else i for i in st)).split()
#
# print(*st1, sep=",")
#
# list comprehension
#
# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

# greeting = 'Hello, world'
# l=[i for i in greeting.upper()]
# print(l)

# 2) з диапозону від 0-50 записати тільки непарні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

# l=[i**2 for i in range(50) if i%2==1]
# print(l)

# function
#
# - створити функцію яка виводить ліст
#
# def list_print(list):
#     print(list)
#
# list_print([1,2,3])
#
# - створити функцію яка приймає три числа та виводить та повертає найбільше.

# def max_3(a,b,c):
#     m=max(a,b,c)
#     print(m)
#     return m
#
# max_3(1,4,6)
#
# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

# def max_many(*args):
#     m=max(args)
#     print(m)
#     return min(args)
#
# max_many(1,4,6,3,4,5,6,7)

# - створити функцію яка повертає найбільше число з ліста

# def max_list(list):
#    return max(list)
#
# max_list([1,2,3,4])
#
# - створити функцію яка повертає найменьше число з ліста

# def min_list(list):
#    return min(list)
#
# min_list([1,2,3,4])

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

# def sum_list(list):
#     return sum(list)
#
# print(sum_list([1,2,3]))

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

# def average(list):
#     return sum(list)/len(list)
#
# print(average([1,2,3]))

# 1)Дан list:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]
#   - знайти мін число
#   - видалити усі дублікати
#   - замінити кожне 4-те значення на 'X'
# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
# 3) вывести табличку множення за допомогою цикла while
# 4) переробити це завдання під меню

num_list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]


#
def one(arr):
    print(min(arr))


#
def two(arr):
    print(set(arr))


#
def three(arr):
    for i, item in enumerate(arr):
        if i % 4 == 0:
            arr[i] = "x"
    print(arr)


#
#
#
# print(num_list)

# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції


def square(n):
    i = 0
    while i < n:
        if i == 0 or i == n - 1:
            print("*" * n)
        else:
            print("*" + " " * (n - 2) + "*")
        i = i + 1


# square(6)


# 3) вывести табличку множення за допомогою цикла while

def five():
    i = 1
    j = 1

    while i < 10:
        string = ""
        while j < 10:
            string = string + str(i * j) + " "
            j = j + 1
        print(string)
        j = 1
        i = i + 1


# 4) переробити це завдання під меню
def menu():
    k = 0
    while int(k) < 6:
        print("Данo list: list = [22, 3,5,2,8,2,-23, 8,23,5]")
        print("1)-знайти мін число")
        print("2)-видалити усі дублікати")
        print("3)-замінити кожне 4-те значення на 'X'")
        print("4) вивести на екран пустий квадрат з  *  сторона якого вказана як агрумент функції")
        print("5) вывести табличку множення за допомогою цикла while")

        print("6) вихід")
        k = input("виберіть дію:")

        if k == "1":
            one(num_list)
            continue

        elif k == "2":
            two(num_list)
            continue
        elif k == "3":
            three(num_list)
            continue
        elif k == "4":
            square(4)
            continue
        elif k == "5":
            five()
            continue
        else:
            k == "6"

menu()
