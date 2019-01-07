'''
Minesweeper game, going to use the model, view, controller perspective.

'''
import numpy as np
import random as rand
from itertools import product

def main():
    # initialise game
    game = model(5, 10)
    display = viewer(game)
    #

    display.show_mines()




class model():
    def __init__(self, boardsize, number_mines):
        self.board = np.zeros((boardsize, boardsize), dtype=int)
        self.number_mines = number_mines
        self.board, self.mine_locations = self.__populate_board__(
                                                boardsize, 
                                                number_mines
                                                )
        self.map = np.full((boardsize, boardsize), 
                            fill_value='B', 
                            dtype=str)
        
        
        
    def __populate_board__(self, boardsize, number_mines):
        flattened_board = self.board.flatten()
        mine_locations = rand.sample(range(boardsize**2-1), number_mines)
        flattened_board[np.array(mine_locations)] = 1
        board = flattened_board.reshape((boardsize, boardsize))
        return board, mine_locations


class viewer():
    def __init__(self, model):
        self.model = model

    def show_mines(self):
        board_as_string = np.array2string(self.model.board)
        print(board_as_string)
    


    
if __name__ == '__main__':
    main()
