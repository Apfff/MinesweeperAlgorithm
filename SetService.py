from typing import List
from Set import Set
import math
from Cell import Cell, InfoCell
from Set import Set, ReductionSet
from Map import Map
from SetMask import SetMask, MaskState
from CellState import CellState
from Util import saveMax, saveMin

#Service for creating and reducing Sets

class SetService:
    map: Map
    setMask: SetMask
    sets: List[Set]
    reductionSets: List[ReductionSet]

    def __init__(self, map, setMask):
        self.map = map
        self.setMask = setMask
        self.sets = []
        self.reductionSets = []  

    def createSets(self):
        for y in range(len(self.map.map)):
            for x in range(len(self.map.map[y])):
                set = self.createSetFromPos(Cell(x,y))
                if set is not None: self.sets.append(set)

    def createSetFromPos (self, pos: Cell):
        offset = Cell(pos.x - math.floor(len(self.setMask.mask[0])/2), 
                    pos.y - math.floor(len(self.setMask.mask)/2))
        base = InfoCell(state = self.map.get(pos), cell = pos)
        if not base.state.isNumber():
            return None
        openCells = []
        mines = None
        discoveredMines = 0

        for y in range(len(self.setMask.mask)):
            for x in range(len(self.setMask.mask[y])):
                mappedCell = Cell(offset.x + x, offset.y + y)
                if self.inBoundaries(mappedCell):
                    if self.setMask.get(x,y) == MaskState.BASE:
                        mines = self.map.get(mappedCell).value
                    else:
                        if self.setMask.get(x,y) == MaskState.RELEVANT:
                            if self.map.get(mappedCell) == CellState.UNKNOW:
                                openCells.append(mappedCell)
                            elif self.map.get(mappedCell) == CellState.MINE:
                                discoveredMines += 1
        if not openCells: 
            return None
        return Set(base, openCells, mines, mines-discoveredMines)

    def createReductionSets(self, reductionMap):
        if self.reductionSets: raise Exception("ReductionSets already created")
        for y in range(len(reductionMap)):
            for x in range(len(reductionMap[0])):
                cell = Cell(x,y)
                originSets: List[Set] = reductionMap[y][x]
                if len(originSets) == 0: continue
                reductionSet = ReductionSet(originSets)
                equalReductionSets = self.getExistingReductionSet(reductionSet)
                if equalReductionSets: #checks if reductionSet already exists
                    equalReductionSets.openCells.append(cell) #add Cell to existing reductionSet
                else:
                    [originSet.childSets.append(reductionSet) for originSet in originSets] #add childSets to Sets
                    reductionSet.openCells.append(cell) #add current Cell to reductionSet
                    self.reductionSets.append(reductionSet) #add reductionSet with Cell

    def getExistingReductionSet(self, newReductionSet: ReductionSet):
        for reductionSet in self.reductionSets:
            if reductionSet == newReductionSet:
                return reductionSet
        return None

    def updateReductionSets(self):
        changes = False
        for originSet in self.sets:
            changes = originSet.updateChildSets() or changes
        return changes

    def initializeReductionSetsMinMax(self):
        [rs.initializeMinMax() for rs in self.reductionSets]

    def getResults(self):
        results = {}
        for rs in self.reductionSets:
            key = rs.isObvious()
            if key not in results:
                results[key] = []
            results[key].extend(rs.openCells)
        return results


    def createReductionMap(self):
        reductionMap = [[[] for _ in range(len(self.map.map[0]))] for _ in range(len(self.map.map))]
        for set in self.sets:
            for cell in set.openCells:
                reductionMap[cell.y][cell.x].append(set)
        return reductionMap

    def inBoundaries(self, pos: Cell):
        return pos.x >= 0 and pos.x < self.map.maxPos.x and pos.y >= 0 and pos.y < self.map.maxPos.y