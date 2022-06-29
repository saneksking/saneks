from chapter_9 import ProgStaff

def main():
    class ManagentStaff(ProgStaff):
        def __init__(self, pName, pPay, pAllowance, pBonus):
            super().__init__('Manager', pName, pPay)
            self.allowence = pAllowence
            self.bonus = pBonus
        def calculatepay(self):
            basicpay = super().claculatepay()
            self.pay = basicpay + self.allowence
            return self.pay
        def claculatepaybonus(self):
            prompt = f'Enter perfomance grade for {self.name}'
            grade = input(prompt)
            if grade == 'A':
                self.bonus = 1000
            else:
                self.bonus = 0 
            return self.bonus

    class BasicStaff(ProgStaff):
        def __init__(self, pName, pPay):
            super().__init__('Basic', pName, pPay)



if __name__ == '__main__':
    main()
