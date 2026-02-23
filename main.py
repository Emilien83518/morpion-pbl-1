#AI
#max player: wants to maximise score
#min player: wants to minimise score
#def terminal: terminal state means the game is over
#def value: value of terminal state
#def player: determines whose turn it is in any given game state (either max or min)
#def action: gives all the possible actions we can take in that state  
#def results: tells what the new state of the game will be after the action 

def terminal(board):
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
    for item in board:
        if '' in item:
            return False
    return True
def value(board):
    if board[0][0]==board[0][1]==board[0][2]=="X" or board[1][0]==board[1][1]==board[1][2]=="X" or board[2][0]==board[2][1]==board[2][2]=="X" or board[0][0]==board[1][0]==board[2][0]=="X" or board[0][1]==board[1][1]==board[2][1]=="X" or board[0][2]==board[1][2]==board[2][2]=="X" or board[0][0]==board[1][1]==board[2][2]=="X" or board[0][2]==board[1][1]==board[2][0]=="X":
        return 1 
    elif board[0][0]==board[0][1]==board[0][2]=="O" or board[1][0]==board[1][1]==board[1][2]=="O" or board[2][0]==board[2][1]==board[2][2]=="O" or board[0][0]==board[1][0]==board[2][0]=="O" or board[0][1]==board[1][1]==board[2][1]=="O" or board[0][2]==board[1][2]==board[2][2]=="O" or board[0][0]==board[1][1]==board[2][2]=="O" or board[0][2]==board[1][1]==board[2][0]=="O":
        return -1
    return 0
