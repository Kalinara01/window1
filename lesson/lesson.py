# def add_one(x: int) -> int:
#     return x + 1


# def division(x: int, y: int) -> float:
#     if  y == 0:
#          raise ZeroDivisionError
#     return x/y


# def add(x: int, y: int) -> int:
#     return x + y

# def is_palindrom(string: str) -> bool:
#     if string == string[::-1]:
#         return True
#     return False


db = [
    {'name': 'hello', 'password': hash ('12345678')},
    {'name': 'World', 'password': hash ('helloworld')}
]
# print(db)
def in_database(name):
    for user in db:
        if user['name'] == name:
            return True
    return False

# print(in_database('hello'))

def register(name, password1, password2):
    if in_database(name):
        raise Exception('Юзер с таким именем существует')
    if password1 != password2:
         raise  Exception('Пароли не совпадают')
    if len(password1) < 7:
         raise  Exception('Cлишком короткий пароль')
    user = {'name': name, 'password': hash (password1)}
    db.append(user)
    return 'Вы успешно зарегистрировались'

# print(register('Hello', '45678521', '45678521'))

def login(name, password):
    if not in_database(name):
        raise Exception('Пользователь не найден')
    for user in db:
        if user['name'] == name:
            if user['password'] != hash (password):
                raise Exception('Пароль не верный')
    return 'Вы успешно залогинились'

# print(login(name=input('Введите имя:'), password=input('Введите пароль: ')))

# def main():
#     print('Welcom')
#     while True:
#         action = input('Register: 1, Login: 2, Quite: 3')
#         if action == '3':
#             break
#         elif action == '1':
#             name = input('Введите имя ')
#             p1 = input('Введите пароль ')
#             p2 = input('Введите подтверждение пароля ')
#             print(register(name, p1, p2))
#         elif action == '2':
#             name = input('Введите имя ')
#             p1 = input('Введите пароль ')
#             print(login(name, p1))
#         else:
#             print('Не корректный ввод')

# main()
