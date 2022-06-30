from chapter_9 import Staff


class ManagerStaff(Staff):
    def __init__(self, pName, pPay, pAllowance, pBonus):
        super().__init__('Manager', pName, pPay)
        self.allowence = pAllowance
        self.bonus = pBonus

    def calculatePay(self):
        basicPay = super().calculatePay()
        self.pay = basicPay + self.allowence
        return self.pay

    def calculatePayBonus(self):
        prompt = f'Enter performance grade for {self.name}: '
        grade = input(prompt)
        if grade == 'A':
            self.bonus = 1000
            print('You reach 1000')
        else:
            self.bonus = 0
        return self.bonus


class BasicStaff(Staff):
    def __init__(self, pName, pPay, pSalary):
        super().__init__(pSalary, pName, pPay)


def main():
    print('-' * 80)
    manager = ManagerStaff(pName='Saneks', pPay=30000, pAllowance='all', pBonus='1000')
    print(manager.name)
    print(manager.pay)
    print(manager.allowence)
    print(manager.bonus)
    manager.calculatePayBonus()


if __name__ == '__main__':
    main()
