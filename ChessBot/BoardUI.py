import pygame as p
import numpy as np
from Pieces import ChessBoard, Piece

#Colours
BACKGROUND = (255,255,255)
BLACK = (221,161,94)
WHITE = (250,237,205)

pieces = {}

"""Map bit positions to board coordinates"""
def BBLocToBoard(chessboard):
    board = [['..' for _ in range(8)] for _ in range(8)]
    for piece, bitboard in chessboard.loc.items():
        #Convert np uint64 to int for bitwise op
        bitboard = int(bitboard)
        for pos in range(64):
            if (bitboard >> pos) & 1: #check if piece at bitboard >> pos (1) ... board pos == name of piece
        
                row = 7 - (pos // 8)
                col = pos % 8
                board[row][col] = piece    
    return board

"""Piece Placement"""
def BoardUpdateVisuals(board):
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece != "..":
                SCREEN.blit(pieces[piece], p.Rect(col * SquareSize, row * SquareSize, SquareSize, SquareSize))
    return 

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
        board = BBLocToBoard(chessboard)
        BoardSquares()
        BoardUpdateVisuals(board)

        for event in p.event.get():
            if event.type == p.QUIT:
                open = False
            elif event.type == p.KEYDOWN:
                if event.key == p.K_ESCAPE:
                    open = False

            if event.type == p.MOUSEBUTTONDOWN:
                x_init, y_init = p.mouse.get_pos()
                if CheckPieceUnderMouse(x_init, y_init, board):
                    held = board[y_init // SquareSize][x_init // SquareSize]

                    run = True
                    while run:
                        p.event.set_grab(True)
                        for event in p.event.get():
                            if event.type == p.MOUSEBUTTONUP:
                                x, y = p.mouse.get_pos()    
                                colDrop, rowDrop = x//SquareSize, y//SquareSize
                                chessboard.Update(held[1], held[0], (ConvertToBitboard(rowDrop,colDrop)))
                                p.event.set_grab(False)                                         
                                run = False
                
        p.display.flip()
    return

"""Convert Row Col to BitBoard Loc"""
def ConvertToBitboard(row, col):
    return np.uint64(1 << ((7-row)*8+col))


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
