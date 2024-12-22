from enum import Enum
from typing import List
from Cell import Cell

class MaskState(Enum):
    IGNORE = 0
    RELEVANT = 1
    BASE = 2

class SetMask():
    mask: List[List[MaskState]]

    def __init__(self, mask):
        self.mask = mask

    def get(self, x, y):
        return self.mask[y][x]

