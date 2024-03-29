from piece import Piece
import random

class Board():
    def __init__(self, size, prob):
        self.size = size 
        self.prob = prob
        self.setBoard()

    def setBoard(self):
        self.board = []
        for row in range(self.size[0]):
            row =[]
            for col in range(self.size[1]):
                hasBomb = random.random() < self.prob
                piece = Piece(hasBomb)
                row.append(piece)
            self.board.append(row)
        self.setNeighbors()

    def setNeighbors(self):
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                piece = self.getPiece((row, col))
                neighbours = self.getListOfNeighbors((row, col))
                piece.setNeighbors(neighbours)

    def getListOfNeighbors(self, index):
        neighbours = []
        for row in range(index[0]-1, index[0]+2):
            for col in range(index[1]-1, index[1]+2):
                outOfBounds = row < 0 or row >= self.size[0] or col < 0 or col >= self.size[1]
                same = row == index[0] and col == index[1]
                if outOfBounds or same:
                    continue
                neighbours.append(self.getPiece((row, col)))
        return neighbours
                
       

    def getSize(self):
        return self.size

    def getPiece(self, index):
        return self.board[index[0]][index[1]]
    
    def handleClick(self, piece, flag):
        if (piece.getClicked() or (not flag and piece.getFlagged())):
            return
        if (flag):  
            piece.toggleflag()
            return
        piece.click

