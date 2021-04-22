from Cell import Cell
import numpy as np

class Grid:

    @property
    def rows(self):
        return self._rows

    @property
    def columns(self):
        return self._columns

    @property
    def size(self):
        return self.rows * self.columns

    def __init__(self, rows, columns):
        self._rows = rows
        self._columns = columns

        self._grid = self.prepareGrid()
        self.configureCells()

    def prepareGrid(self):
        return [[Cell(row, column) for column in range (self.columns)] for row in range(self.rows)]

    def configureCells(self):
        for cell in self.cellGen():
            row = cell.row
            col = cell.column

            cell.north = self[row - 1, col]
            cell.south = self[row + 1, col]
            cell.west = self[row, col - 1]
            cell.east = self[row, col + 1]

    def cellGen(self):
        for row in range(self.rows):
            temp = self._grid[row]
            for cell in temp:
                yield cell

    def __getitem__(self, key):
        #if is_key(key):
            row, column = key
            if row < 0 or row > self.rows - 1:
                return None
            if column < 0 or column > self.columns - 1:
                return None
            return self._grid[row][column]


def is_key(key):
    """
    Runtime check for key correctness
    """
    return type(key) == tuple and len(key) == 2 and not any(type(value) != int for value in key)


