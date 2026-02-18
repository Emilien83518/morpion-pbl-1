#AI
#max player: wants to maximise score
#min player: wants to minimise score
#def terminal: terminal state means the game is over
#def value: value of terminal state
#def player: determines whose turn it is in any given game state (either max or min)
#def action: gives all the possible actions we can take in that state  
#def results: tells what the new state of the game will be after the action 
board=[["X","X","X"],["O","O",""],["O","X","O"]]
def terminal(board):
    for line in board:
        values=[board[i][j] for i,j in line]
        if values=["X","X","X"]:
            return True 
    elif values=["O","O","O"]:
        return True 
    for row in board:
        if '' in row:
            return False 
    return True
 