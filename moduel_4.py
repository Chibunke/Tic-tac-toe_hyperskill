a = input('Enter cells:')
#a = ' '.join(a)
#a = a.split()
def game_bord():
    print('---------\n'
    '|', a[0], a[1], a[2], '|\n'
    '|', a[3], a[4], a[5], '|\n'
    '|', a[6], a[7], a[8], '|\n'
    '---------')

game_bord()
def checkers():
    from string import ascii_letters
    global a
    a_ = input('Enter the coordinates:')
    for input_ in a_:

        if input_ in list(ascii_letters):
            print('You should enter numbers!')
            checkers()
            break
    if a_ not in ['1 1', '1 2', '1 3', '2 1', '2 2','2 3', '3 1', '3 2', '3 3']:
        print('Coordinates should be from 1 to 3!')
        checkers()
    else:

        def coordinate():
            global a
            nonlocal a_
            a_ = a_.split()
            if a_ == list('13'):
                if a[0] == '_':
                    a = list(a)
                    a[0] = 'X'
                    ''.join(a)
                    game_bord()
                else:
                    print('This cell is occupied! Choose another one!')
                    checkers()

            elif a_ == list('23'):
                if a[1] == '_':
                    a = list(a)
                    a[1] = 'X'
                    ''.join(a)
                    game_bord()
                else:
                    print('This cell is occupied! Choose another one!')
                    checkers()

            elif a_ == list('33'):
                if a[2] == '_':
                    a = list(a)
                    a[2] = 'X'
                    ''.join(a)
                    game_bord()
                else:
                    print('This cell is occupied! Choose another one!')
                    checkers()

            elif a_ == list('12'):
                if a[3] == '_':
                    a = list(a)
                    a[3] = 'X'
                    ''.join(a)
                    game_bord()
                else:
                    print('This cell is occupied! Choose another one!')
                    checkers()

            elif a_ == list('22'):
                if a[4] == '_':
                    a = list(a)
                    a[4] = 'X'
                    ''.join(a)
                    game_bord()
                else:
                    print('This cell is occupied! Choose another one!')
                    checkers()
            elif a_ == list('32'):
                if a[5] == '_':
                    a = list(a)
                    a[5] = 'X'
                    ''.join(a)
                    game_bord()
                else:
                    print('This cell is occupied! Choose another one!')
                    checkers()
            elif a_ == list('11'):
                if a[6] == '_':
                    a = list(a)
                    a[6] = 'X'
                    ''.join(a)
                    game_bord()
                else:
                    print('This cell is occupied! Choose another one!')
                    print('r')
                    checkers()
            elif a_ == list('21'):
                if a[7] == '_':
                    a = list(a)
                    a[7] = 'X'
                    ''.join(a)
                    game_bord()
                else:
                    print('This cell is occupied! Choose another one!')
                    checkers()
            elif a_ == list('31'):
                if a[8] == '_':
                    a = list(a)
                    a[8] = 'X'
                    ''.join(a)
                    game_bord()
                else:
                    print('This cell is occupied! Choose another one!')
                    checkers()
        coordinate()
checkers()