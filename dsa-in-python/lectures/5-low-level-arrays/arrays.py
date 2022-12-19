def drawLine(tickLength, tickLabel=""): 
    """Draw one line with given tick length (followed by optional label)"""
    line = "-" * tickLength
    if tickLabel: 
        line += " " + tickLabel
    print(line)

def drawInterval(centerLength): 
    """Draw tick interval based upon a central tick length."""
    if centerLength > 0:                # stop when legnth drops to 0 
        drawInterval(centerLength - 1)  # recursively draw top ticks 
        drawLine(centerLength)          # draw center tick
        drawInterval(centerLength - 1)  # recursively draw bottom ticks]

def drawRuler(numInches, majorLength): 
    """Draw English ruler with given number of inches, major tick length."""
    drawLine(majorLength, '0')          # draw inch 0 line
    for j in range(1, 1 + numInches): 
        drawInterval(majorLength - 1)   # draw interior ticks for inch
        drawLine(majorLength, str(j))   # draw inch j line and label