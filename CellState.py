from enum import Enum

class CellState(Enum):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NOINFO = "?"
    MINE = "x"
    UNKNOW = "o"

    def isMine(self):
        return self == CellState.MINE
    
    def isNumber(self):
        return self.value in range(0,9)
    
    def isUnknown(self):
        return self == CellState.UNKNOW
    
    def isNoInfo(self):
        return self == CellState.NOINFO
    
    @classmethod
    def getEnum(cls, value):
        for enum in cls:
            if enum.value == value:
                return enum
        raise ValueError(f"No matching enum found for {value}")
    
