def tic (): 
    print('moves: ')   
    moves = [ 'top left', 'top middle', 'top right',
             'middle left', 'middle', 'middle right',
             'bottom left', 'bottom middle', 'bottom right']
    xwin = []
    owin = []
    
    print(moves)
    

    ask = input('''
       |     |        
       |     |        
   ____|_____|____
       |     |        
       |     |            
   ____|_____|_____
       |     |        
       |     |             
       |     |       
    


      What is your first move: ''')
    
    if ask == 'top right':
        if ask in moves:
            move = moves.pop(2)
            xwin.append(move)
            opask = input('''
       |     |        
       |     | X     
   ____|_____|____
       |     |        
       |     |            
   ____|_____|_____
       |     |        
       |     |             
       |     |       
    


      What is the next move: ''')
    if ask == 'top middle':
        if ask in moves:
            move = moves.pop(1)
            xwin.append(move)
            opask = input('''
       |     |        
       |  X  |        
   ____|_____|____
       |     |        
       |     |            
   ____|_____|_____
       |     |        
       |     |             
       |     |       
    


      What is the next move: ''')
    
    
    if ask == 'top left':
        if ask in moves:
            move = moves.pop(0)
            xwin.append(move)
            opask = input('''
       |     |        
     X |     |        
   ____|_____|____
       |     |        
       |     |            
   ____|_____|_____
       |     |        
       |     |             
       |     |       
    


      What is the next move: ''')
            
        

    if ask == 'top right':
        if opask in moves:
            if opask == "top left":
                move = moves.pop(0)
                owin.append(move)
                ask = input('''
       |     |        
     O |     | X     
   ____|_____|____
       |     |        
       |     |            
   ____|_____|_____
       |     |        
       |     |             
       |     |       
    


      What is your opponent's move: ''')
    if ask == 'top right':
        if opask in moves:
            if opask == "top middle":
                move = moves.pop(1)
                owin.append(move)
                ask = input('''
       |     |        
       |  O  | X     
   ____|_____|____
       |     |        
       |     |            
   ____|_____|_____
       |     |        
       |     |             
       |     |       
    


      What is the next move: ''')
        
    
            
    


     
    

tic()