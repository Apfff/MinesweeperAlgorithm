from typing import List
from Cell import Cell
from CellState import CellState

class Map():
    informalMap: List[List[str]]
    map: List[List[CellState]]
    minPos: Cell
    maxPos: Cell

    def __init__(self, informalMap: List[List[str]]):
        self.informalMap = informalMap
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
    
    def get(self, pos: Cell):
        return self.map[pos.y][pos.x]