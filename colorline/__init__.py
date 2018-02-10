COLOR_LIST = {
    'k': 30,
    'r': 31,
    'g': 32,
    'y': 33,
    'b': 34,
    'p': 35,
    'c': 36,
    'w': 37,
}

BCOLOR_LIST = {
    'k': 40,
    'r': 41,
    'g': 42,
    'y': 43,
    'b': 44,
    'p': 45,
    'c': 46,
    'w': 47,
}

MODE_LIST = {
    'default': 0,
    'highlight': 1,
    'underscore': 4,
    'blink': 5,
    'inverse': 7,
    'invisible': 8,
}

def cprint(text, color='w', bcolor='b', mode='default', end='\n'):
    print('\033[{};{};{}m'.format(MODE_LIST[mode], COLOR_LIST[color], BCOLOR_LIST[bcolor]), end=end)
    print(text, end=end)
    print('\033[0m', end=end)

