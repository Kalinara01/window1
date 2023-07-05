'''===Цикл==='''
# while - это цикл который работает пока уcловие верно True

'''опасность в создании бесконечного цикла'''


# counter = 10 
# while counter != 0:
#     print(counter)
#     counter = counter - 1

# a = 8655558998765
# summa = 0
# for i in str(a):
#     summa = summa + int(i)
# print(summa)

# a = '1nj3454mn678lm985seff3'
# summa = 0
# for i in a:
#     if i.isdigit():
#         summa = summa + int(i)
#     print(summa)


# при итерации словаря получаем только ключи
# dict_ = {'a': 1, 'b': 2}
# for i in dict_:
#     print(i)

# dict_.values() это прохождение по значениям


'''===Ключевые слова в циклах==='''
# break - полностью выйти из цикла. Досрочно прерывает цикл
# continue - перейти к след итерации
# Оператор continue начинает след проход цикла, миную оставшееся тело цикла

# for in in 'hello'
#  тело

# for i in range(11):
#     if i == 4:
#         continue
#     print(i)

# for i in range(11):
#     print(i)
#     if i == 4:
#         continue это впустую работает


'''Оператор pass'''
# ничего не делает. Фактически заглушка для обьекта pass

# for i in range(11):
#     if i == 4:
#         pass
#     print(i)


# слово else применяется в циклах for и while - приверяет был ли произведен выход из цикла без оператора break('естественным образом') код внутри else отработает если не сработал break

# mark = int(input('Введите число' :))
# if mark >= 90:
#     print('Отлично, Ваша оценка 5!')
# elif mark >= 80 and mark < 90:
#         print('Здорово, Ваша оценка 4!')
# elif mark >= 70 and mark < 80:
#             print('Хорошо, Ваша оценка 3!')
# elif mark >= 60 and mark < 70:
#                 print('Вам стоит подучить материал')
# else:
#                     print('Вы не сдали экзамен')