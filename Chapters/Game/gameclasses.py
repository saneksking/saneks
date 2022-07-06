import random


class Game:
    def __init__(self, noOfQuestions=0):
        self._noOfQuestions = noOfQuestions

    @property
    def noOfQuestions(self):
        return self._noOfQuestions

    @noOfQuestions.setter
    def noOfQuestions(self, value):
        if value < 1:
            self._noOfQuestions = 1
            print("\nMinimum Number of Questions = 1")
            print("Hence, number of questions will be set 1")
        elif value > 10:
            self._noOfQuestions = 10
            self._noOfQuestions = 1
            print("\nMinimum Number of Questions = 1")
            print("Hence, number of questions will be set1")
        else:
            self._noOfQuestions = value


class BinaryGame(Game):
    def generateQuestions(self):
        score = 0
        for i in range(self._noOfQuestions):
            base10 = random.randint(1, 100)
            userResult = input(f'Преобразуйте число в двоичеую систему счисления: {base10} ')
            while 1:
                try:
                    if userResult == base10:
                        print('Правильный ответ!:)')
                        score += 1
                        break
                    else:
                        print('Ответ не верен!Повезет в другой раз!:( '
                              'Вот правильный ответ {:b}!'.format(base10))
                        break
                except TypeError:
                    print('Вы ввели не число!')
                    userResult = input(f'Попробуйте снова преобразовать число: {base10} ')
        return score

