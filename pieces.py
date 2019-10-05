class piece:

    def __init__(self, name):
        self.name = name

    def getType(self):
        return self.name

class pawn(piece):

    def __init__(self):
        piece.__init__(self, "pawn")
