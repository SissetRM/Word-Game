def calculateHandlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string int)
    returns: integer
    """
    return sum(hand.values())


print(calculateHandlen({'a': 1, 'b': 1}))
print(calculateHandlen({'a': 1, 'c': 0, 'b': 1}))
