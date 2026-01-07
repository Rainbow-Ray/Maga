import math


def countHypotenyse(a, b):
    return math.sqrt(a ** 2 + b ** 2)


def countCat(a, c):
    return math.sqrt(c ** 2 - a ** 2)


class StitchCoords:
    bottomStart: [float, float, float] = [0, 0, 0]
    bottomEnd: [float, float, float] = [0, 0, 0]
    topStart: [float, float, float] = [0, 0, 0]
    topEnd: [float, float, float] = [0, 0, 0]

    def __init__(self):


    def countCoords(self, prRowSticthCoords, prStitchCoords, width, height):
        bottomStart = prRowSticthCoords.topStart
        bottomEnd = prRowSticthCoords.topEnd
        topStart = bottomStart + height
        topEnd = bottomEnd + height
        return [bottomStart, bottomEnd, topStart, topEnd]

    def countIncCoords(self, prRowSticthCoords, prStitchCoords,width, height, countOfSt):

        wPrev = (prRowSticthCoords.topStart - prRowSticthCoords.topEnd)

        widthInc = width / countOfSt

        wOut = countCat(widthInc,width)


        bX = wPrev[0] / countOfSt
        bY =wPrev[1] / countOfSt

        bottomStart = prRowSticthCoords.topStart
        bottomEnd =bottomStart + (bX, bY)



    # bottomStartY: float = 0
    # topStartX: float = 0
    # topStartY: float = 0
    #
    # bottomEndX: float = 0
    # bottomEndY: float = 0
    # topEndX: float = 0
    # topEndY: float = 0


class Stitch:
    name : str = "stitch"
    abbr: str = "s"
    symbol: str = "0"
    width: float = 1
    height: float = 1
    coords: StitchCoords
    number: int = 1


class Row:
    stitches: [Stitch] = []
    number: int = 0


class Thing:
    rows: [Row] = []
    lastRow: Row
    workingRow: Row

