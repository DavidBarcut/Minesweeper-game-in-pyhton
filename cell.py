import random 
from re import X
from tkinter import button, Label
import sys
import ctypes 

def surround_cells(self):
    surround_cells = [
        self.get_cell_by_axis(self.x -1, self.y - 1),
        self.get_cell_by_axis(self.x -1, self.y),
        self.get_cell_by_axis(self.x -1, self.y + 1),
        self.get_cell_by_axis(self.x, self.y - 1),
        self.get_cell_by_axis(self.x, self.y + 1),
        self.get_cell_by_axis(self.x +1, self.y - 1),
        self.get_cell_by_axis(self.x +1, self.y),
        self.get_cell_by_axis(self.x +1, self.y + 1)
    ]
    surround_cells = [cell for cell in surround_cells if cell]
    print(surround_cells)
    return surround_cells

def mines_len(self):
    i = 0
    for cell in self.surround_cells:
        if cell.is_mine:
            i += 1
    return i