

import gameclasses
import gametasks

try:
    mathInstructions = 'В этой игре вам предлагается решить простую арифметическую задачу.\n' \
                       'За каждый правильный ответ вам начисляется одно очко.\n' \
                       'За ошибочные ответы очки не вычитаются.\n' \
                       'Приятной игры!:)'

    binaryInstructions = 'В этой игре вы получаете десятичное число.\n' \
                         'Ваша задача - преобразовать его в двоичную систему счисления.\n' \
                         'За каждый правильный ответ начисляется одно очко.\n' \
                         'За ошибочные ответы очки не вычитаются.\n' \
                         'Приятной игры!:)'

    bg = gameclasses.BinaryGame()
    mg = gameclasses.MathGame()
    userName = input('Введите своё имя: ')
    score = int(gametasks.getUserScore(userName))
    if score == -1:
        newUser = True
        score = 0
    else:
        newUser = False

    print(f'Привет {userName}! Добро пожаловать в игру!')
    print(f'Твои очки: {score}')

    userChoice = 0

    while userChoice != '-1':
        choice = input('MathGame(1) or BinaryGame(2)?: ')
        while choice != '1' and choice != '2':
            print('Ты ввёл неправильный номер игры! Попробуй заново!')
            continue
        quest = input('Сколько вопросов ты хочешь (1-10)?: ')
        while 1:
            try:
                num = int(quest)
                break
            except TypeError:
                print('Ты ввёл не число! Попробуй заново!')
                quest = input('Сколько вопросов ты хочешь (1-10)?: ')
        if choice == '1':
            mg.noOfQuestions = num
            gametasks.printInstructions(mathInstructions)
            score += mg.generateQuestions()
        elif choice == '2':
            bg.noOfQuestions = num
            gametasks.printInstructions(binaryInstructions)
            score += bg.generateQuestions()
        print(f'Твои полученные очки {score}')

        exitChoice = input('Нажмите Enter для продолжения или (-1) для выхода: ')
        if exitChoice == '-1':
            break
        else:
            continue
    gametasks.updateUserScore(True, 'Saneks', '0')


except Exception as e:
    print('Неизвестная ошибка! Программа завершается!')
    print(f'Ошибка: {e}!')
