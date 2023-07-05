#   GNU nano 6.2                                                                                  git_commands.py *                                                                                          
# git init - превращает текущую директорию в git зепозиторий (создается .git)
# git add . (. - все файлы можно указывть отдельные файлы) - отслеживание всех файлов)
# git commit -m "comnit" - добавляет/соверщает собранение в git всех файлов которые  находятся в индексе
# git log - выводит журнал (log) сохранений
# git status - показывает статус файлов
# git remote add origin (название связи - обычно origin) SSH (ссылка на удаленный репозиторий)
# git checkout hash_commit - просматриваем версию
# dit branch - выводит в терминал список всех веток (звездочкой помечена активная ветка)
# dit checkout <название_ветки>
#                                 - переход на указанную ветку
# git switch <название ветки>
# git push origin(название_связи) master(название_ветки) - отправка версии кода на удаленный репозиторий



# git clone <ссылка_на_удаленный_репозиторий> - склонировать/скопировать/скачать репозиторий




'''ООП - объектно ориентированного програмирование'''

# class SomeClass:
#     pass

# class A:
#     pass

# a = A() # экземпляр класса, объект класса. Экземпляр класса instance, объект класса object
# print(isinstance(a, A))


# class int:
#     # свойства
#     pass

# class list:
#     # свойства
#     pass


# a = 4
# print(type(a))

# class Dog:
  
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return f'{self.name} {self.age}'
    
#     def bark(self):
#         print('Cav-gav')

#     def dog_info(self):
#         return f'this is {self.name}, he is {self.age} years old'
    
#     def birthday(self):
#         self.age += 1
#     # @classmethod
#     # def eat(cls):
#     #     print('Nyam-nyam')

# dog1 = Dog(name='Rex', age=3)
# dog2 = Dog(name='Bobic', age=2)
# dog3 = Dog(name='Oreo', age=1)
# # dog1.bark()
# # print(dog3.dog_info())
# dog1.birthday()
# print(dog1.age)


# class Rectangle:

#     default_color = 'Red'

#     def __init__(self, width, length):
#         self.width = width
#         self.length = length

#     def area(self):
#         return self.width * self.length
    
# rec1 = Rectangle(4, 6)
# rec2 = Rectangle(2,7)
# # print(rec1.area())
# # print(rec1.width)
# rec2.default_color = 'yellow'
# print(rec2.default_color)
# print(rec1.default_color)

# class Car:

#     car_count = 0

#     def __init__(self):
#         Car.car_count += 1

# car1 = Car()
# print(Car.car_count)
# car2 = Car()
# car3 = Car()
# car4 = Car()
# print(Car.car_count)
        


'''ООП Наследование'''

# class Polygon:

#     sides = 'many'

#     def __init__(self, *args, **kwargs):
#         self.args = args
#         self.kwargs = kwargs
#         # print(self.args)
#         # print(self.kwargs)

#     def get_perimiter(self):
#         if self.args:
#             return sum(self.args)
#         elif self.kwargs:
#             return sum(self.kwargs.values())
        
# class Rectangle(Polygon):

#     sides = 4

#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def get_perimiter(self):
#         return (self.a + self.b) * 2
        

# rectangle = Rectangle(a=7, b=6)
# rectangle2 = Rectangle(a=9, b=2)
# print(rectangle.sides)
# print(rectangle.get_perimiter())
# print(rectangle2.get_perimiter())

# polygon = Polygon(a=9, b=8, c=10, d=9, e=5)  

# print(polygon.get_perimiter())
# print(polygon.sides)


'''Икапсуляция'''
# Модификатор доступа:
# 1. public - приватный, get_info()
# 2. protected - защищенный _get_info()
# 3. private - приватный __get_info














