""" 
This class is responsible for starting all the information about the current state of a chess game. It will also be responsible for determining the valid move at the current state. It will also keep a move log.
"""

class GameState():
    def __init__(self) -> None:
        #board is an 8X8 2d list, each elements of the list has 2 characters.
        #The first character represents the color of the piece , "b" or "w"
        #The second character represents the type of the piece, "R","N","B","Q","K" or "P"
        self.board = [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            ["--","--","--","--","--","--","--","--",],
            ["--","--","--","--","--","--","--","--",],
            ["--","--","--","--","--","--","--","--",],
            ["--","--","--","--","--","--","--","--",],
            ["wp","wp","wp","wp","wp","wp","wp","wp"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]
        ]
        self.moveFunctions = {"p": self.getPawnMoves,"R": self.getRookMoves, "N": self.getKnightMoves, "B": self.getBishopMoves, "Q": self.getQueenMoves, "K": self.getKingMoves}
        self.whiteToMove = True
        self.moveLog = []
        self.whiteKingLocation = (7, 4)
        self.blackKingLocation = (0, 4)
        
    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move) #log the move so we can undo it later
        self.whiteToMove = not self.whiteToMove #swap players
        #update the king's location if moved
        if move.pieceMoved == "wk":
            self.whiteKingLocation = (move.endRow, move.endCol)
        elif move.pieceMoved == "bk":
            self.blackKingLocation = (move.endRow, move.endCol)
        
    """Undo the last move made"""
    def undoMove(self):
        if len(self.moveLog) != 0: #make sure that there is a move to undo
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceMoved
            self.whiteToMove = not self.whiteToMove #switch turns back
            #update the king's location if needed
            if move.pieceMoved == "wk":
                self.whiteKingLocation = (move.startRow, move.startCol)
            elif move.pieceMoved == "bk":
                self.blackKingLocation = (move.startRow, move.startCol)
            
    """All moves considering checks"""
    def getValidMoves(self):
        #1) Generate all possible moves
        moves = self.getAllPossibleMoves()
        #2) for each move, make the move
        for i in range(len(moves)-1, -1, -1): #when removing from a list go backwards through that list
            self.makeMove(moves[i])
            
            #3) generate all opponents moves
            oppMoves = self.getAllPossibleMoves()
            #4) for ach of your opponent move see if they attack your king
            
            
        #5) if they do attack your king , is not a valid move
        return moves
    
    
    """
    Determine if the current player in check
    """
    def inCheck(self):
        if self.whiteToMove:
            return self.squareUnderAttack(self.whiteKingLocation[0], self.blackKingLocation[1])
        else:
            return self.squareUnderAttack(self.blackKingLocation[0], self.whiteKingLocation[1])
    
    """
    Determine if the enemy can attack the square r, c    
    """
    def squareUnderAttack(self, r, c):
        self.whiteToMove = not self.whiteToMove #switch to opponents turn
        oppMoves = self.getAllPossibleMoves()
        self.whiteToMove = not self.whiteToMove #switch turns back
        for move in oppMoves:
            if move.endRow == r and  move.endCol == c: #square under attack
                return True
            
        return False
    
    """All moves without considering checks"""
    def getAllPossibleMoves(self):
        moves = []
        for r in range(len(self.board)): #number of rows
            for c in range(len(self.board[r])): #number of cols in given row
                turn = self.board[r][c][0]
                if (turn == "w" and self.whiteToMove) or (turn == "b" and not self.whiteToMove):
                    piece = self.board[r][c][1]
                    self.moveFunctions[piece](r,c,moves) #calls the appropriate move function based on piece type
                        
            
        return moves
                        
    """ 
    Get all the pawn moves for the pawn located at row, col and add these moves to the list
    """
    def getPawnMoves(self,r,c,moves):
        if self.whiteToMove: #white pawn move
            if self.board[r-1][c] == "--": #1 square pawn advance
                moves.append(Move((r,c), (r-1,c), self.board))
                if r == 6 and self.board[r-2][c] == "--": #2 square pawn advance
                    moves.append(Move((r,c), (r-2,c), self.board))
            if c-1 >= 0: #capture to the left
                if self.board[r-1][c-1][0] == "b": #enemy piece to capture
                    moves.append(Move((r,c), (r-1,c-1), self.board))
            if c+1 <= 7: #captures to the right
                if self.board[r-1][c+1][0] == "b": #enemy piece to capture
                    moves.append(Move((r,c), (r-1,c+1), self.board))
        
        else: # black pawn move
            if self.board[r+1][c] == "--":
                moves.append(Move((r,c), (r+1,c), self.board))
                if r == 1 and self.board[r+2][c] == "--":
                    moves.append(Move((r,c), (r+2,c), self.board))
            if c-1 >= 0: #capture to the left
                if self.board[r+1][c-1][0] == "w": #enemy piece to capture
                    moves.append(Move((r,c), (r+1,c-1), self.board))
            if c+1 <= 7: #capture to the right
                if self.board[r+1][c+1][0] == "w":
                    moves.append(Move((r,c), (r+1,c+1), self.board))
            
    
    """ 
    Get all the Rook moves for the pawn located at row, col and add these moves to the list
    """
    def getRookMoves(self,r,c,moves):
        directions = ((-1,0), (0,-1), (1,0), (0,1)) #up, left , doen , right
        enenyColor = "b" if self.whiteToMove else "w"
        for d in directions:
            for i in range(1,8):
                endRow = r + d[0] * i
                endCol = c + d[1] * i
                if 0 <= endRow < 8 and 0 <= endCol < 8: #on board
                    endPiece = self.board[endRow][endCol]
                    if endPiece == "--": #empty space valid 
                        moves.append(Move((r,c), (endRow,endCol), self.board))
                    elif endPiece[0] == enenyColor: #empty piece valid
                        moves.append(Move((r,c), (endRow,endCol) , self.board))
                        break
                    else: #friendly piece invalid
                        break
                else: #off board
                    break
    
    """ 
    Get all the Knight moves for the pawn located at row, col and add these moves to the list
    """
    def getKnightMoves(self,r,c,moves):
        knightMoves = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
        allyColor = "w" if self.whiteToMove else "b"
        for m in knightMoves:
            endRow = r + m[0]
            endCol = c + m[1]
            if 0 <= endRow < 8 and 0 <= endCol < 8:
                endPiece = self.board[endRow][endCol]
                if endPiece[0] != allyColor: #not an ally piece (empty or enemy piece)
                    moves.append(Move((r,c), (endRow, endCol), self.board))
    
    """ 
    Get all the Bishop moves for the pawn located at row, col and add these moves to the list
    """
    def getBishopMoves(self,r,c,moves):
        directions = ((-1,-1), (-1,1), (1,-1), (1,1)) #4 diagonals
        enemyColor = "b" if self.whiteToMove else "w"
        for d in directions: #bishop can move max of 7 squares
            for i in range(1,8):
                endRow = r + d[0] * i
                endCol = c + d[1] * i
                if 0 <= endRow < 8 and 0 <= endCol < 8:
                    endPiece = self.board[endRow][endCol]
                    if endPiece == "--": #empty space valid
                        moves.append(Move((r,c), (endRow,endCol), self.board))
                    elif endPiece[0] == enemyColor: #empty piece valid 
                        moves.append(Move((r,c), (endRow, endCol), self.board))
                        break
                    else: #friendly piece invalid
                        break
                else: #off board
                    break
    
    """ 
    Get all the King moves for the pawn located at row, col and add these moves to the list
    """
    def getKingMoves(self,r,c,moves):
        kingMoves = ((-1,-1), (-1, 0), (-1,1), (0,-1), (0,1), (1, -1), (1, 0), (1, 1))
        allyColor = "w" if self.whiteToMove else "b"
        for i in range(8):
            endRow = r + kingMoves[i][0]
            endCol = c + kingMoves[i][1]
            if 0 <= endRow < 8 and 0 <= endCol < 8:
                endPiece = self.board[endRow][endCol]
                if endPiece[0] != allyColor: #not an ally piece (empty or enemy piece)
                    moves.append(Move((r, c), (endRow, endCol), self.board))
    
    """ 
    Get all the Queen moves for the pawn located at row, col and add these moves to the list
    """
    def getQueenMoves(self,r,c,moves):
        self.getRookMoves(r, c, moves)
        self.getBishopMoves(r, c , moves)
    

class Move():
    #Maps keys to value
    # key : value
    ranksToRows = {"1":7,"2":6,"3":5,"4":4,"5":3,"6":2,"7":1,"8":0}
    rowsToRanks = {v: k for k,v in ranksToRows.items()}
    filesToCols = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7}
    colsToFiles = {v: k for k,v in filesToCols.items()}
    
    
    
    def __init__(self,startSq,endSq, board) -> None:
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        self.moveID = (self.startRow * 1000) + (self.startCol * 100) + (self.endRow * 10) + self.endCol
        print(self.moveID)
        
    """OverRide equal method"""
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Move):
            return self.moveID == other.moveID
        return False
        
    def getChessNotation(self):
        #you can add to make this like real chess notation
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r]