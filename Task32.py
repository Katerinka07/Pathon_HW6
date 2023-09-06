'''
Задача 32: Определить индексы элементов массива (списка), значения которых 
принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного
максимума)
'''


def index_elements(lst, minn, maxx):
    result = []
    for i in range(len(lst)):
        if minn <= lst[i] <= maxx:
            result.append(i)
    return result

list_1 = [int(input(f'Введите {i + 1} элемент списка: ')) for i in range(int(input('Введите количество элементов списка:')))]
print(list_1)
min_el = int(input('Введите минимальный элемент: '))
max_el = int(input('Введите максимальный элемент: '))
index = index_elements(list_1, min_el, max_el)
print(index)