
def main():
    class Staff:
        def __init__ (self, pPosition, pName, pPay):
            self._position = pPosition
            self.name = pName
            self.pay = pPay 
            print('Creating Staff object')
        def __str__(self):
            return "Position = %s, Name = %s, Pay = %d"%(self._position, self.name, self.pay)
        def calculatePay(self):
            prompt = '\nEnter number of hours worked for  %s: '%(self.name)
            hours = input(prompt)
            prompt = 'Enter the hourly rate for %s: '%(self.name)
            hourlyRate = input(prompt)
            self.pay = int(hours)*int(hourlyRate)
            return self.pay

        @property
        def position(self):
            print('Geting method')
            return seld._position
        @position.setter
        def position(self, value):
            if value == 'Manager' or value == 'Basic':
                self._position = value
            else:
                print('Not position!')


    staff = Staff('Basic', 'Saneks', 0)
    print(staff)

    class A:
        def __init__(self):
            self.__x = 5
            self._y = 10

    varA = A()
    print(varA._y)
    '''print(varA.__x) Произойдет ошибка так как произойдет корректировка имен'''
    print(varA._A__x)
    class MethodDemo:
        a = 1

        @classmethod
        def classM(cls):
            print(f'Class method {cls.a}')

        @staticmethod
        def staticM():
            print('Static method')

    MethodDemo.classM()
    md1 = MethodDemo()
    md1.classM()
    md1.staticM()

class SomeClass:
    def __init__(self):
        print('This is some class')
    def somemethod(self, a):
        print(f'The value of a is {a} ')
        self.b = 5
class SomeOtherClass:
    def __init__(self):
        print('This is some other class')

class ProgStaff:                                      company = 'programmlab'
    def __init__ (self, psalary):
        self.salary = psalary
    def printinfo(self):
        print(f'Company name is {ProgStaff.company}')
        print(f'Salary is {self.salary}')

peter = ProgStaff(2500)
john = ProgStaff(2500)
ProgStaff.company = 'programmscholl'
print(peter.company)
print(john.company)
peter.salary = 2700
print(peter.salary)
print(john.salary)
john.printinfo()
ProgStaff.printinfo(john)
if __name__ == '__main__':
    main()
