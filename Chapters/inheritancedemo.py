from chapter_10 import BasicStaff, ManagerStaff

peter = BasicStaff('Peter', 0, '1000')
john = ManagerStaff('John', 0, 1000, 1000)
print(peter)
print(john)
print('Peter\' s Pay = ', peter.calculatePay())
print('John\'s Pay = ', john.calculatePay())
print('John\'s Performance Bonus = ', john.
      calculatePayBonus())
totalPay = john + peter
print(f'\nTotal Pay for both Staff = {totalPay}')
