# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи

# def notebook():
#     todo_list = []
#
#     def add_todo(todo):
#         nonlocal todo_list
#         todo_list.append(todo)
#
#     def get_all():
#         nonlocal todo_list
#         return todo_list
#
#     return add_todo, get_all


# l= notebook()
# l[0]("jjjjj")
# print(l[1]())

# add, get = notebook()
#
# add("get up")
# add("wash dishes")
# print(get())

from typing import Callable


# def notebook() -> tuple[Callable[[str], None], Callable[[None], list[str]]]:

# def notebook():
#     todo_list: list[str] = []
#
#     def add_todo(todo) -> None:
#         nonlocal todo_list
#         todo_list.append(todo)
#
#     def get_all() -> list[str]:
#         nonlocal todo_list
#         return todo_list
#
#     return add_todo, get_all
#
#
# add, get = notebook()
# add('do that')
# add('do that')
# add('do that')
# add('todo')
#
# print(get())


# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#
# Приклад:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'


# def expanded_form(number) -> str:
#     l: list[str] = [item + "0" * (len(str(number)) - 1 - i) for i, item in enumerate(str(number)) if item != "0"]
#     st: str = ""
#     for i in l:
#         st += str(i)
#         st += " + "
#     st = st[:-3]
#     return st
#
#
# print(expanded_form(2050602))

# варіант з лекції

# def expanded_form(number: int) -> str:
#     st: str = str(number)
#     return " + ".join(ch + "0" * (len(st) - 1 - i) for i, ch in enumerate(st) if ch != "0")+f" = {st}"
#
#
# print(expanded_form(23502))
#
# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція
# продекорована цим декоратором, та буде виводити це значення після виконання функцій


def decor(func):
    count = 0

    def inner():
        nonlocal count
        func()
        count += 1
        print(count)

    return inner


@decor
def count_func():
    print("Hello")


count_func()
count_func()
count_func()
count_func()
