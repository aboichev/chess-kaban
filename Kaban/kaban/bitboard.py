
ROWS = 8
COLS = 8

SIZE = ROWS * COLS
state = {}
next_move = 'w'

pieces = 'kqrbnpKQRBNP'
unicodePieces = { key: chr(value) for (key, value) in zip(pieces, range(9812, 9824)) }

def to_index(rank, file):
    return COLS * rank + file


def parse_fen(fen):
    state.clear()
    fields = fen.split(' ')
    ranks = fields[0].split('/')
    next_move = fields[1]

    rank_ix = ROWS - 1
    for rank in ranks:
        char_ix = COLS - 1
        for char in rank:
            if not char.isdigit():
                parse_char(char, rank_ix, char_ix)
                char_ix -= 1
            else:
                char_ix -= int(char)
        rank_ix -= 1

def parse_char(char, rank_ix, char_ix):
    ix = to_index(rank_ix, char_ix)
    add_to_state(char, ix)
    #print(char, ix, end = ', ')

def add_to_state(name, pow):
    num = state.setdefault(name, 0)
    num += (2 ** pow)
    state[name] = num

def should_break(num):
    return num % COLS == 0

def to_ascii():
    end_with = ' '
    print()

    for i in range(SIZE - 1, -1, -1):
        empty = True
        for key in state:
            if empty == True and 2 ** i | state[key] == state[key]:
                print(unicodePieces[key], end = end_with)
                empty = False
        if empty:
            print('_', end = end_with)
        if should_break(i):
            print()


fen = '4k3/pppppppp/8/8/8/8/PPPPPPPP/4K3 w - - 0 1'
parse_fen(fen)
to_ascii()









