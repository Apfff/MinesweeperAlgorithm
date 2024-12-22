from Set import Set
from Map import Map
from Cell import Cell
from SetMask import *
from SetService import *

#inputs 

inputMap = [
        ['o','o','o'],
        ['2','4','o'],
        ['x','2','o']
    ]

setMask = [
        [MaskState.RELEVANT,MaskState.RELEVANT, MaskState.RELEVANT],
        [MaskState.RELEVANT,MaskState.BASE, MaskState.RELEVANT],
        [MaskState.RELEVANT,MaskState.RELEVANT, MaskState.RELEVANT],
    ]

def printMap(map):
    map_str = ""
    for row in map:
        map_str += " ".join([str(cell) for cell in row]) + "\n"
    print(map_str)

def main():
    ss = SetService(Map(inputMap), SetMask(setMask))
    print("Map:")
    print(ss.map)
    ss.createSets()
    print("Origin Sets:")
    [print(s) for s in ss.sets]
    print()
    print("Reduction Sets:")
    ss.createReductionSets(ss.createReductionMap())
    [print(rs) for rs in ss.reductionSets]
    print()
    print("Origin Sets Child Sets:")
    [print(s) or [print(f"   {cs}") for cs in s.childSets] for s in ss.sets]
    print()
    print("Initial Min Max Reduction Sets:")
    ss.initializeReductionSetsMinMax()
    [print(rs) for rs in ss.reductionSets]
    print()
    print("Update #1:")
    print(f"Changes -> {ss.updateReductionSets()}")
    [print(rs) for rs in ss.reductionSets]
    print()
    print("Results #1:")
    [print(f"{rs.isObvious()} <- {rs}") for rs in ss.reductionSets]
    print()
    print("Update #2:")
    print(f"Changes -> {ss.updateReductionSets()}")
    [print(rs) for rs in ss.reductionSets]
    print()
    print("Results #2:")
    [print(f"{rs.isObvious()} <- {rs}") for rs in ss.reductionSets]
    print()
    print("Update #3:")
    print(f"Changes -> {ss.updateReductionSets()}")
    [print(rs) for rs in ss.reductionSets]
    print()
    print("Results #3:")
    [print(f"{rs.isObvious()} <- {rs}") for rs in ss.reductionSets]
    print()
    print("Update #4:")
    print(f"Changes -> {ss.updateReductionSets()}")
    [print(rs) for rs in ss.reductionSets]
    print()
    print("Results #4:")
    [print(f"{rs.isObvious()} <- {rs}") for rs in ss.reductionSets]


if __name__ == "__main__":
    main()