def findTheLongest(inputStr: str) -> tuple:
    """
    param inputStr: input string
    return: tuple
    """
    # convert string into lowercase
    inputStr = inputStr.lower()

    # convert str inputStr to a list
    inputList = list(inputStr)

    # variable initialisation
    results = []
    temp_char = inputList[0]
    counter = 0

    # simply count chars using temp. values
    for x in range(0, len(inputList)):
        if inputList[x] == temp_char:
            counter += 1
        else:
            results.append([temp_char, counter])
            temp_char = inputList[x]
            counter = 1

    # add the last item into results list
    results.append([temp_char, counter])

    # used built-in "sorted" function to sort according to first item
    results = sorted(results)

    """
    returns the tuple that that has the max value on the second order
    of sub-list
    """
    return tuple(max(results, key=lambda x: x[1]))
