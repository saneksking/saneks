import random
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
print(len(my_list))
print('-' * 57)
print('Цикл while и for')
i = 0

while i <= 5:
    i += 1
    print(i)

my_list2 = [4, 7, 8, 2]

for i in my_list2:
    print(i)
print('-' * 57)
print('Функции и модули')
def my_func(name):
    print(f'Hello {name}')
def cal(num1, num2):
    return num1 + num2
my_func('Saneks')
print(cal(5, 7))
print('-' * 57)
print('Исключения и файлы')
try:
    n = 7
    n2 = 0
    print(n / n2)
except ZeroDivisionError:
    print('На ноль делить нельзя')
finally:
    print('Это выводится всегда')
try:
    raise NameError('Invalid name')
except:
    print('Вызвал исключение')
assert 5 > 4
print(4)
file = open('test.txt', 'w')
file.write('This is text')
file.close()
file = open('test.txt', 'r')
cont = file.readlines()
print(cont)
file.close()
print('-' * 57)
print('Другие типы объектов')
def some_func():
    print('Hi')

print(some_func())
print('Словари')
name = {'king': 'Saneks', 'Dad': 'Baty'}
print(name['king'])
print(name['Dad'])
name[5] = 'kin'
name['Dad'] = 'baty'
print(name)
print(1 in name)
print(6 not in name)
print('Кортежи')
cort = ('Hello', 'world', '!')
print(cort[0])
print(cort[1])
print(cort[2])
print('Срезы')
lis = [1, 2, 3, 4, 5, 6]
print(lis[0:3])
print(lis[0::2])
print('Списковое включение')
l = [i ** 2 for i in range(10) if i**2 % 2 == 0]
print(l)
print('-' * 57)
print('Функциональнон прогоапмирование')
def add_twice(func, arg):
    return func(func(arg))
def add_five(x):
    return x + 5

print(add_twice(add_five, 10))
print('Чистая и нечистая функции')
def new(x, y):
    temp = x + 2 * y
    return temp / (2 * x + y)
print(new(5, 7))

some_list = []
def impure(arg):
    some_list.append(arg)

print(impure(6))
print(some_list)
print('Лямбда')
def new2(f, arg):
    return f(arg)
print((lambda x: x**2 + 5*x + 4) (-4))
new3 = (lambda y: y ** 2 + 6*y + 8)
print(new3(5))
print('Функции map и filter')
def add_five(x):
  return x + 5

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)

nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))
print(res)

print('Генераторы')
def countdown():
    i=5
    while i > 0:
        yield i
        i -= 1

for i in countdown():
    print(i)

#def infinite_sevens():
#  while True:
#    yield 7
#
#for i in infinite_sevens():
 # print(i)


def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(numbers(11)))
print('Декораторы')
def decor(func):
    def wrap():
        print('***********')
        func()
        print('***********')
    return wrap
@decor
def hello():
    print('hello')


hello()
print('Рекурсия')
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(5))
print('Множества')
num_set = {1, 2, 3, 4, 5}
word_set = set(["spam", "eggs", "sausage"])

print(3 in num_set)
print("spam" not in word_set)
num_set.add(7)
num_set.remove(2)
print(num_set)
print('Классы')
class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def sign(self):
        print('Meow')
    def gav(self):
        print('Gav')

class Cat(Animal):
    def sign(self):
        print('meow')
        super().gav()
print('Снизу вывод класса')
cat = Cat('Simba', 'black')
print(cat.name)
print(cat.color)
cat.sign()

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)
print(result.y)

class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])

spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam / hello)

class VagueList:
    def __init__(self, cont):
        self.cont = cont

    def __getitem__(self, index):
        return self.cont[index + random.randint(-1, 1)]

    def __len__(self):
        return random.randint(0, len(self.cont)*2)

vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)

square = Rectangle.new_square(5)
print(square.calculate_area())

class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True

ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)


class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        self._pineapple_allowed = False

    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed

    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        if value:
            password = input("Enter the password 123: ")
            if password == "123":
                self._pineapple_allowed = value
            else:
                raise ValueError("Alert! Intruder!")

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)
print('-' * 57)
print('Регулярные выражения')
import re
patern = r'saneks'
if re.match(patern, 'sanekssanekssaneks'):
    print('match')
else:
    print('no match')
if re.search(patern, 'ekssaneksekssaneks'):
        print('Match')
else:
    print('No match')
print(re.findall(patern, 'ekssanekssan'))

math = re.search(patern, 'saneksekssanesaneks')
print(math.group())
print(math.start())
print(math.end())
print(math.span())
str = "My name is David. Hi David."
pattern = r"David"
newstr = re.sub(pattern, "Saneks", str)
print(newstr)
print('Метасимволы')
pattern = r"^gr.y$"

if re.match(pattern, "grey"):
    print("Match 1")

if re.match(pattern, "gray"):
    print("Match 2")

if re.match(pattern, "stingray"):
    print("Match 3")

patteern = r"[A-Z][A-Z][0-9]"

if re.search(patteern, "LS8"):
    print("Match 1")

if re.search(patteern, "E3"):
    print("Match 2")

if re.search(patteern, "1ab"):
    print("Match 3")

patttern = r"egg(spam)*"

if re.match(patttern, "egg"):
    print("Match 1")

if re.match(patttern, "eggspamspamegg"):
    print("Match 2")

if re.match(patttern, "spam"):
    print("Match 3")

print('-' * 57)
print('Другие пакеты python')
def function(named_arg, *args):
    print(named_arg)
    print(args)

function(1, 2, 3, 4, 5)
