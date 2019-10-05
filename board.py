import numpy as np

class tile:

    def __init__(self):
        self.name = "tile"

    def getType(self):
        return self.name

class board:

    def __init__(self, sizeX=3, sizeY=3):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.board = np.ndarray([sizeX, sizeY], dtype=object)
        for cx in range(self.sizeX):
            for cy in range(self.sizeY):
                self.board[cx, cy] = tile

    def getSizeX(self):
        return self.sizeX

    def getSizeY(self):
        return self.sizeY

    def getBoard(self):
        return self.board

    def setPos(self, posX, posY, obj):
        self.board[posX, posY] = obj

    def getPos(self, posX, posY):
        return self.board[posX, posY]
