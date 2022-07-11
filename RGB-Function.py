#This function returns the color for a given position
#i can be the time, a frame, or a position inside a canvas
def getColorAt(i):
    if i <= 255:
        return 255, 0, i
    elif i <= 510:
        return 510-i, 0, 255
    elif i <= 765:
        return 0, i-510, 255
    elif i <= 1020:
        return 0, 255, 1020-i
    elif i <= 1275:
        return i-1020, 255, 0
    elif i <= 1530:
        return 255, 1530-i, 0
