def stick_game():
    print('welcome to the sticks game')
    print('rules:you can pick 1,2,or 3 sticks in one turn')
    print('the player who picks the last stick loses')
    no_of_sticks=16
    player1=input('enter the first players name:')
    player2=input('enter the second players name:')
    print('game started')
    remainingsticks=no_of_sticks
    while (remainingsticks>0):
        player=player1
        print('stick remaining=',remainingsticks)
        n=int(input(f'{player} pick(1,2,or3sticks:'))
        remainingsticks=remainingsticks-n
        if remainingsticks<=0:
            print(f'{player} picks the last stick and loses the game')
        else:
            player=player2
            print(f'stick remaining',remainingsticks)
            i=int(input((f'{player} pick1,2or3 sticks:')))
            remainingsticks=remainingsticks-i
            if remainingsticks<=0:
                print(f'{player} picks the last stick and loses the game')
stick_game()