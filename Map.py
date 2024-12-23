from typing import List
from Cell import Cell
from CellState import CellState
from ObviousState import ObviousState

class Map():
    informalMap: List[List[str]]
    map: List[List[CellState]]
    minesCount: int
    minPos: Cell
    maxPos: Cell

    def __init__(self, informalMap: List[List[str]], minesCount):
        self.informalMap = informalMap
        self.minesCount = minesCount
        self.map = Map.generateMap(informalMap)
        self.minPos = Cell(0,0)
        self.maxPos = Cell(len(self.map[0]), len(self.map))
    
    def __repr__(self):
        map_str = ""
        for row in self.map:
            map_str += " ".join([str(cell.value) for cell in row]) + "\n"
        return map_str

    def generateMap(inputMap):
        cleansedMap = Map.cleanseMap(inputMap)
        return [[(CellState.getEnum(cell)) for cell in row] for row in cleansedMap]

    def cleanseMap(inputMap):
        return [[(int(cell) if cell.isdigit() else cell) for cell in row] for row in inputMap]
    
    def isObvious(self):
        if sum([cell.isUnknown() for row in self.map for cell in row]) == self.minesCount:
            return ObviousState.ALL_MINES
        if self.minesCount == 0:
            return ObviousState.ALL_NUMBERS
        return ObviousState.NOT_OBVIOUS

    def getAllUnknownCells(self):
        return 
    
    def getObviousResults(self):
        return {self.isObvious(), 
                [cell for row in self.map for cell in row if cell.isUnknown()]}

    def get(self, pos: Cell):
        return self.map[pos.y][pos.x]