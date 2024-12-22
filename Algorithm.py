from SetService import SetService
from Map import Map
from SetMask import SetMask

def runAlgorithm(inputMap: Map, setMask: SetMask):
    #initialize SetService
    ss = SetService(Map(inputMap), SetMask(setMask))
    #create origin Sets
    ss.createSets()
    #create reduction Sets & add child Sets to origin Sets
    ss.createReductionSets(ss.createReductionMap())
    #initialize minM and maxM values for reduction Sets
    ss.initializeReductionSetsMinMax()
    