'''
Minesweeper game, going to use the model, view, controller perspective.

'''
import numpy as np
import random as rand
import tkinter as tk
from itertools import product
import time

class Model():
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

    def _check_for_mines(self, location):
        '''
        PARAMETERS
        ----------
        location: tuple in form (row, column)
        '''
        if self.board[location] == 1:
            return True
        else:
            return False

    def toggle_flag(self, location):
        '''
        PARAMETERS
        ----------
        location: tuple in form (row, column)
        '''
        self.viewable_board[location] = 'F'

    def clear_tile(self, location):
        '''
        PARAMETERS
        ----------
        location: tuple in form (row, column)
        '''
        if self._check_for_mines(location):
            # you lost
            self.end_game()
            return False
        else:
            self.viewable_board[location] = 'C'
            return True

    def end_game(self):
        raise Exception('YOU LOST')

class GUI_Viewer():
    def __init__(self, model):
        self.model = model
        self.viewable_board = self.model.viewable_board
        self.root = tk.Tk()
        # self.root.mainloop()
        self.root.update_idletasks()
        self.root.update()
        time.sleep(1)

    def draw_board(self):
        for i, row in enumerate(self.viewable_board):
            for j, value in enumerate(row):
                tile = tk.Label(self.root, text=value, bg='grey')
                tile.grid(row=i, column=j)
        self.root.update_idletasks()
        self.root.update()
        time.sleep(1)


    def show_mines(self):
        board_as_string = np.array2string(self.model.board)
        print(board_as_string)

    def show_board(self):
        board_as_string = np.array2string(self.model.viewable_board)
        print(board_as_string)
  

class Viewer():
    def __init__(self, model):
        self.model = model

    def show_mines(self):
        board_as_string = np.array2string(self.model.board)
        print(board_as_string)

    def show_board(self):
        board_as_string = np.array2string(self.model.viewable_board)
        print(board_as_string)
        
    


    
if __name__ == '__main__':

    # initialise game
    game = Model(5, 10)
    display = Viewer(game)
    gui_display = GUI_Viewer(game)
    #
    game.toggle_flag((4, 4))
    game.clear_tile((3, 3))
    display.show_mines()
    display.show_board()
    gui_display.show_mines()
    gui_display.show_board()
    gui_display.draw_board()
    game.toggle_flag((3, 4))
    game.clear_tile((2, 3))
    gui_display.draw_board()
    game.end_game()


ain()
