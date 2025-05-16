from typing import List, Dict
import copy
from Cell import *
from ObviousState  import ObviousState
from termcolor import colored

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
        print(colored(f"## updateChild -> {self} ##", "green"))
        changes = False
        absLowerBound = self.getAbsoluteLowerBound()
        absUpperBound = self.minesLeft - sum([cs.minM for cs in self.childSets])     
        for childSet in self.childSets:
            oldMinM = childSet.minM
            oldMaxM = childSet.maxM
            print(colored(childSet, "blue"))
            print(f"    oldMinM: {oldMinM} | oldMaxM: {oldMaxM}")
            print(f"    absLowerBound: {absLowerBound} | absUpperBound: {absUpperBound}")
            childSet.minM = min(max(absLowerBound + oldMaxM, oldMinM), self.minesLeft)
            childSet.maxM = max(min(absUpperBound + oldMinM, oldMaxM), 0)
            changes = (childSet.minM > oldMinM or childSet.maxM < oldMaxM) or changes
            print(colored(f"{childSet} \n new minM = {childSet.minM}, new maxM = {childSet.maxM}", "white"))
        return changes

    
    def getAbsoluteLowerBound(self):
        originDict: Dict['Set', List['ReductionSet']] = {}
        for childSet in self.childSets:
            for originSet in childSet.originSets:
                if originSet not in originDict:
                    originDict[originSet] = []
                originDict[originSet].append(childSet)
        print(colored("originDict:", "light_green"))
        print("".join([f"\n{key}:\n" + "\n".join([f"   {cs}" for cs in value]) for key, value in originDict.items()]))
        self.cleanseOriginDict(originDict)
        print(colored("cleansed originDict:", "light_blue"))
        print("".join([f"{key}:\n" + "\n".join([f"   {cs}" for cs in value]) for key, value in originDict.items()]))
        absLowerBound = self.minesLeft
        for os in originDict:
            absLowerBound -= min(sum([rs.maxM for rs in originDict.get(os)]), os.minesLeft) #pick individual max's or over os max (merged rs's)
        return absLowerBound
        
    def cleanseOriginDict(self, originDict: Dict['Set', List['ReductionSet']]):
        impactValueDict: Dict['Set', float] = {} 
        for os in originDict:
            if os == self: continue
            impactValueDict[os] = sum([rs.maxM for rs in originDict.get(os)])/os.minesLeft
        for cs in self.childSets:
            if len(cs.originSets) < 2: continue #reductionSet doesnt have multiple originSets (besides self)
            originSetsCopy = copy.copy(cs.originSets)
            originSetsCopy.remove(self) #remove self so it doesnt influence biggestImpactOrigin
            biggestImpactOrigin = max(originSetsCopy, key=impactValueDict.get)
            originSetsCopy.remove(biggestImpactOrigin)
            originSetsCopy.append(self) #put it back for removing reductionSets
            for os in originSetsCopy: originDict.get(os).remove(cs) #remove rs for all os which are not biggestImpactOrigin


                
        print(colored("impact value dict:", "light_blue"))
        [print(f"{key} -> {impactValueDict.get(key)}") for key in impactValueDict]


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
    
    def initializeMax(self):
        restrictiveOrigin = min(self.originSets, key=lambda originSet: originSet.minesLeft)
        self.maxM = min(restrictiveOrigin.minesLeft, len(self.openCells))

    def initializeMin(self):
        self.minM = 0

    def isObvious(self):
        if(self.maxM == 0):
            return ObviousState.ALL_NUMBERS 
        if(self.minM == len(self.openCells)):
            return ObviousState.ALL_MINES 
        return ObviousState.NOT_OBVIOUS 
