a = input()

print('---------\n'
'|', a[0], a[1], a[2], '|\n'
'|', a[3], a[4], a[5], '|\n'
'|', a[6], a[7], a[8], '|\n'
'---------')
win_list = []
game = False

def win(g):
    # horizontal win for x or o
    if a[0] == a[1] == a[2] == g:
        win_list.append('{} win'.format(g))

    elif a[3] == a[4] == a[5] == g:
        win_list.append('{} win'.format(g))

    elif a[6] == a[7] == a[8] == g:
        win_list.append('{} win'.format(g))

        # vertical win for x or o
    elif a[0] == a[3] == a[6] == g:
        win_list.append('{} win'.format(g))


    elif a[1] == a[4] == a[7] == g:
        win_list.append('{} win'.format(g))


    elif a[2] == a[5] == a[8] == g:
        win_list.append('{} win'.format(g))

        # diagonal win for x or o
    elif a[0] == a[4] == a[8] == g:
        win_list.append('{} win'.format(g))


    elif a[2] == a[4] == a[6] == g:
        win_list.append('{} win'.format(g))

x_s = a.count('X')
o_s = a.count('O')
if x_s - o_s >= 2:
    print("Impossible")
elif o_s - x_s >= 2:
    print("Impossible")
else:

    # winning conditions
    win('X')
    win('O')
    if 'X win' in  win_list and 'O win' in win_list:
        print('Impossible')
    elif 'X win' in win_list and 'O win' not in win_list:
        print('X wins')
    elif 'X win' not in win_list and 'O win' in win_list:
        print('O wins')
    else:
        game = True
    # none winning condition such as draw or game not finished

    if game:

        if x_s + o_s != 9:
            print('Game not finished')

        else:
            print('Draw')




