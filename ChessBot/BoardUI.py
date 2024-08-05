"""WIP - Needs severe restructuring for drag and drop features and to draw from BitBoards etc for moves and update bitboard with moves"""


import pygame as p
from Pieces import ChessBoard, Piece

#Colours
BACKGROUND = (255,255,255)
BLACK = (221,161,94)
WHITE = (250,237,205)

pieces = {}

"""Map bit positions to board coordinates"""
def bitboard_to_board(bitboard, piece_name):
    #Convert np uint64 to int for bitwise op
    bitboard = int(bitboard)
    board = [['..' for _ in range(8)] for _ in range(8)]
    #piece_name matchs names in pieces dictionary  WIP
    piece_mapping = {
        "KINGWHITE": 'wK', "QUEENWHITE": 'wQ', "BISHOPWHITE": 'wB',
        "KNIGHTWHITE": 'wN', "ROOKWHITE": 'wR', "PAWNWHITE": 'wP',
        "PAWNBLACK": 'bP', "ROOKBLACK": 'bR', "KNIGHTBLACK": 'bN',
        "BISHOPBLACK": 'bB', "QUEENBLACK": 'bQ', "KINGBLACK": 'bK'
    }
    piece_name = piece_mapping.get(piece_name, '..')
    for pos in range(64):
        if (bitboard >> pos) & 1:
            row = 7 - (pos // 8)
            col = pos % 8
            board[row][col] = piece_name
    return board

"""Map ChessBoard object to 2D array"""
def chessboard_to_board(chessboard):
    board = [['..' for _ in range(8)] for _ in range(8)]
    for piece_name, bitboard in chessboard.pieces.items():
        board_part = bitboard_to_board(bitboard, piece_name)
        for row in range(8):
            for col in range(8):
                if board_part[row][col] != '..':
                    board[row][col] = board_part[row][col]
    return board

"""Window + Board"""
def initialise(chessboard):
    p.init()

    global Width, Height, SCREEN, SquareSize
    Width, Height = 640, 640
    SquareSize = Width // 8
    SCREEN = p.display.set_mode((Width, Height))
    SCREEN.fill(BACKGROUND)

    loadPieces()
    
    open = True 
    while open: 
        board = chessboard_to_board(chessboard)
        BoardSquares()
        BoardUpdateVisuals(board, pieces)

        for event in p.event.get():
            if event.type == p.QUIT:
                open = False
            elif event.type == p.KEYDOWN:
                if event.key == p.K_ESCAPE:
                    open = False

            # Dragging/Movement vvvv WIP
            if event.type == p.MOUSEBUTTONDOWN:
                x_init, y_init = p.mouse.get_pos()
                if CheckPieceUnderMouse(x_init, y_init, board):
                    held = board[y_init // SquareSize][x_init // SquareSize]
                    hold = True
                    while hold:
                        p.event.set_grab(True)
                        for event in p.event.get():
                            if event.type == p.MOUSEBUTTONUP:
                                x, y = p.mouse.get_pos()    
                                # drop pos                                                
                                hold = False
                                p.event.set_grab(False)

        p.display.flip()
    return

"""Board Pattern"""
def BoardSquares():
    for col in range(0, Width, SquareSize):
        for row in range(0, Height, SquareSize):
            Colour = WHITE if ((col // SquareSize + row // SquareSize) % 2 == 0) else BLACK #Alternating colours, uses each square index sum  (col//SquareSize gives the index on the board)
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
                SCREEN.blit(pieces[board[row][col]], p.Rect(col * SquareSize, row * SquareSize, SquareSize, SquareSize))
    return 

"""True if piece under mouse"""
def CheckPieceUnderMouse(x, y, board):
    col = x // SquareSize
    row = y // SquareSize
    return board[row][col] != '..'

def main():
    chessboard = ChessBoard()
    initialise(chessboard)
    return

if __name__ == "__main__":
    main()