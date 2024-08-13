def tic (): 
    print('Moves: ')   
    moves = [ 'top left', 'top middle', 'top right',
             'middle left', 'middle', 'middle right',
             'bottom left', 'bottom middle', 'bottom right']
    xwin = []
    owin = []

    def gameboard(xwin, owin):
        board = [' ' for _ in range(9)] # _ is the same as x
        positions = {
            'top left': 0, 'top middle': 1, 'top right': 2,
            'middle left': 3, 'middle': 4, 'middle right': 5,
            'bottom left': 6, 'bottom middle': 7, 'bottom right': 8
        }

        for move in xwin: #move is the same as x
            board[positions[move]] = 'X' # for every move in the move list appended, put an x on the board space accordingly. positions dictionary made to index easier
        for move in owin:
            board[positions[move]] = 'O'

        print(f'''
           |     |        
        {board[0]}  |  {board[1]}  |  {board[2]}  
       ____|_____|____
           |     |        
        {board[3]}  |  {board[4]}  |  {board[5]}  
       ____|_____|____
           |     |        
        {board[6]}  |  {board[7]}  |  {board[8]}  
           |     |       
        ''')

    ask = input('''
       |     |        
       |     |        
   ____|_____|____
       |     |        
       |     |            
   ____|_____|____
       |     |       
       |     |             
       |     |       
      What is your first move: ''')

    if ask in moves:
        move = moves.pop(moves.index(ask))
        xwin.append(move)
        gameboard(xwin, owin)
    else:
        print("Invalid move. Try again.")
        return

    opask = input("What is the opponent's move: ")

    if opask in moves:
        move = moves.pop(moves.index(opask))
        owin.append(move)
        gameboard(xwin, owin)
    else:
        print("Invalid move. Try again.")
        return





    turns = 9
    while turns > 0: #alternates the turns
        
        

        # top row win x
        if "top left" in xwin:
            if "top middle" in xwin:
                if "top right" in xwin:
                    return print('X wins!')
                    break
                    
#middle row win x
        if "middle left" in xwin:
            if "middle middle" in xwin:
                if "middle right" in xwin:
                    return print('X wins!')
                    break
#bottom x win
        if "bottom left" in xwin:
            if "bottom middle" in xwin:
                if "bottom right" in xwin:
                    return print('X wins!')
                    break
#left left x win
        if "bottom left" in xwin:
            if "top left" in xwin:
                if "middle left" in xwin:
                    return print('X wins!')
                    break
#middle middle x win
        if "top middle" in xwin:
            if "middle" in xwin:
                if "bottom middle" in xwin:
                    return print('X wins!')
                    break
#right column win
        if "top right" in xwin:
            if "middle right" in xwin:
                if "bottom right" in xwin:
                    return print('X wins!')
                
#diagonal top left to bottom right
        if "top left" in xwin:
            if "middle" in xwin:
                if "bottom right" in xwin:
                    return print('X wins!')
                    
#diagonal top right to bottom left
        if "top right" in xwin:
            if "middle" in xwin:
                if "bottom left" in xwin:
                    return print('X wins!')
                    
                    
#wins for o
# top row win x
        if "top left" in owin:
            if "top middle" in owin:
                if "top right" in owin:
                    return print('O wins!')
                    
                    
#middle row win x
        if "middle left" in owin:
            if "middle middle" in owin:
                if "middle right" in owin:
                    return print('O wins!')

                    
#bottom x win
        if "bottom left" in owin:
            if "bottom middle" in owin:
                if "bottom right" in owin:
                    return print('O wins!')
                    break
#left left x win
        if "bottom left" in owin:
            if "top left" in owin:
                if "middle left" in owin:
                    return print('O wins!')
                    break
#middle middle x win
        if "top middle" in owin:
            if "middle" in owin:
                if "bottom middle" in owin:
                    return print('O wins!')
                
                    
#right column win
        if "top right" in owin:
            if "middle right" in owin:
                if "bottom right" in owin:
                    return print('O wins!')
            
#diagonal top left to bottom right
        if "top left" in owin:
            if "middle" in owin:
                if "bottom right" in owin:
                    return print('O wins!')
                    
#diagonal top right to bottom left
        if "top right" in owin:
            if "middle" in owin:
                if "bottom left" in owin:
                    return print('O wins!')
        
                
        ask = input("Your move: ")
        if turns == 0:
            return print('Draw!')
        if ask in moves:
            move = moves.pop(moves.index(ask))
            xwin.append(move)
            gameboard(xwin, owin)
        else:
            print("Invalid move. Try again.")
            continue

        opask = input("Opponent's move: ")
        if opask in moves:
            move = moves.pop(moves.index(opask))
            owin.append(move)
            gameboard(xwin, owin)
        else:
            print("Invalid move. Try again.")
            turns -= 1
            continue
        
        

                    
                          

        

tic()
