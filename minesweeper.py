from Set import Set
from Map import Map
from Cell import Cell
from SetMask import *
from SetService import *
from Algorithm import *

#inputs 

inputMap = [
        ['x','o','o','1','o'],
        ['x','4','3','3','o'],
        ['3','x','3','x','o'],
        ['x','3','3','x','x'],
        ['x','2','1','?','2']
    ]

minesCount = 10

setMask = [
        [MaskState.RELEVANT,MaskState.RELEVANT, MaskState.RELEVANT],
        [MaskState.RELEVANT,MaskState.BASE, MaskState.RELEVANT],
        [MaskState.RELEVANT,MaskState.RELEVANT, MaskState.RELEVANT],
    ]

def main():
    runAlgorithm(inputMap, minesCount, setMask)


if __name__ == "__main__":
    main()