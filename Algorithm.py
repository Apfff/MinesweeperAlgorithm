from typing import List, Dict
from SetService import SetService
from Map import Map
from SetMask import SetMask
from Set import ReductionSet
from ObviousState import ObviousState

def runAlgorithm(inputMap: Map, minesCount: int, setMask: SetMask):
    #create map
    map = Map(inputMap, minesCount)
    #check if map is obvious
    if map.isObvious() != ObviousState.NOT_OBVIOUS:
        outputNextMove(map.getObviousResults())
        return
    #initialize SetService
    ss = SetService(map, SetMask(setMask))
    #create origin Sets
    ss.createSets()
    #create reduction Sets & add child Sets to origin Sets
    ss.createReductionSets(ss.createReductionMap())
    #initialize minM and maxM values for reduction Sets
    ss.initializeReductionSetsMinMax()
    #update Reduction Sets until there is no change
    while ss.updateReductionSets(): pass
    outputNextMove(ss.getResults())

def outputNextMove(results: Dict):
    if set(results.keys()) == {ObviousState.NOT_OBVIOUS}:
        raise Exception("No valid move could be determined")
    print("Results:")
    print(f"Numbers: {results.get(ObviousState.ALL_NUMBERS)}")
    print(f"Mines: {results.get(ObviousState.ALL_MINES)}")


    
