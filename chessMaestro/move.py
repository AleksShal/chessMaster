import json

grob = open('grob_2.json', 'r')
gr = json.load(grob)
grob.close()


def get_move(move: str, branch=gr.copy()):
    """

    :param move: ход в формате str
    :param branch: дерево вариантов, в формате dict
    :return: список вариантов после хода(list(variants)), дерево вариантов после хода(branch_2)
    """
    branch_2 = branch.get(move)
    variants = branch.get(move).keys()
    return take_move(list(variants), branch_2)


def take_move(variants: list, branch_2: dict):
    """

    :param variants: список ходов после хода 'move'
    :param branch_2: дерево вариантов после хода(branch_2)
    :return: следующий ход, дерево вариантов после хода(branch_2)
    """
    print('Выбери вариант:')
    for index, variant in enumerate(variants):
        print(f'{index + 1} - {variants[index][-3:]}')
    yr_move = variants[int(input("Твой выбор: ")) - 1]
    print(yr_move)
    return get_move(yr_move, branch=branch_2)


if __name__ == '__main__':
    print(get_move('1e_w_g4_'))
