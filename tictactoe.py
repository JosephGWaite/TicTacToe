import random
from copy import deepcopy

# zero, one, or two players
# 

#TODO: 
# implement the tree build algorithm
# computer moves shoudl do so from a list of proper moves
# so we need to generate a list of proper moves

class TicTacToe(): 
    def __init__(this, playerCount): 
        this.playerCount = playerCount 
        this.state = [" "," "," "," "," "," "," "," "," "]

    def showBoard(this,state):
        print("╔═╦═╦═╗")
        print("║" + state[0] + "║" + state[1] +"║" + state[2] + "║")
        print("╠═╬═╬═╣")
        print("║" + state[3] + "║" + state[4] +"║" + state[5] + "║")
        print("╠═╬═╬═╣")
        print("║" + state[6] + "║" + state[7] +"║" + state[8] + "║")
        print("╚═╩═╩═╝")
    #returns the position of every empty board square
    #[1,2,4,5,9]
    def allowedMoves(this, state):
        moves = []
        for i in range(len(state)) :
            if state[i] == " " :
                moves.append(i)
        return moves

    #will modify the state
    #player is either X or O

    def moveRandom(this,state, player): 
        state[random.choice(this.allowedMoves(state))] = player

    def moveGiven(this, state, player, position): #no verification
        state[position] = player

    def movePrompt(this, state, player):
        coordPair = eval(input(player +"'s move: ")) #input is of the form (x,y)
        x = coordPair[0]
        y = coordPair[1]
        boardPos = 3*x + y

        if (x > 2 or y > 2 ):
            this.movePrompt(state,player)
        elif state[boardPos] == " ":
            state[boardPos] = player
        else:
            this.movePrompt(state,player)

    def checkWin(this,state):
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

    def boardValue(this, state, player):
        '''return the value of board. 100pts for 3 in a row. 10 for 2. 1 for 1. else 0''' 
        things = []
        #sum up the rows into charsets eg 'xxx' 'xx' 'x  ' 
        things.append(state[0] + state[1] + state[2])
        things.append(state[3] + state[4] + state[5])
        things.append(state[6] + state[7] + state[8])
        #sum up columns 
        things.append(state[0] + state[3] + state[6])
        things.append(state[1] + state[4] + state[7])
        things.append(state[2] + state[5] + state[8])
        #Diagonals
        things.append(state[0] + state[4] + state[8]) 
        things.append(state[2] + state[4] + state[6])
        
        values = []
        for i in range(len(things)):
            # OR we could do 10 ^ things[i].count(player)
            # but I typed this up before I realised. RIP gg fgt
            if things[i].count(player) == 1 and things[i].count(" ") >= 2 :
                values.append(1)
            elif things[i].count(player) == 2 and things[i].count(" ") >= 1:
                values.append(10)
            elif things[i].count(player) == 3 : 
                values.append(100)
            else:
                values.append(0)
        # print(max(values))
        return max(values)

    #if all the moves have been made, there are no more empty tiles
    def checkDraw(this, state):
        return state.count(" ") == 0

    def gameOver(this, state):
        return this.checkWin(state) or this.checkDraw(state)

    """
    minimax(player,board)
        if(game over in current board position)
            return winner
        children = all legal moves for player from this board
        if(max's turn)
            return maximal score of calling minimax on all the children
        else (min's turn)
            return minimal score of calling minimax on all the children
    """
    def statemove(this, state, player, postion):
        x= deepcopy(state)
        x[postion] = player
        return x #there has to be a better way of doing this... 

    #gameboard, value, player, move
    def TreeBuild(this, state, player): #player = (X || O) 

        # assignment says this function must check if game over
        if this.gameOver(state):
            return "GAME OVER"

        #assignment specifies that these mus tbe returned
        print("STATE : \n",state)
        print("VALUE : ")
        print("PLAYER: ",player) 
        print("MOVES: ")

        # here we create a list of valid next-states
        moves, scores, pos = [], [], []
        for i in this.allowedMoves(state): #allowed moves returns a list of empty board pos
            x = this.statemove(state, player, i) #state move returns a state
            moves.append(x) 
            pos.append(i)
            scores.append(this.boardValue(x, player))
        print(scores)
        print(moves)
        y = scores.index(max(scores))
        print("best move")
        print(pos[y],moves[y])
        return pos[y]

    def playOneGame(this):
        this.showBoard(this.state)
        while True:
            print("vvvvvvvvvvvvvvvvvvvvvvvvvvv") 
            this.showBoard(this.state)
            foo = this.TreeBuild(this.state,"x")
            # X's moves
            this.moveGiven(this.state, "x", foo)
            if this.checkWin(this.state):
                print("X WINNER")
                break
            if this.checkDraw(this.state):
                print("DRAW")
                break 
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")

            # O's moves
            this.moveRandom(this.state, "o")  
            this.showBoard(this.state)
            if this.checkWin(this.state) :
                print("O WINNER")
                break
            if this.checkDraw(this.state):
                print("DRAW")
                break
def main():
    game = TicTacToe(2)
    game.playOneGame()

main()
