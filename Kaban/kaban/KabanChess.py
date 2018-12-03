import sys
from kaban.to_ascii import to_ascii

class KabanChess:
    def __init__(self, fen_str = None):
        self._fen = fen_str or 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
        self._pos = {}
        self._moves = {}
        self._rows = 8
        self._cols = 8
        _parse_fen(self)
        _gen_moves(self)

    @property
    def board_size(self):
        return self._rows * self._cols

    def to_ascii(self):
        return to_ascii(self._cols, self._rows, self._pos)

    def moves_to_ascii(self):
        return to_ascii(self._cols, self._rows, self._moves)

def _parse_fen(self):
    self._pos.clear()
    fields = self._fen.split(' ')
    ranks = fields[0].split('/')
    self._next_move = fields[1]

    rank_ix = self._rows - 1
    for rank in ranks:
        char_ix = self._cols - 1
        for char in rank:
            if not char.isdigit():
                _parse_piece_position(self, char, rank_ix, char_ix)
                char_ix -= 1
            else:
                char_ix -= int(char)
        rank_ix -= 1

def _parse_piece_position(self, char, rank_ix, char_ix):
    ix = _to_index(self, rank_ix, char_ix)
    _add_to_state(self, char, ix, self._pos)

def _to_index(self, rank, file):
    return self._cols * rank + file

def _add_to_state(self, name: str, pow: int, state = {}):
    num = state.setdefault(name, 0)
    num |= (2 ** pow)
    state[name] = num

def _gen_moves(self):
    if self._next_move == 'w':
        pieces = 'P'
    else:
        pieces = 'p'

    for piece in pieces:
        if piece in 'P':
            pawn_capture = (self._pos[piece] ^ (self._pos[piece] & 72340172838076673)) << 7
            pawn_capture |= (self._pos[piece] ^ (self._pos[piece] & 9259542123273814144)) << 9
            self._moves[piece] = pawn_capture

if __name__ == "__main__":
    fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    if len(sys.argv) > 1:
        fen = sys.argv[1]
        game = KabanChess(fen)
    else:
        game = KabanChess()
    game.to_ascii()
    game.moves_to_ascii()