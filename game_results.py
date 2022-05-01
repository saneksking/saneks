from my_lib import get_terminal_size


def show_text_center(title='', char='*'):
    '''Выводит логотип'''
    title = str(title)
    w, _ = get_terminal_size()
    print(''.center(w, char))
    print(f' {title} '.center(w,char))
    print(''.center(w, char))

def show_footer():
    '''Выводит подвал'''
    w, _ = get_terminal_size()
    print('Программа завершена'.center(w, '='))


def main():
    '''Запуск предложения'''
    #Выводим логотип
    show_text_center(title=' Программа для подсчёта очков в игре ', )
    
    #Основной алгоритм
    print('Программа выполняется...')

    #Выводит подвала
    show_text_center(title=' Программа завершена ', char='=')


if __name__ == '__main__':
    main()
