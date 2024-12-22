def saveMin(v1, v2):
    if v1 is not int and v2 is not int:
        raise Exception("Both values are none Integer")
    if v1 is not int: return v2
    if v2 is not int: return v1
    return min(v1, v2)

def saveMax(v1, v2):
    if v1 is not int and v2 is not int:
        raise Exception("Both values are none Integer")
    if v1 is not int: return v2
    if v2 is not int: return v1
    return max(v1, v2)