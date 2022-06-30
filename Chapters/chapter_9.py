
class Staff:
    def __init__(self, pPosition, pName, pPay):
        self._position = pPosition
        self.name = pName
        self.pay = pPay
        print('Creating Staff object')

    def __str__(self):
        return f"Position = {self._position}, Name = {self.name}, Pay = {self.pay} "

    def __add__(self, other):
        return self.pay + other.pay

    def calculatePay(self):
        prompt = '\nEnter number of hours worked for  %s:  ' % self.name
        hours = input(prompt)
        prompt = 'Enter the hourly rate for %s:  ' % self.name
        hourlyRate = input(prompt)
        self.pay = int(hours) * int(hourlyRate)
        return self.pay

    @property
    def position(self):
        print('Getting method')
        return self._position

    @position.setter
    def position(self, value):
        if value == 'Manager' or value == 'Basic':
            self._position = value
        else:
            print('Not position!')


class A:
    def __init__(self):
        self.__x = 5
        self._y = 10

    @property
    def y(self):
        return self._y


class MethodDemo:
    a = 1

    @classmethod
    def classM(cls):
        print(f'Class method {cls.a}')

    @staticmethod
    def staticM():
        print('Static method')


class SomeClass:
    def __init__(self):
        self.b = 5
        print('This is some class')

    @staticmethod
    def someMethod(a):
        print(f'The value of a is {a} ')


class SomeOtherClass:
    def __init__(self):
        print('This is some other class')


class ProgStaff:
    company = 'ProgramLab'

    def __init__(self, pSalary):
        self.salary = pSalary

    def printInfo(self):
        print(f'Company name is {ProgStaff.company}')
        print(f'Salary is {self.salary}')


def main():
    varA = A()
    print(varA.y)
    '''print(varA.__x) Произойдет ошибка так как произойдет корректировка имен'''
    '''print(varA._A__x) Выведится значение переменной __x'''
    MethodDemo.classM()
    md1 = MethodDemo()
    md1.classM()
    md1.staticM()
    staff = Staff('Basic', 'Saneks', 0)
    print(staff)


peter = ProgStaff(2500)
john = ProgStaff(2500)
ProgStaff.company = 'programSchool'
print(peter.company)
print(john.company)
peter.salary = 2700
print(peter.salary)
print(john.salary)
john.printInfo()
ProgStaff.printInfo(john)
if __name__ == '__main__':
    main()
