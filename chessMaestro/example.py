import json

grob = open('grob_2.json', 'r')
gr = json.load(grob)
grob.close()
br = gr.copy()


def get_move(move: str, br=gr.copy()):
    y = br.get(move)
    variants = br.get(move).keys()
    return take_move(list(variants), y)


def take_move(variants: list, y: dict):
    print('Выбери вариант:')
    for index, variant in enumerate(variants):
        print(f'{index + 1} - {variants[index][-3:]}')
    yr_move = variants[int(input("Твой выбор: ")) - 1]
    print(yr_move)
    return get_move(yr_move, br=y)


if __name__ == '__main__':
    # print(list(gr.get("1e_w_g4_").keys())[1])
    print(get_move('1e_w_g4_'))
    print(br.get('1e_w_g4_'))
    print(br.keys())
