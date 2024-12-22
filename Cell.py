from CellState import CellState

class Cell: 
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def __repr__(self):
        return self.__str__()

class InfoCell(Cell):
    state: CellState

    def __init__(self, state: CellState, x: int = None, y: int = None, cell: Cell = None):
        if cell is not None:
            self.x = cell.x
            self.y = cell.y
        else:
            super().__init__(x, y)
        self.state = state

    def __str__(self):
        return f"([{self.state}] {self.x},{self.y})"