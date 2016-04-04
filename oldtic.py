#waitejg
#1403712

#Lab 8 Rakcetball


import random 

#show gamestate in human readable format. takes the state of the game
# which should be a list of length 9 
def showBoard(state):
    print("╔═╦═╦═╗")
    print("║" + state[0] + "║" + state[1] +"║" + state[2] + "║")
    print("╠═╬═╬═╣")
    print("║" + state[3] + "║" + state[4] +"║" + state[5] + "║")
    print("╠═╬═╬═╣")
    print("║" + state[6] + "║" + state[7] +"║" + state[8] + "║")
    print("╚═╩═╩═╝")

#automatically make a move
#will modify the variable passed in 
def oPlaceAuto(state):
    #sort of a do while loop, ensures we make at least one move
    while True:
        boardPos = random.randrange(9) #here we make the move, all pos are valid
        if state[boardPos] == " ": #if that move is on an empty tile, place an o there 
            state[boardPos] = "o"
            break #and exit our while true loop
        #if it's not a valid move, ie a play has already moved there, make another.
        # and keep going until we get a valid move

#same as above       
def xPlaceAuto(state):
    while True:
        boardPos = random.randrange(9)
        if state[boardPos] == " ":
            state[boardPos] = "x"
            break
        
def checkWin(state):
    #check rows if they any are equal, but not to the " " empty tile
    if (state[0] == state[1] == state[2] and state[0]!= " ") or\
       (state[3] == state[4] == state[5] and state[3]!= " ") or\
       (state[6] == state[7] == state[8] and state[6]!= " "):
        return 1
    
    #check columns for equality, but not to empty tile
    elif (state[0] == state[3] == state[6] and state[0] != " ") or\
         (state[1] == state[4] == state[7] and state[1] != " ") or\
         (state[2] == state[5] == state[8] and state[2] != " "):
        return 1
    
    #check diagonales (0,4,8) (2,4,6)
    elif (state[0] == state[4] == state[8] and state[4] != " ") or\
         (state[2] == state[4] == state[6] and state[4] != " "):
        return 1
    
    # no winner, yet
    else:
        return 0

#if all the moves have been made, there are no more empty tiles
def checkDraw(state):
    return state.count(" ") == 0

#monte carlo sort of sim
def statistics(totalPlayed):
    #init vars 
    oWins = 0
    xWins = 0
    draws = 0
    #num of sims is passed as a param
    for i in range(totalPlayed):
        #play a game and record winner
        game = playOneGame()
        #keep track of winner
        if  game == "O":
            oWins += 1
        elif game == "X":
            xWins += 1
        elif game == "DRAW":
            draws += 1
    #print the probability of O winning. seems to be around .285 
    print("O wins / total Games =", oWins/totalPlayed)
    
        
def playOneGame():
    #start with an empty board
    state = [" "," "," "," "," "," "," "," "," "]
    while True:
        xPlaceAuto(state) #will return true if valid move, else invalid. and we do it again
        #after a move is made, check winner, then check if draw.
        #if either, exit and return the winner
        if checkWin(state):
            return("X")
            break
        if checkDraw(state):
            return("DRAW")
            break

        oPlaceAuto(state) #make move 
        if checkWin(state): #check if winner
            return("O")#if so, return and exit loop
            break
        if checkDraw(state): #check if draw 
            return("DRAW")
            break
def main():
    playOneGame()
    
statistics(50)
