print('-' * 50)
print('Программа для подсчитывания очков у игроков')
print('-' * 50)
users = {}
while True:
    user = input('Введите имя игрока или 0 для завершенния ввода: ')
    print('-' * 50)
    users[user] = 0
    if user == '0':
        del users['0']
        print(users)
        break

while True:
    try:
        print('-' * 50)
        choice = input(f'Выберите игрока которому хотите добавить очки или 0 для выхода из программы {users}: ')
        if choice == '0':
            print('Программа выключается...')
            break
        if choice not in users:
            print('Такого игрока нет')
            continue
        num = int(input(f'Сколько хотите добавить {choice}: '))
        users[choice] = num
        print(users)
    except TypeError:
        print('Неверный ввод')
        continue
