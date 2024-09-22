#game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-",]

#checks if game's still playing
gameGo = True

#winner
winner = None

#turn
nowPlaying = "X"

#game
def playGame():
    #loop to play the game
    
    while gameGo:
        
        #asking position to play to current player
        handTurns(nowPlaying)
        
        #checks the game
        overGameCheck()
        
        #changes player
        changePlayer()
       
        #verifies who wins or tie
    if winner == "X" or winner == "O":
        print(f"winner is {winner}!")
        displayBoard()
    elif winner == None:
        print("It's a tie!")
        displayBoard()
    


def displayBoard():
    #displays board with position in list and printing brackets to separate them
    print("[",board[0],"]","[",board[1],"]","[",board[2],"]")
    print("[",board[3],"]","[",board[4],"]","[",board[5],"]")
    print("[",board[6],"]","[",board[7],"]","[",board[8],"]")

#makes who to play and where to place
def handTurns(mark):
    validInput = False
    #verifies first to place option
    while not validInput:
        displayBoard()
        print(f"{mark}'s turn")
        playPos = input("choose position to play from 1 to 9 (left to right): ")
        
        #verifies if option is playable
        while playPos not in ["1", "2", "3", "4" ,"5" ,"6" ,"7" ,"8", "9"]:
            playPos = input("choose position to play from 1 to 9 (left to right): ")
        playPos = int(playPos) - 1
        
        #verfies if position available
        if board[playPos] == "-":
            validInput = True
        else:
            print("Already placed there. Go again")
        
    board[playPos] = mark
        
    
#verifies if someone wins    
def checkWin():
    
    global winner
    
    rowWin = checkRow()
    colWin = checkCol()
    diagWin = checkDiag()
    
    if rowWin:
        winner = checkRow()
    elif colWin:
        winner = checkCol()
    elif diagWin:
        winner = checkDiag()
    else:
        winner = None
    return 


#verifies if someone wins with a row win
def checkRow():
    global gameGo
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    if row1 or row2 or row3:
        gameGo = False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return


#verifies if someone wins with a column win
def checkCol():
    global gameGo
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"
    if col1 or col2 or col3:
        gameGo = False
    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]
    return


#verifies if someone wins with a diagonal win
def checkDiag():
    global gameGo
    diag1 = board[2] == board[4] == board[6] != "-"
    diag2 = board[0] == board[4] == board[8] != "-"
    if diag1 or diag2:
        gameGo = False
    if diag1:
        return board[2]
    elif diag2:
        return board[0]
    return


#verifies if the game ties
def checkTie():
    global gameGo
    if "-" not in board:
        gameGo = False
    return


#changes current player
def changePlayer():
    global nowPlaying
    if nowPlaying == "X":
        nowPlaying = "O"
    elif nowPlaying == "O":
        nowPlaying = "X"
    return


#checks if the game ended (calling functions to check if its a win or its a tie)
def overGameCheck():
    checkWin()
    checkTie() 

#calls the game function
playGame()