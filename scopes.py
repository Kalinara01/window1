'''Области видимости и пространсва имен'''
# 4
# 1. builtins (встроенное)
# print()
# len()
# abs()
# input()

# 2. Global(глобальные) - все именя внутри файла
# a = 89
# b = 5

# 3. Enclose - пространство находящееся между двумя пространствами (не всегда есть)

# 4. Local (локальное) - внутри функции

# print(dir(__builtins__)) - возвращает список встроенных классов, объектов и функции

# a = 34
# b = 0
# print(globals())
# print(globals()['b'])
# print(b is globals()['b'])
# globals()['y'] = 'hello world'
# # print(globals())
# print(y)

# def hello():
#     a = 'hello'
#     print(a)

# hello()

# def func(a, b):
#     x = 7
#     print(locals())
# func(3, 4)

'''Enclose''' # - вложение в функциях

# x = 'Это глобальная переменная'

# def some_func():
#     x = 'Это enclose переменная'
#     def some_func2():
#         x = 'Это локальная переменная'
#         print(x)
#     some_func2()
# print(x)
# print(x)
# some_func()

'''Порядок поиска переменных'''
# lokal - enclose - dlobal - builtins
# a = 8
# def func():
#     b = 'local'
#     return a + 100

# print(func())

# global - позволяет менять значение глобальной переменной, находясь в локальной области видимости

# a = 8 
# def func():
#     global a
#     a += 100
#     # return 'changed'
# print(func())
# print(a)


# count = 0
# def counter():
#     global count
#     print(count)
#     count += 1


# counter()
# counter()


# a = 9
# def outer_func():
#     a = 10

#     def inner_func():
#         global a
#         a = 8
#         print('inner', a)
#     inner_func()
#     print('outer', a)

# outer_func()
# print(a)


'''nonlocal'''
# def f1():
#     a = '1'

#     def f2():
#         def inner2():
#             nonlocal a - предоставляет доступ на изменение enclose переменной в локальной области видимости
#             a = 2
#             print(a)
#         inner2()
#     f2()
#     print(a)

# f1()

# def counter(i):
#     count = 0

#     def add():
#         nonlocal count
#         print(count)
#         count += 1
#     for i in range(i+1):
#         add()

# counter(10)



