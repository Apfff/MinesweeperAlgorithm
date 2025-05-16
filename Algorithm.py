from typing import Dict
from termcolor import colored
from SetService import SetService
from Map import Map
from SetMask import SetMask
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
    print("origin sets pre update:")
    [print("    ",os) for os in ss.sets]
    print("Reduction sets pre update:")
    [print("    ",rs) for rs in ss.reductionSets]
    #update Reduction Sets until there is no change
    print()
    i = 1
    print(colored(f"--- Update Iteration {i} ---\n", "yellow"))
    while ss.updateReductionSets():
        #return #TODO remove
        i += 1
        print(colored(f"--- Update Iteration {i} ---\n", "yellow"))
        pass
    outputNextMove(ss.getResults())

def outputNextMove(results: Dict):
    if set(results.keys()) == {ObviousState.NOT_OBVIOUS}:
        raise Exception("No valid move could be determined")
    print("Results:")
    print(f"Numbers: {results.get(ObviousState.ALL_NUMBERS)}")
    print(f"Mines: {results.get(ObviousState.ALL_MINES)}")


    
