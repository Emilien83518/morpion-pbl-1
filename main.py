#AI
#max player: wants to maximise score
#min player: wants to minimise score
#def terminal: terminal state means the game is over
#def value: value of terminal state
#def player: determines whose turn it is in any given game state (either max or min)
#def action: gives all the possible actions we can take in that state  
#def results: tells what the new state of the game will be after the action 
board=[['X','X','O'],
       ['','O',''],
       ['O','X','O']]
def terminal(board):
    for r in board:
        if '' in r: 
            return False 
    for row in board:
        if row[0]==row[1]==row[2] and row[0]!='':
            return True 
    for col in range(3):
        if board[0][col]==board[1][col]==board[2][col] and board[0][col]!='':
            return True     
    if board[0][0]==board[1][1]==board[2][2] and board[0][0]!='':
            return True    
    if board[0][2]==board[1][1]==board[2][0] and board[0][2]!='':
            return True 
    return True
print(terminal(board))
