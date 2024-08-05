from enum import IntEnum
import numpy as np


class Piece(IntEnum):
        #Pieces stored as binary with colour + value  col|value -> 00|000
    PAWN = 1
    KNIGHT = 2
    BISHOP = 3 
    ROOK = 4
    QUEEN = 5
    KING = 6 

    WHITE = 16
    BLACK = 8


class ChessBoard():
    def __init__(self):
        self.pieces = {
            "KINGWHITE": np.uint64(0b0000000000000000000000000000000000000000000000000000000000010000),
            "QUEENWHITE": np.uint64(0b0000000000000000000000000000000000000000000000000000000000001000),
            "BISHOPWHITE": np.uint64(0b0000000000000000000000000000000000000000000000000000000000100100),
            "KNIGHTWHITE": np.uint64(0b0000000000000000000000000000000000000000000000000000000001000010),
            "ROOKWHITE": np.uint64(0b0000000000000000000000000000000000000000000000000000000010000001),
            "PAWNWHITE": np.uint64(0b0000000000000000000000000000000000000000000000001111111100000000),
            "PAWNBLACK": np.uint64(0b0000000011111111000000000000000000000000000000000000000000000000),
            "ROOKBLACK": np.uint64(0b1000000100000000000000000000000000000000000000000000000000000000),
            "KNIGHTBLACK": np.uint64(0b0100001000000000000000000000000000000000000000000000000000000000),
            "BISHOPBLACK": np.uint64(0b0010010000000000000000000000000000000000000000000000000000000000),
            "QUEENBLACK": np.uint64(0b0000100000000000000000000000000000000000000000000000000000000000),
            "KINGBLACK": np.uint64(0b0001000000000000000000000000000000000000000000000000000000000000)
            }
        self.BoardReset() 

    def BoardReset(self):
        bitboard = np.uint64(0)
        for piece in self.pieces.values():
            bitboard |= piece
    
    def PieceTypePos(self, piece, color):
        return self.pieces.get((f'{piece.name+color.name}'), np.uint64(0))



##TESTING##
# chess_board = ChessBoard()
# king_white_pos = chess_board.PieceTypePos(Piece.KING, Piece.WHITE)

# print('{:064b}'.format(king_white_pos))




