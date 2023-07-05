'''Декораторы'''

# def f():
#     print('hello')


# a = f
# a()

'''функция высшего порядка - принимает как аргумент и/или возвращает функцию'''

'''Декораторы - функция высщего порядка, позволяет обернуть другую функции для расширения функционална (не изменяя код)'''

# def a():
#     print('I am a function')

# def b(func):
#     print(f'hello, {func.__name__}')
#     func()

# b(a)

# def benchmark(func):
#     import time
#     start = time.time()
#     func()
#     finish = time.time()
#     print(f'Время функции {func.__name__}, заняло: {finish - start}')


# def loop():
#     i = 0
#     range_number = 1000
#     while i < range_number:
#         print(i)
#         i += 1
#         import time

# benchmark(loop)


'''Синтаксис дикораторов'''
# def decorator_func(func):
#     def wrapper():
#         print('Функция обертки')
#         print('выполняем обертываемую функцию')
#         func()
#         print('выход из обертки')
#     return wrapper

# # @ - синтаксический сахар
# @decorator_func
# def say_hi():
#     print('hi')
# say_hi()

# def uppercase_decorator(func):
#     def wrapper():
#         return func() .upper()
#     return wrapper

# @uppercase_decorator
# def say_hi():
#     return 'hi'

# print(say_hi())

# def benchmark(func):
#     def wrapper():
#         import time
#         start = time.time()
#         func()
#         finish = time.time()
#         print(f'Время функции {func.__name__}, заняло: {finish - start}')
#     return wrapper


# @benchmark
# def loop():
#     i = 0
#     range_number = 1000
#     while i < range_number:
#         print(i)
#         i += 1
        

# @benchmark
# def add():
#     ls = []
#     for i in range(1000):
#         ls.append(i)

# loop()
# add()


'''Декораторы с аргументами'''
'''Универсальная запись'''

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         print('hello')

#     return wrapper

# @decorator
# def func1(a):
#     print('py27')

# func1(1)

# def smart(func):
#     def wrapper(q, w):
#         print('функция оберетка')
#         if w == 0:
#             print('На ноль делить нельзя')
#             return None
#         return func (q, w)
#     return wrapper

# @smart
# def division(a,b):
#     return a/b

# print(division(9, 0))


# def benchmark(num):
#     def inner_func(func):
#         def wrapper():
#             for i in range(num):
#                 func()
#         return wrapper
#     return inner_func

# @benchmark(5)
# def func():
#     print(1)

# func()

# def strong(func):
#     def wrapper(*args, **kwargs):
#         return '<strong>' + func() + "</strong>"

#     return wrapper

# def div(func):
#     def wrapper(*args, **kwargs):
#         return '<div>' + func() + "</div>"
#     return wrapper
# @div
# @strong

# @strong
# def get():
#     return 'Johm Snow'

# print(get())