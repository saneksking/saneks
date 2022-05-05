while True:

    num1 = float(input('Введите ваше число: '))
    num2 = float(input('Введите ваше число: '))
    variant = input('+ - / * %: ')
    if variant == '+':
        print(num1 + num2)
    elif variant == '':
        print('Вы не ввели вариант! ')
    elif variant == '-':
        print(num1 - num2)
    elif variant == '/':
        print(num1 / num2)
    elif variant == '*':
        print(num1 * num2)
    elif variant == '%':
        print(num1 % num2)
    var = input('Вы хотите выйти? y/n: ')
    if var == 'y':
        break
    elif var == 'n':
        continue
        
