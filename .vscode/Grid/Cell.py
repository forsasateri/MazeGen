class cell:

    def __init__(self, r, c):
        self.row = r
        self.column = c
        self.links = {}
    
    def link(self, cell, bidi = True):
        self.links[cell] = True
        if bidi:
            cell.link(self, False)

    def unlink(self, cell, bidi = True):
        del self.links[cell]
        if bidi:
            cell.unlink(self, False)

    def links(self):
        # Problem
        return self.links.keys()

    def linked(self, cell):
        return cell in self.links

    def neighbours(self):
        self.list = []
        if north:
            self.list.append(north)
        if south:
            self.list.append(south)
        if east:
            self.list.append(east)
        if west:
            self.list.append(west)
        return self.list