'''Comprehension'''
# генерация последовательности в одну строку используя цикл(синтвксический сахар)
# list,set, dict
'''Синтаксис'''
# result for element in iterable_object
# result for element in iterable_jbject if filler
'''list comprehension'''
# упрощенный подход к созданию списка,задействует цикл for и if-else

# list_ = []
# for i in range(11):
#     list_.append(i)
#     print(list_)

# list_ = [i for i in range(11)]
# print(list_)

# import time 
# start_time = time.time()

# list_ = []
# for i in range(100):
#     list_.append(1)

# time1 = time.time() - start_time

# start_time = time.time()
# list_2 = [i for i in range(1000)]
# time2 = time.time() - start_time
# print(time1,time2)


# list_ = []
# for i in range(11):
#     if i % 2 == 0:
#         list_.append(1)
# print(list_)
 
# list_2 = [i for i in range(11) if i % 2 == 0]
# print(list_2)

# list1 = [1, 'hello', 3, 'a', 4.0, 6, 8, 'hw']
# list2 = [f'{i} нечетное' if i % 2 else f'{i} четное' for i in list1 if  type(i) ]

'''Set comprehension'''
# почти тоже самое, что представление списков используется {} скобки не содержит дубликатов не гарантирует сохранность элементов в порядке

# list_ = [1, 2, 3, 1, 3, 5, 4]
# set_ = {i for i in list_}
# print(set_)

# set_ = set()
# for i in list_:
#     set_.add(i)
# print(set_)


'''Dict comprehension'''
# необходимо допольнительно определть клю

# dict_ = {1: i**2 for i in range(10)}
# print(dict_)

# dct_ = {}
# for i in range(10):
#     dct_.update({i: i ** 2})

# print(dct_)

# d = {'a': 2, 'b': 3}
# a = {k: 'четное' if v % 2 == 0 else 'нечетное' for k, v in d.items()}
# print(a)

# d = {i: str(i) for i in range(1,11) }
# print(d)

# a = [1,2,3,4,5]
# b = ['a', 'b', 'c', 'd', 'e']
# d = {a[i]: b[i] for i in range(len(b))}

# print(d)

'''Вложенные comprehension'''

# dict_ = {i: list(range(1,i+1)) for i in range(1,6)}
# print(dict_)

employees = {
    'id1': {
        'first name': 'Александр',
        'last name' : 'Иванов',
        'age': 30,
        'job':'программист'
            },
    'id2': {
        'first name': 'Ольга',
        'last name' : 'Петрова',
        'age': 35,
        'job':'ML-engineer'
    }}

# for info in employees.values():
#     for k, v in info.items():
#         if k == 'age':
#             info[k] = float(v)
# print(employees)


# print({id_:{k: (float(v) if k == 'age' else v) for k, v in info.items()} for id_, info in employees.items()})+-