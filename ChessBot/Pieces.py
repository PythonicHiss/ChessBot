"""WIP, code currently bugged"""

from enum import IntEnum
import numpy as np


class Piece(IntEnum):
        #Pieces stored as binary with colour + value  col|value -> 00|000
    P = 1
    N = 2
    B = 3 
    R = 4
    Q = 5
    K = 6 

    w = 16
    b = 8



class ChessBoard():
    def __init__(self):
        self.BoardReset()

    def BoardReset(self):
        self.loc = {
            "wK": np.uint64(0b0000000000000000000000000000000000000000000000000000000000010000),
            "wQ": np.uint64(0b0000000000000000000000000000000000000000000000000000000000001000),
            "wB": np.uint64(0b0000000000000000000000000000000000000000000000000000000000100100),
            "wN": np.uint64(0b0000000000000000000000000000000000000000000000000000000001000010),
            "wR": np.uint64(0b0000000000000000000000000000000000000000000000000000000010000001),
            "wP": np.uint64(0b0000000000000000000000000000000000000000000000001111111100000000),
            "bP": np.uint64(0b0000000011111111000000000000000000000000000000000000000000000000),
            "bR": np.uint64(0b1000000100000000000000000000000000000000000000000000000000000000),
            "bN": np.uint64(0b0100001000000000000000000000000000000000000000000000000000000000),
            "bB": np.uint64(0b0010010000000000000000000000000000000000000000000000000000000000),
            "bQ": np.uint64(0b0000100000000000000000000000000000000000000000000000000000000000),
            "bK": np.uint64(0b0001000000000000000000000000000000000000000000000000000000000000)
            }
    
    def PieceTypePos(self, piece, color):
        return self.loc.get((f'{color}{piece}'), np.uint64(0))
    
    def Update(self, piece, color, newPosBitboard):
        key = f'{color}{piece}'
        if key in self.loc: 
            self.loc[key] =  np.uint64(self.loc[key]) ^  (np.uint64(self.loc[key]) | np.uint64(newPosBitboard)) 
        else: 
            raise ValueError(f"Invalid piece/color")
        


