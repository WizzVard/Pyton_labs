import random

# Task 10
ROWS = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}


def validate_input(row, col):
    return get_color(row, col) if 'a' <= row <= 'h' and 1 <= col <= 8 else 'Invalid input'


def get_color(row, col):
    return 'white' if (ROWS[row] + col) % 2 == 0 else 'black'

# Task 11


def dec_to_bin(q):
    result = ''
    while q:
        r = str(q % 2)
        result = ''.join([result, r])
        q = q // 2
    return result[::-1]


def bin_to_dec(binary):
    result = 0
    pos = 0
    for i in reversed(binary):
        result += int(i) * 2 ** pos
        pos += 1
    return result

# Task 12


def r_p_s(value):
    options = {'rock': 'r',
               'paper': 'p',
               'scissors': 's'}

    if value not in options:
        return 'Invalid input'

    you = options[value]
    opp = random.choice(list(options.values()))
    # return 'You won' if (you == 's' and opp == 'p') or (you == 'r' and opp == 's') or (you == 'p' and opp == 'r') \
    #     else 'Its draw' if you == opp else 'You loose'
    if you == opp:
        return 'Its draw'
    elif (you == 's' and opp == 'p') or (you == 'r' and opp == 's') or (you == 'p' and opp == 'r'):
        return 'You won'
    else:
        return 'You loose'


if __name__ == '__main__':
    row = input('Enter the row(a - h): ')
    col = int(input('Enter the col(1 - 8): '))
    print(validate_input(row, col))

    number = int(input('Enter decimal number: '))
    print(f'{number} in Decimal is {dec_to_bin(number)} in Binary')

    binary = input('Enter binary number: ')
    print(f'{binary} in Binary is {bin_to_dec(binary)} in Decimal')

    game = input('Enter rock/scissors/paper: ')
    print(r_p_s(game))
