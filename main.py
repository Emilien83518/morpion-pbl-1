#AI
#max player: wants to maximise score
#min player: wants to minimise score
#def terminal: terminal state means the game is over
#def value: value of terminal state
#def player: determines whose turn it is in any given game state (either max or min)
#def action: gives all the possible actions we can take in that state  
#def results: tells what the new state of the game will be after the action 

import copy

def Terminal(b, p):
    wins = [
        [b[0][0], b[0][1], b[0][2]], [b[1][0], b[1][1], b[1][2]], [b[2][0], b[2][1], b[2][2]],
        [b[0][0], b[1][0], b[2][0]], [b[0][1], b[1][1], b[2][1]], [b[0][2], b[1][2], b[2][2]],
        [b[0][0], b[1][1], b[2][2]], [b[0][2], b[1][1], b[2][0]]
    ]
    return [p, p, p] in wins

def minimax(board_state, is_maximizing):
    # Terminal states
    if Terminal(board_state, "O"): return 10
    if Terminal(board_state, "X"): return -10
    if not any("" in row for row in board_state): return 0

    if is_maximizing:
        best_score = -float('inf')
        for r in range(3):
            for c in range(3):
                if board_state[r][c] == "":
                    board_state[r][c] = "O"
                    score = minimax(board_state, False)
                    board_state[r][c] = ""
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for r in range(3):
            for c in range(3):
                if board_state[r][c] == "":
                    board_state[r][c] = "X"
                    score = minimax(board_state, True)
                    board_state[r][c] = ""
                    best_score = min(score, best_score)
        return best_score
s=True
board=[["","",""],["","",""],["","",""]]
Me=0
Ai=0

while Me==0 and Ai==0:
    while s == True:
        row = input("row (0-2): ")
        column = input("column (0-2): ")
        if board[int(row)][int(column)] == "":
            board[int(row)][int(column)] = "X"
            s = False
        else:
            s = True
    
    if Terminal(board, "X"):
        Me = 1
        print("you won")
        break
    if not any("" in row for row in board):
        print("draw")
        break

  
    best_val = -float('inf')
    best_move = (-1, -1)
    
    for r in range(3):
        for c in range(3):
            if board[r][c] == "":
                board[r][c] = "O"
                move_val = minimax(board, False)
                board[r][c] = ""
                if move_val > best_val:
                    best_move = (r, c)
                    best_val = move_val
    
    if best_move != (-1, -1):
        board[best_move[0]][best_move[1]] = "O"
        print(f"AI plays at: {best_move[0]} {best_move[1]}")
    
    s = True 

    for row_list in board:
        print(row_list)

    if Terminal(board, "O"):
        Ai = 1
        print("you lost")