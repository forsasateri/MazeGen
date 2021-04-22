

class Cell:

    @property
    def row(self):
        return self._row

    @property
    def column(self):
        return self._column

    @property
    def links(self):
        return list(self._links.keys())

    @property
    def neighbours(self):
        nList = []
        if self.north:
            nList.append(self.north)
        if self.south:
            nList.append(self.south)
        if self.east:
            nList.append(self.east)
        if self.west:
            nList.append(self.west)
        return nList

    @property
    def data(self):
        return self._data

    def __init__(self, row, column):

        if row is None or row < 0:
            raise ValueError("Row must be a positive integer")
        if column is None or column < 0:
            raise ValueError("Column must be a positive integer")

        self._column = column
        self._links = {}
        self._data = {}

        self.north = None
        self.south = None
        self.west = None
        self.east = None
    
    def link(self, cell, bidi = True):
        self._links[cell] = True
        if bidi:
            cell.link(self, False)
        return self

    def unlink(self, cell, bidi = True):
        del self._links[cell]
        if bidi:
            cell.unlink(self, False)
        return self

    def linked(self, cell):
        return cell in self._links