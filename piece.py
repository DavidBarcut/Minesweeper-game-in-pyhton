class Piece():
    def __init__(self, hasBomb):
        self.hasBomb = hasBomb
        self.clicked = False
        self.flagged = False
        
    def getHasBomb(self):
        return self.hasBomb
    
    def getClicked(self):
        return self.clicked
    
    def getFlagged(self):
        return self.flagged
    
    def setNeighbors(self, neighbors):
        self.neighbors = neighbors
        self.setNumAround()
    
    def setNumAround(self):
        self.numAround = 0
        for piece in self.neighbors:
            if piece.getHasBomb():
                self.numAround += 1

    def getNumAround(self):
        return self.numAround
    
    def toggleflag(self):
        self.flagged = not self.flagged

    def click(self):
        self.clicked = True