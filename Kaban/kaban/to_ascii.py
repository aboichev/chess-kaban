def to_ascii(cols: int, rows: int, pieces: dict):
    end_with = ' '
    print()

    for i in range(cols * rows - 1, -1, -1):
        empty = True
        for key in pieces:
            if empty == True and 2 ** i | pieces[key] == pieces[key]:
                print(key, end = end_with)
                empty = False
        if empty:
            print('_', end = end_with)
        if i % rows == 0:
            print()
    print()
