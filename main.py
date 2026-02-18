import random
action=""
s=True
board=[["","",""],["","",""],["","",""]]
Me=0
Ai=0
row=0
col=0
while Me==0 and Ai==0:
    while s == True:
        row=input("row")
        col=input("column")
        if board[int(row)][int(col)]=="":
            board[int(row)][int(col)]="X"
            s=False
        else:
            s=True
        target="X"
    for outer_idx, inner_list in enumerate(board):
        for inner_idx, value in enumerate(inner_list):
            if value == target:
                print(f"Found {target} at position: [{outer_idx}][{inner_idx}]")
    while s == False:
        row= random.randint(0,2)
        col= random.randint(0,2)
        if board[int(row)][int(col)]=="":
            board[int(row)][int(col)]="O"
            s=True
        else:
            s=False
        target="O"
    for outer_idx, inner_list in enumerate(board):
        for inner_idx, value in enumerate(inner_list):
            if value == target:
                print(f"Found {target} at position: [{outer_idx}][{inner_idx}]")
    if board[0][0]==board[0][1]==board[0][2]=="X" or board[1][0]==board[1][1]==board[1][2]=="X" or board[2][0]==board[2][1]==board[2][2]=="X" or board[0][0]==board[1][0]==board[2][0]=="X" or board[0][1]==board[1][1]==board[2][1]=="X" or board[0][2]==board[1][2]==board[2][2]=="X" or board[0][0]==board[1][1]==board[2][2]=="X" or board[0][2]==board[1][1]==board[2][0]=="X":
        Me = 1
        print("you won")
    elif board[0][0]==board[0][1]==board[0][2]=="O" or board[1][0]==board[1][1]==board[1][2]=="O" or board[2][0]==board[2][1]==board[2][2]=="O" or board[0][0]==board[1][0]==board[2][0]=="O" or board[0][1]==board[1][1]==board[2][1]=="O" or board[0][2]==board[1][2]==board[2][2]=="O" or board[0][0]==board[1][1]==board[2][2]=="O" or board[0][2]==board[1][1]==board[2][0]=="O":
        Ai = 1
        print("you lost")
#AI
#max player: wants to maximise score
#min player: wants to minimise score
#def terminal: terminal state means the game is over
#def value: value of terminal state
#def player: determines whose turn it is in any given game state (either max or min)
#def action: gives all the possible actions we can take in that state  
#def results: tells what the new state of the game will be after the action 
def terminal(board): 
    