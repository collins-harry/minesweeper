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
    game.toggle_flag((4, 4))
    game.clear_tile((3, 3))
    display.show_mines()
    display.show_board()





class model():
    '''
    ARGUEMENTS
    ---------
    board : board of zeroes, ones where mines are present
    number_mines
    mine_locations : mine locations when board is flattened
    viewable_board : np.array (boardsize, boardsize) filled with B (blank)
    '''
    def __init__(self, boardsize, number_mines):
        self.board = np.zeros((boardsize, boardsize), dtype=int)
        self.number_mines = number_mines
        self.board, self.mine_locations = self._populate_board(
                                                boardsize, 
                                                number_mines
                                                )
        self.viewable_board = np.full((boardsize, boardsize), 
                            fill_value='B', 
                            dtype=str)
        

    def _populate_board(self, boardsize, number_mines):
        flattened_board = self.board.flatten()
        mine_locations = rand.sample(range(boardsize**2), number_mines)
        flattened_board[np.array(mine_locations)] = 1
        board = flattened_board.reshape((boardsize, boardsize))
        return board, mine_locations
    

    def toggle_flag(self, location):
        '''
        PARAMETERS
        ----------
        location: tuple in form (row, column)
        '''
        self.viewable_board[location] = 'F'


    def _check_for_mines(self, location):
        '''
        PARAMETERS
        ----------
        location: tuple in form (row, column)
        '''
        if self.board[location] == 1:
            return True
        else:
            print(f'mine value at location {location} = {self.board[location]}')
            print('^ should be 0')
            return False


    def clear_tile(self, location):
        '''
        PARAMETERS
        ----------
        location: tuple in form (row, column)
        '''
        if self._check_for_mines(location):
            # you lost
            return False
        else:
            self.viewable_board[location] = 'C'
            return True



class viewer():
    def __init__(self, model):
        self.model = model

    def show_mines(self):
        board_as_string = np.array2string(self.model.board)
        print(board_as_string)

    def show_board(self):
        board_as_string = np.array2string(self.model.viewable_board)
        print(board_as_string)
        
    


    
if __name__ == '__main__':
    main()
