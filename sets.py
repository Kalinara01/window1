'''Множества set()'''
# изменяемый неупорядоченный, итерируемый, неиндексируемый тип данных
# Предназначен для хранения уникальных значений. Могут зранить в себе только неизменяемый типы данных, если используете tuple то в них тоже должны храниться неизменяемый типы данных

# set1 = {1, 2, 3, 3}
# # print(set1)
# set2 = {(1, 2, 3), 1, 2, 3}
# print(set2)

# set3 = {1, True, 0, False}
# print(set3)

'''Создание множеств'''
# 1. set()
# a = set([1. 2, 3,4])
# print(a)

# 2. {}
# set_ = {1, 2, 3, 'hello', (4,5), None, True, False}
# print(set_)

'''=== Методы set==='''
'''добавление элементов'''
# add(element)
# update(sequence)

# set_ = {1, 2, 3}
# set_.add('hello')
# print(set_)

# update (за раз может добавить несколько элементов но не повторяет имеющиеся) передаем все итерируемые
# set_update = {1, 2, 3}
# set_update = ('hello')
# print(set_)

'''Удаление элементов'''
# remove(element) - удаляет элемент если такого элемента нет выдает ошибку
# discard(element) -  еслт элемент нет ничего не произойдет
# pop()- удаляет случайный

# set_ = {1, 2, 3, 4, 5}
# set_.remove(1)
# set_.discard(3)
# set_.pop()
# print(set_)
# pop удаляет самый  первый цифру а popped обратно возвращает


# set_a.difference(set_b) -  выводит элементы которые есть в set.a но нет в sert_b
# set_a = {1, 2, 3}
# set_b = {3, 4, 5, 6}
# print(set_a.difference(set_b)


# set_a.symmetric_difference(set_b) - выводит уникальные элементы в обоиж множествах
# set_a ^ set_b
# set_a.intersection(set_b) - выводит похожие элементы для set_a и set_b
# set_a.union(set.b) -  соединяет set_a и set_b
# set_a | set_b
# set_a = {1, 2, 3}
# set_b = {4, 5, 6}
# print(set_a | set_b)

# Д/З
# copy
# difference_update()
# intersection_update()
# symmetric_difference_update()
# isdisjoint()
# issubset()
# issuperset()

# address = "1.1.1.1"
# print(address.replace('.', '[.]'))

# command = "G()()()()(al)"
# print(command.replace('(al)', 'al').replace('()',('0'))