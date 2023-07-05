'''Тип данных dict()'''
# {key: value}
# позволяет хранить обькты для доступа к которым используется ключ (key)

# именяемый итерируемые неидексируемые упорядочный тип данных

# {} литералы
# dick_ = {}
# print(type(dick_))

# dick_ = {'a': 'hello', 'b': 'world', 'c': 3 }
# print(dict_['c'])
#  ключи должны быть неизменяемый типом данных
#  ключ должен быть уникальный
#  значение словаря могут быть любые типы данных

# dick_ = {1: {'a': 'one'}, 'helli': [1,2,3]} # правильное

'''===Создание словарей==='''
# 1. {kye: value}
# 2. dick()
# print(dick) это неправильно
# print(dick([('key1', 'value'),('key2', 'value')]))

'''Методы словарей'''

# dict_ = {'name': 'John', 'age': 25, 'hobby': ['footbal', 'poker', 'sing']}
# dict_.clear()
# print(dick_)

# .copy() возвращает коптю словаря


# .fromkeys(seq, [value]) создает словарь с ключами из seq и значения value (для всех одинаковый по умолчанию none)

# list_ = ['name', 'age', 'hobby']
# dict_ = dict.fromkeys(list_, 'wow')
# print(dict_)

# получение элемента из словаря
# .get(key, [value]) -> возвращает значение по ключу key а если такого ключа нет не бросает ошибку а возвр  Value или None
# ['key']

# изменение элементов словаря

# .update(new_dick) это добавляет new_dick в наш словарь
# dict_ = ['name': 'Jonh', 'age': 25, 'hobby': ['footbal', 'poker', 'sing']]
# new_dick = {'address': 23}
# dict_.update({'address': 23})
# print(dict_)
# .setdefault(key, [defaul_value]) работает точно так же как метод get(), но  если нет такого ключа он создаст новую пару key: defaul_value

# dict_ = ['name': 'Jonh', 'age': 25, 'hobby': ['footbal', 'poker', 'sing']]
# print(dict_.setdefault('address'))
# print(dict_)

# .keys()выводит все ключи в словаре
# ,values() выводит значения в словаре
# .items() возвращает все пары из словаря 
# print(dict_.items())

# удаление элементов в словаре
# pop(key, [message]) удаляет пару ключ и значение, и возвращает значение если ключа нет то возвращает message (по умолчению бросает исключение (ошибку))

# .popitem() удаляет и возвращает пару ключ и значение. удаляет последнюю довабленную пару