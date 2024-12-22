from typing import List
from Cell import *

class Set:
    base: InfoCell
    openCells: List[Cell]
    mines: int
    minesLeft: int
    childSets: List['ReductionSet']

    def __init__(self, base, openCells, mines, minesLeft):
        self.base = base
        self.openCells = openCells
        self.mines = mines
        self.minesLeft = minesLeft
        self.childSets = []
    
    def __str__(self):
        openCells_str = ', '.join(map(str, self.openCells))
        return f"Set(base={self.base}, mines [{self.mines-self.minesLeft}/{self.mines}], openCells=[{openCells_str}])"
    
    def __repr__(self):
        return self.__str__()
    

    def updateChildSets(self):
        changes = False
        absLowerBound = self.minesLeft - sum([cs.maxM for cs in self.childSets])
        absUpperBound = self.minesLeft - sum([cs.minM for cs in self.childSets])
        
        print(f"Initial absLowerBound: {absLowerBound}, absUpperBound: {absUpperBound}")
        
        for childSet in self.childSets:
            oldMinM = childSet.minM
            oldMaxM = childSet.maxM
            
            print(f"Before update - childSet: {childSet}, oldMinM: {oldMinM}, oldMaxM: {oldMaxM}")
            
            childSet.minM = max(absLowerBound + oldMaxM, oldMinM)
            childSet.maxM = min(absUpperBound + oldMinM, oldMaxM)
            
            print(f"After update - childSet: {childSet}, newMinM: {childSet.minM}, newMaxM: {childSet.maxM}")
            
            changes = (childSet.minM > oldMinM or childSet.maxM < oldMaxM) or changes
        
        print(f"Changes: {changes}")
        return changes

class ReductionSet:
    originSets: List[Set]
    openCells: List[Cell]
    minM: int
    maxM: int


    def __init__(self, originSets):
        self.originSets = originSets
        self.openCells = []
        self.minM = None
        self.maxM = None

    def __eq__(self, other):
        if isinstance(other, ReductionSet):
            return self.originSets == other.originSets
        return False
    
    def __str__(self):
        openCells_str = ', '.join(map(str, self.openCells))
        return f"ReductionSet({len(self.originSets)} originSets, openCells=[{openCells_str}], minM={self.minM}, maxM={self.maxM})"

    def __repr__(self):
        return self.__str__()
    
    def initializeMinMax(self):
        self.maxM = min(min([os.minesLeft for os in self.originSets]), len(self.openCells))
        self.minM = 0

    def isObvious(self):
        if(self.maxM == 0):
            return 1 #all openCells are numbers
        if(self.minM == len(self.openCells)):
            return 2 #all openCells are mines
        return 0 #not obvious
