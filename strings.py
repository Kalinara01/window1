'''''''''=====Строки===='''''''''''
# строки это неизменяемый тип данных, который представляет последовательность символов, заключенных в кавычки

# id() это возвращвет номер ячейки памяти

# a = '5'
# b = 5
# print(id(a))


# string = 'строка с одинарным кавычками'
# string = "строка с двойными кавычками"
# # string3 = 'error'
# strind4 = "Don't"
# # string5 = '" Makers"'
# # print 


'''====Экранизация строк==='''
# '/символ'
'/n' # это перенос на следующую строку

# a = 'hello /nword'
# print(a)

'/t' # это тамбулиция
# a = 'hello/t world
# print(a) #hello world

'//' #  это для отобрежение '/'
# a = 'hello //'
# print(a)

'\'' # для отображения '
"\"" # для отобрежения "
'\r' # возврвщение каретки в начало строки

# print('Makers \rlab') #labers

'\v' # перенос на новую строку со смещением вправо на длину предыдущей

# print('hello\vworld')

'\a' # это гудок встроенного ы систему динамика
# print('hello\a')


# Конкатенция строк это склеивание строк
# a = 'hello'
# b = 'world'
# print(a + '' +b)
  
# 'Дублирование строк'
# print(a * 5)

'''===Форматирование строк (Динамическиу строки)==='''


# 1. %
# 2. .format()
# 3. f-строки

# 1
# name = input('Введите имя;')
# print('Hello, %s' %name)

# # 2 
# name = input('name; ')
# name2 = input('name2;' )
# print('Hello, {}, {}'.format(name, name2))

# 3 интерполяция строк
# name = input('name; ')
# name2 = input('name2 ')
# print(f'Hello {name}')



'''===Методы строк==='''

# Методы на is 
# s.isdigit() проверяет состоит ли строки только из чисел (True/False)
# s.isalnum() только из букв и чисел
# s.islpha() только из букв
# s.islower() все символы в нижнем регистре
# s.isupper() это символы в верхнем регистре
# s.isspace() состоит ли строка из неотображаемых символов (пробел, '\n' ...)

# . lower() переводит целую строку в нижний регистр
# print('Avyadsgfdsugfvcbsu'. lower()

# .upper() переводит строку ы верхней регистр
# print('Ahjhgyuuhjbii'.upper())

# .swapcase() переводит символы в противоположный регистр
# print('Agioijhbmm'.swapcase())


# .title() переводит первую букву каждого слова в верхний регистр
# print('hello world' .title)

# .capitalize() переводит первый символ строки в верхний регистр
# print('hello world' .capitalize())

# .strip() убирает пробельные символы в начале и в конце

# .lstrip() убирает пробельные символы в начале
# .rstrip() в конце

# .replace(old, new, [count]) меняет old значение на new определенное кол-во count
# print('ha ha ha ha'.replace('ha', 'new', 2))

# .split(разделитель) делит строку по разделителю, возвращает список (массив)

# разделитель.join(iterable) соединяет строку по разделителю

# .startswich(string) проверяет начинается ли наша строк c string
# .endswich(string) проверяет заканчивается ли строка на string

# .count(string) считает количество вхождении string в строке
# a = 'llhlelloll'
# print(a.count('ll'))

'''====Индекс==='''
# индекс порядковый номер элемента
'hello'
#0123

# a = 'hello world'
# print(a[-1]) это последний элемент

'''срезы'''
# print(a[0:2])

# срезы по индуксу это нахождение полстроки, начинная от start и заканчивая до stop (stop не включительно), шаг-через какой элемент записывать

# a = 'hello world'
# print(a[::-1]) это переворачивает строку

