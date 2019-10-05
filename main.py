import pieces, board
import yamllib as yl
from uuid import uuid4

class game:

    def __init__(self):
        self.gameId = uuid4()
        self.gBoard = board.board()
        for i in range(3):
            self.gBoard.setPos(0, i, pieces.pawn())
            self.gBoard.setPos(2, i, pieces.pawn())

    def saveGame(self):
        saveState = []
        for i in range(3):
            saveState.append([self.gBoard.getPos(i, 0).name,
                            self.gBoard.getPos(i, 1).name,
                            self.gBoard.getPos(i, 2).name])
        yl.yamllib.yaml_dump("./gamestate.yml", [self.gameId, saveState])

if __name__ == "__main__":
    newGame = game()
    newGame.saveGame()
    print(newGame.gBoard.getBoard())
