

import gameclasses
import gametasks

try:
    binaryInstructions = 'В этой игре вы получаете десятичное число.\n' \
                         'Ваша задача - преобразовать его в двоичную систему счисления.\n' \
                         'За каждый правильный ответ начисляется одно очко.\n' \
                         'За ошибочные ответы очки не вычитаются.\n' \
                         'Приятной игры!:)'

    bg = gameclasses.BinaryGame()
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
        choice = input('BinaryGame(1) or exit(-1)?: ')
        while choice != '1' and choice != '-1':
            if choice == '-1':
                break
            print('Ты ввёл неправильный номер игры или выхода! Попробуй заново!')
            choice = input('BinaryGame(1) or exit(-1)?: ')
            continue
        if choice == '-1':
            break
        quest = input('Сколько вопросов ты хочешь (1-10)?: ')
        while 1:
            try:
                num = int(quest)
                break
            except TypeError:
                print('Ты ввёл не число! Попробуй заново!')
                quest = input('Сколько вопросов ты хочешь (1-10)?: ')
        if choice == '1':
            bg.noOfQuestions = num
            gametasks.printInstructions(binaryInstructions)
            score += bg.generateQuestions()
        print(f'Твои полученные очки {score}')

        exitChoice = input('Нажмите Enter для продолжения или (-1) для выхода: ')
        if exitChoice == '-1':
            break
        else:
            continue


except Exception as e:
    print('Неизвестная ошибка! Программа завершается!')
    print(f'Ошибка: {e}!')
