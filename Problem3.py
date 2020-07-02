def secondLowest(mylist: list) -> int:
    """
    param mylist: input list
    return: int
    I will reuse some parts of the second problem
    """

    # variable initialisation
    results = []
    temp_char = mylist[0]
    counter = 0

    # simply count chars using temp. values
    for x in range(0, len(mylist)):
        if mylist[x] == temp_char:
            counter += 1
        else:
            results.append([temp_char, counter])
            temp_char = mylist[x]
            counter = 1

    # add the last item into results list
    results.append([temp_char, counter])

    # used built-in "sorted" function to sort according to first item
    results = sorted(results)

    if results[0][1] == results[1][1]:
        """
        if lowest and second-lowest values have same frequency,
        max(results, key=lambda x: x[1]) statement will give
        the first lowest frequent sub-list
        if I remove this sub-list and when I call the same max statement,
        it will give me the second-lowest frequency.
        """
        results.remove(max(results, key=lambda x: x[1]))
        return max(results, key=lambda x: x[1])[0]
    else:
        return max(results, key=lambda x: x[1])[0]
