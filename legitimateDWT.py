def LegitimateDWT(startingAmount):
    startingAmount = str(startingAmount)
    try:
        if float(startingAmount) < 0:
            return False
    except:
        return False
    if '.' in startingAmount:
        decimalCount = len(startingAmount[startingAmount.index('.') + 1:])
        if decimalCount > 2:
            return False
    return True