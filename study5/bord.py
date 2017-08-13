theBord = {'top-L':' ', 'top-M':' ', 'top-R':' ',
           'mid-L':' ', 'mid-M':' ', 'mid-R':' ',
           'low-L':' ', 'low-M':' ', 'low-R':' '}

def printBord(bord):
    print(bord['top-L'] +'|'+bord['top-M']+'|'+ bord['top-R'])
    print('-+-+-')
    print(bord['mid-L'] +'|'+bord['mid-M']+'|'+ bord['mid-R'])
    print('-+-+-')
    print(bord['low-L'] +'|'+bord['low-M']+'|'+ bord['low-R'])

turn = 'X'
for i in range(9):
    printBord(theBord)
    print(turn+ 's turn. where do you put?')
    move = input()
    theBord[move] = turn

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printBord(theBord)
