'''Список методы списков цикл for. Кортеж'''

# список - изменяемый индексируемый, упорядотечный, итерируемый.
# [] ->литеры (выражения которые создают обькты определенного тип данных) 

#list_ = [1, 2, 3, 'hello', [1, 2, 3], {1: 'a'}]
#print(list_[0])
#print(list_[4][0])

# name = input('Введите имена через пробел: ')
# guests = input('Введите имена через пробел: ')

'''Создание списков'''
#1. list(iterable)
# a = 'hello'
# print(list(a))
# range() -> возвращает последовательность элементов
# print(list(range(1, 10, 2)))

# 2. [] -> литералы
# list_ = []
# print(type(list_))
# list_ = [1] * 6
# print(list_)

# range([start]), stop, ([step]) -> возвращает последовательность чисел по умолчанию начинает с 0 последовательность каждый раз увеличивается на 1  и останавливается перед заданным числом (stop)

'''Метод списков'''
# del -> удаление элемента
# list_ = [1, 2, 3]
# del list_[0]
# print(list_)

# .append() -> добавление элемента в конец списка
# list_ = [1, 2, 3]
# print(id(list_))
# list_ .append('hello')
# print(list_)
# print(id(list_))

# .extend(element[iterable]) -> расширает список добавляя в конец все элементы списка
# list_ = [1, 2, 3]
# list_ .extend([1, 2, 3])
# list_.append([1, 2, 3])
# print(list_)


# .insert(index, element) -> добавляет элемент по индексу

# list_ = [1, 2, 3]
# list_.insert(1, 9)
# print(list_)

# .index(element,[start], [end]) -> возвращает индекс элемента
# list_ = [1, 2, 3, 5, 6, 7]
# print(list_.index(3, 2))

# .count(element) -> считает количество вхождений element в списке
# list_ = [1, 2, 3, 3, 3, 2, 3, 3, 'hello']
# print(list_count('l'))

# print(len(list_)) # количество элементов в списке или длина спика

# .pop(index) -> удаляет элемент по index, если index не указан то удалит с конца
# list_ = [1, 2, 3]
# a = list_.pop(0)
# print(list_, a)

# .remove(element) -> удаляет первый элемент в списке

# list_ = [1, 2, 3, 4, 3, 4, 5, 6, 7]
# list_.remove('hello')
# print(list_)

# .reverse() -> переворачивае  список
# # [:: -1]
# list_ = [1, 2,3,3,3,4,3,4 5,6, 'helli', 'h']
# list_ .reverse(
# # print(list_[:: -1])

# .sort() -> сортирует список
# list_.sort()
# print(list_)
# .copy() -> поверхносное копирование

# new_list = list_.copy()
# new_list.appaend(1)
# print(list_)
# print(new_list)

'''Цикл for'''
# цикл - это блок кода, который повторяется несколько раз

# for -> работает с итерируемыми обьктами, заканчивает когда даходит до конца

# list_ = [1, 2, 3, 4, 5]
# # print(list_[0])
# for element in list_:
#     print(element)

# for i in 'hello':
#     print(i)

# i = 10
# print(i)

# for i in range(11):
#     print(i)

# for i in range(11):
#     if i == 3:
#         print(i)
#     elif i == 5:
#         print('отлично')
#     else:
#         print('hello')

'''Tuple (кортеж)'''
# tuple_ = (1, 2, 3)
# print(dir(tuple_))
# print(tuple('hello')
# (,) -> литералы

# tuple_ = 1, 2, 3
# print(type(tuple_))

'''Методы tuple'''
# .count(element) ->
# tuple_ = (1, 2, 3, 4, 1, 2, 1, 1)
# print(tuple_.count(1))

# .index(element) -> возвращает index элемент

# print(tuple_.index(2))