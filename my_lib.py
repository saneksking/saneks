import os

def get_terminal_size():
    '''Функция которая возвращает ширину и высоту'''
    width, height = os.get_terminal_size()
    return width, height


def get_type(obj):
    '''принимает любой объект, возвращает его тип'''
    return type(obj)



