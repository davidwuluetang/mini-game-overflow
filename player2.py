from game_tree import GameTree

class PlayerTwo:

    def __init__(self, name = "P2 Bot"):
        self.name = name

    def get_name(self):
        return self.name

    def get_play(self, board, AI_level):
        tree = GameTree(board, -1, AI_level[0], AI_level[1])
        (row,col) = tree.get_move(AI_level[0])
        return (row,col)