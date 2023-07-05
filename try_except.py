'''Обработка исключений'''
# Ошибка - проблема в синтаксисе (которые исправляем самочтоятельно)
# 1. SyntaxError - забыли двоеточие, кавычку, скобку и т.д
# 2f = 8
# 2. IndentationError - неправильный отступ
# hello = 9
# 3. TaError - неверная табуляция (смешивагие пробелов и табов)

'''Исключение'''
# 1. NameError - которое выходит когда обращаемся к несуществуюему имени
# 2. IndexError - выходит когда обращаемся к несущ индексу
# 3. ZeroDivisionError - выходит при делении ноль ArithmeticError
# 4. ImportError - неправильный импорт
# 5. KeyError - выходит когда обращаемся по несущ ключу
# 6. ValueError - выходит когда пытаемся распаковать какую то последовательность где количество элементов и переменных не совпадают
# когда в функции передаем некорркетный тип данных
# 7. TypeError - когда мы пытаемся использовать метод не свойственный какому то типу данных
# или когда пытаемся передать больше аргументов чем требуется
# [].append(), 5 + "5"
# 8. AttributeError - когда обращаемся к несущ атрибуту или методу объектов
# 'hello'.splite()
# 9. BaseException (прородитель)


'''===Обработка исключений==='''
# чтобы код не прекращал работать прт некорректных данных

# try:
#     '''код который может вызвать ошибку'''
# except (Ошибка которая может возникнуть);
#     '''код который сработает если в try возникла ошибка'''

# else: 
#     '''код который отработает если try не возникла ошибка'''
# finally:
#     '''код который отработает в любом случае'''

# try:
#     a = int(input('Введите число'))
# except ValueError:
#     # print('f')
#     try:
#        a = int(input('Введите только число'))
#     except   ValueError:
#         print('все')

# try:
#     a = 2
#     b = 0
#     print(a/b)
# except ZeroDivisionError:
#     print('На ноль делить нельзя!!!!')

# try:
#     while True:
#         print(0)
# except KeyboardInterrupt:
#     print('ctrl+c')

# try:
#     num1 = 2
#     num2 = 0
#     print(num1/num2)
# except ZeroDivisionError:
#     print('gyiuhjkm')

# try:
#     dict_ = {key: key**2 for key in range(100) if key % a == 0}
# except NameError:
#     a = 2
#     dict_ = {key: key**2 for key in range(100) if key % a == 0}

# print(dict_)
# else в обработке исключений
# dict_ = {'a': 5, 'b': 10, 'c': 15, 'd': 20}
# key_ = input('Введите ключ: ')
# try:
#    res = dict_[key_]
#    print(res)
# except Exception as e:
#     print('Нет такого ключа {e}')
# else:
#     print('Blok else')

'''Оператор finally в try except'''
# try:
#     res = 10 * 2
# except Exception as e:
#     print(f'Возникла {e.__class__}')
# finally:
#     a = 5
#     res = a * 2
#     print(res)

# raise - Исскуственно вызывает ошибку
# n = int(input('Enter your age: '))
# if n <= 0:
#     raise ValueError('wow')

# res = n + 100
# print(res)

# try:
#     if 2 > 1:
#         raise Exception('f')
# except Exception:
#     print('Где логика')