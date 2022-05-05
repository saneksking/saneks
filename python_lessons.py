print('Операции с числами!'.center(5, '='))
print(7 + 8)  # Операция сложения
print('*' * 57)
print(6 * 3) # Операция умножения
print('*' * 57)
print(6 / 3) # Операция деления
print('*' * 57)
print(4.0 + 5) # Операция сложения числа с точкой
print('*' * 57)
print(2 ** 5) # Возведение в степень
print('*' * 57)
print(3 ** (1 / 2)) # Возведение в степень с точкой
print('*' * 57)
print(20 // 3) # Частное от деления
print('*' * 57)
print(25 % 7) # Остаток от деления
print('-' * 57)
print('Операции со строками')
print('This is string')
print('I\'m developer')
print('*' * 57)
print('One\nTwo\nThree')
print('''Four
Five
Six''')
print('*' * 57)
print('Python' + ' is' + ' awesome!')
print('*' * 57)
print('Great ' * 5)
print('-' * 57)
print('Операции с переменными')
name = 'Saneks'
x = 5
print('*' * 57)
print(x)
print('*' * 57)
print(x + 7)
x = 'string'
print('*' * 57)
print(x)
num = 5
num += 6
print('*' * 57)
print(num)
string = 'spam'
string += 'egg'
print('*' * 57)
print(string)
num1 = 5
print(num1)
print('*' * 57)
print(num2:=int(input('Введите число: ')))
print('*' * 57)
print(num2)
print('-' * 57)
print('Операции с вводом и выводом')
lastname = input('Введите свою фамилию: ')
age = int(input('Введите ваш возраст: '))
print(f'Ваша фамилия ' + lastname + ' и ваш возраст ' + str(age))
print('-' * 57)
print('Болево значения')
print(4 == 4)
print('*' * 57)
print(1 == 2)
print('*' * 57)
print(5 != 4)
print('*' * 57)
print(5 >= 4)
print('*' * 57)
print(4 <= 3)
print('*' * 57)
print( 'Annie' < 'Anny')
print('-' * 57)
print('Инструкция if,else,elif')
if 1 == True:
    print('Это инструкция if')

if 1 == 0:
    pass
else:
    print('Это инструкция else')

if 4 != 4:
    pass
elif 4 == 4:
    print('Это инструкция elif')

print('-' * 57)
print('and,or,not')
print(2 > 1 and 3 < 4 )
print(2 == 3 or 4 > 3)
print('-' * 57)
print('Списки')
words = ['Hello', 'world', '!']
print(words[0])
print(words[1])
print(words[2])
empty_list = []
print(f'Это пустой список {empty_list}!')
my_list = ['Saneks', 13, ['mam', 33]]
print(f'Это значение во  вложенном списке {my_list[2] [1]}')

my_list[1] = 19
print(my_list[1])
print('Saneks' in my_list and 19 in my_list)
print('method append')
my_list.append(6)
print(my_list)
print(len(my_list))
my_list.insert(1, 13)
print(my_list)
print(len(my_list))
print('-' * 57)
print('Цикл while и for')
i = 0

while i <= 5:
    i += 1
    print(i)

my_list2 = [4, 7, 8, 2]

for i in my_list2:
    print(my_list2)
