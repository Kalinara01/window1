'''Встроенные функции'''
# print
# len
# input
# divmod
# id
# range

'''lamba''' # анонимная функция (та же самая функция только без имени)

# def func(a, b): return a + b
# print(func(3, 5))

# lambda парамеиры: что функция должна возвращать 

# a = lambda a, b: a + b
# print(a(4, 6))

# x = lambda a, b, c: (a * b)%c
# print(x(2, 66, 7))

# x = lambda a, b, c: (a, b, c)
# print(x(2, 66, 7))

# get_keys = lambda dict_: dict_.keys()
# dict = {1: 'hello', 'a': 7, 'n': 9}
# print(get_keys(dict))

# pow_ = lambda x : x ** 2 
# print(pow_(9))

# def pow_(x):
#     return(pow_(9))


# map(func, iterable) - она прменяет func к каждому элементу итерируемого объекта

# map_ = map(int, ['1', '2', '3'])
# print(list(map_))

# list_ = [1, 2, 3, 4]
# def f(number):
#     return number ** 2
# a = map(f, list_)
# print(list(a))

# list_ = [1, -3, 100, -44]
# list_2 = list(map(lambda x: x < 0, list_))
# print(list_2)

# func = lambda num: num + 1
# res = []
# list_ = [1, 2, 3, 4, 1, 6, 7, 5]
# for i  in list_:
#     res.append(func(i))
# print(res)

# filter(func, iterable) - возвращает генератор, из элементов итерируемого объекта которые прощли фильтр(проверку)
# фильтрует если функция возвращает True

# def filter_nums(number):
#     if number % 2 == 0:
#         return True

# res = list(filter(filter_nums, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(res)

# list_ = ['Эртай', 'Тима', 'Айкол', 'Нуркамила', 'Айбек']
# def starswith_vowel(name):
#     vowels = 'АЕИУОЯЮЫЭ'
#     # print(tuple(vowels))
#     return name.upper().startswith(tuple(vowels))
# res = list(filter(lambda name: name[0].upper() in vowels, list))
# print(res)


# reduce - нужно импортировать из библиотеки functools, возвращает один результат
from functools import reduce 
# (sum(),min(), max())
# reduce

# list_ = [1, 2, 3, 4, 5, 6]
# res = reduce(lambda x, y: x + y, list_)
# print(res)


# list_ = [1, 2, 3, 4, 5, 6, -34, -100]
# min_ = reduce(lambda small, x: small if(small < x) else x, list_)
# print(min_)

# def mul(num1, num2):
#     return num1 * num2
# list_ = [1, 2, 3, 4, 5, 6, -34, -100]
# res = list_[0]
# for i in list_[1:]:
#     res = mul(res, i)
# print(res)


'''enumerate(iterable, [start - число, по дефолту 0])''' # -> возвращает генератор где каждый элемент - tuple состоящий изз числа и элемента
# нумерует элементы

# list_ = ['a', 'b', 'c']
# for i in enumerate(list_):
#     print(i)

'''zip(iterable, iterable - *iterable) - соединяет последовательности'''
# list_1 = [1, 2, 3, 4, 5, 6]
# list_2 = ['a', 'b', 'c', 'd', 'e', 'f']
# print(zip(list_1, list_2))
# print(list(zip(list_1, list_2)))

# list_1 = [1, 2, 3, 4, 5, 6]
# list_2 = ['a', 'b', 'c']
# print(list(zip(list_1, list_2)))

# list_1 = [1, 2, 3, 23, 4, 5, 33]
# list_2 = [0, 0, 0, 0, 0, 0, 0]
# list_3 = ['a', 'b', 'b', 'b', 'l']
# print(list(zip(list_1, list_2, list_3)))

# dict_ = {1: 2, 2: 3, 3: 4, 4: 5}
# res = list(map(str, dict_.values()))
# # print(res)
# dict_2 = dict(zip(dict_.keys(), res))
# print(dict_2)


# list_ = [1, 1, 3, 2, 3, 5, 4]

# def str_num(number):
#     if number % 2 == 0:
#         return "четное"
#     else:
#         return "нечетное"
# res = list(map(str_num, list_))
# print(res)


# a = input()
# l = a.split
# a , b = map(int, l)
# print(a, b)
