grob = open('grob.txt', 'r')
move_vars = grob.read().split(sep='\n')
grob.close()


def move_go(move: str):
    return number_move(move)


def number_move(move: str):
    try:
        move_number = int(move[:2])
    except ValueError:
        move_number = int(move[:1])
    return move_variants(move_number, move)


def move_variants(num_move: int, move):
    variants = []
    next_move = str(num_move + 1)
    if len(next_move) == 1:
        next_move += 'e'
    for move in move_vars:
        if next_move == move[:2]:
            variants.append(move)
    if not variants:
        print('Вариант закончен')
    return take_variant(variants, next_move, move)


def take_variant(variants: list, next_move, move):
    print('Выбери вариант:')
    for index, variant in enumerate(variants):
        print(f'{index + 1} - {variants[index][-3:]}')
    var = int(input("Твой выбор: ")) - 1
    return your_move(var, next_move, move)


def your_move(move_var: int, next_move, move):
    if move[3] or move[4] == 'w':
        yr_move = next_move + '_' + 'b' + '_' + f'{[move for move in variants][var][-3:]}'
    elif move[3] or move[4] == 'b':
        yr_move = next_move + '_' + 'b' + '_' + f'{[move for move in variants][var][-3:]}'
    print(yr_move)
    return move_go(yr_move)


if __name__ == '__main__':
    print(move_go('1_w_g4'))
    # print(move_variants(1))
