import pygame as p

#Colours
BACKGROUND = (255,255,255)
BLACK = (221,161,94)
WHITE = (250,237,205)

pieces = {}

"""Window + Board"""
def initialise(board):
    p.init()
    
    global Width, Height, SCREEN, SquareSize
    Width, Height = 640, 640
    SquareSize = Width//8
    SCREEN = p.display.set_mode((Width, Height))
    SCREEN.fill(BACKGROUND)

    loadPieces()
    
    open = True 
    while open: 
        BoardSquares()
        BoardUpdateVisuals(board, pieces)

        for event in p.event.get():
            if event.type == p.QUIT:
                open = False
            elif event.type == p.KEYDOWN:
                if event.key == p.K_ESCAPE:
                    open = False

            #Dragging/Movement vvvv
            if event.type == p.MOUSEBUTTONDOWN:
                x_init,y_init = p.mouse.get_pos()
                if CheckPieceUnderMouse(x_init,y_init,board) == True:
                    piece = board[y_init//SquareSize][x_init//SquareSize]
                    
                    hold = True
                    while hold:
                        p.event.set_grab(True)
                        for event in p.event.get():
                            if event.type == p.MOUSEBUTTONUP:
                                x,y = p.mouse.get_pos()                               
                                board = TestLegal(piece, board, x, y, x_init, y_init)                      
                                hold = False
                                p.event.set_grab(False)  

        p.display.flip()
    return

################################################### MAKE OOP  ##################################################
def TestLegal(piece, board, x, y, x_init, y_init):
    if board[y//SquareSize][x//SquareSize][0] != piece[0]: #piece[0]/...[0] are first letters
        if LegalChecker[piece[1]](piece, board, x, y, x_init, y_init) == True:
            pass
        board[y_init//SquareSize][x_init//SquareSize] = ".."
        board[y//SquareSize][x//SquareSize] = piece
    return board



"""Piece checks"""

def LegalBishop(piece, board, x, y, x_init, y_init):
    return 

def LegalQueen(piece, board, x, y, x_init, y_init):
    return

def LegalKnight(piece, board, x, y, x_init, y_init):
    return

def LegalRook(piece, board, x, y, x_init, y_init):
    return 

def LegalPawn(piece, board, x, y, x_init, y_init):
    return 

def LegalKing(piece, board, x, y, x_init, y_init): #Not done: checks, castling or capture into check  -- Do in another function
    return 

LegalChecker = {"B": LegalBishop, "Q": LegalQueen, "K": LegalKing, "P": LegalPawn, "N": LegalKnight, "R": LegalRook}

################################################### MAKE OOP  ##################################################



"""Board Pattern"""
def BoardSquares():
    for col in range(0, Width, SquareSize):
        for row in range(0, Height, SquareSize):
            Colour = WHITE if ((col//SquareSize+row//SquareSize)%2 == 0) else BLACK   #Alternating colours, uses each square index sum  (col//SquareSize gives the index on the board)
            Square = p.Rect(col, row, SquareSize, SquareSize)
            p.draw.rect(SCREEN, Colour, Square)
    return 

"""Loading Pieces"""
def loadPieces():
    names = ['bB', 'bK', 'bN', 'bP', 'bQ', 'bR', 'wB', 'wK', 'wN', 'wP', 'wQ', 'wR']
    for piece in names:
        pieces[piece] = p.transform.scale(p.image.load(f'pixel/{piece}.png'), (SquareSize, SquareSize)) #Scale png to board size
    return pieces

"""Piece Placement"""
def BoardUpdateVisuals(board, pieces):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == '..':
                pass
            else:
                SCREEN.blit(pieces[board[row][col]],p.Rect(col*SquareSize,row*SquareSize, SquareSize, SquareSize))
    return 

"""True if piece under mouse"""
def CheckPieceUnderMouse(x,y, board):
    col = x//SquareSize
    row = y//SquareSize
    return board[row][col] != '..'






def main():
    board = [['bR','bN','bB','bQ','bK','bB','bN','bR'],
             ['bP','bP','bP','bP','bP','bP','bP','bP'],
             ['..','..','..','..','..','..','..','..'],
             ['..','..','..','..','..','..','..','..'],
             ['..','..','..','..','..','..','..','..'],
             ['..','..','..','..','..','..','..','..'],
             ['wP','wP','wP','wP','wP','wP','wP','wP'],
             ['wR','wN','wB','wQ','wK','wB','wN','wR']]
    initialise(board)
    return

if __name__ == "__main__":
    main()