""" 
This is our main drive file. It will be responsible for handlind user input and displyaing the current gameState.
"""

import pygame as p 
import chessEngine

WIDTH = HEIGHT = 512 #400 is another option
DIMENSION = 8 #Dimension of the chess board is 8X8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 #for animation later on
IMAGES = {}

""" 
Initialize a global dictionary of images. This will be called exactly once in the main
"""
def loadImages():
    pieces = ["wp","wR","wN","wB","wK","wQ","bp","bR","bN","bB","bK","bQ"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
    #Note: we can access an image by saying "IMAGES["wp"]"

""" 
The main driver for our code. This will handle user input and updating the graphics
"""

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = chessEngine.GameState()
    # print(gs.board)
    validMoves = gs.getValidMoves()
    moveMade = False #flag variable when a move is made
    loadImages() #only do this once, before the while loop
    running = True
    sqSelected = () #no square is selected , keep track of the last click of the user (tuple : (row,col))
    playerClicks = [] #keep track of player click
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            #mouse handler
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() #(x,y) location of mouse
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                if sqSelected == (row,col): #the user clicks the same square twice
                    sqSelected = () #deselect
                    playerClicks = [] #clear player clicks
                else:
                    sqSelected = (row,col)
                    playerClicks.append(sqSelected) #append both 1st click and 2nd click
                if len(playerClicks) == 2: #after 2nd click
                    move = chessEngine.Move(playerClicks[0],playerClicks[1], gs.board)
                    print(move.getChessNotation())
                    if move in validMoves:
                        gs.makeMove(move)
                        moveMade = True
                        sqSelected = () #reset user click
                        playerClicks = []
                    else:
                        playerClicks = [sqSelected]
            #key handler
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:
                    gs.undoMove()
                    moveMade = True
                    
        if moveMade:
            validMoves = gs.getValidMoves()
            moveMade = False
        drawGameState(screen,gs)
        clock.tick(MAX_FPS)
        p.display.flip()
        
        
""" 
Responsible for all the graphics within a current game state
"""
def drawGameState(screen,gs):
    drawBoard(screen) #draw squares on the board
    #add in piece highlighting and move suggestion (later)
    drawPieces(screen, gs.board) #draw pieces on top of that squares
    
""" 
Draw the sqaures on the board
"""
def drawBoard(screen):
    colors = [p.Color("light gray"), p.Color("dark green")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))

""" 
Draw the pieces on the board using Gamestate.board
"""
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece!= "--":  # Not an empty square
                # print(f"Drawing {piece} at ({r}, {c})")  # Debugging output
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

if __name__ == "__main__":
    main()