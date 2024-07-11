def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    #>>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=" ")  # print all on the same line
    print()  # print an empty line


def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    newHand = hand.copy()
    for i in range(sum(hand.values())):
        try:
            if word[i] in newHand:
                newHand[word[i]] = newHand[word[i]]-1
        except IndexError:
            break
    return newHand


Hand = {'a': 1, 'x': 2, 'l': 3, 'e': 1}
displayHand(Hand)
Hand = updateHand(Hand, 'axe')
displayHand(Hand)
Test = updateHand({'h': 1, 'e': 1, 'l': 2, 'o': 1}, 'hello')
print(Test)
