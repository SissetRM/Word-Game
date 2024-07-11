WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList


def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    deltHand = hand.copy()
    if word in wordList:
        for i in range(len(word)):
            if word[i] not in deltHand.keys():
                return False
            elif deltHand.__getitem__(word[i]) <= 0:
                return False
            else:
                deltHand[word[i]] -= 1

        return True
    else:
        return False


wordlist = loadWords()
Hand = {'g': 1, 'o': 2, 'd': 1, 's': 0}
GoodWord = 'good'
BadWord = 'godo'
BadInput = 'what'
NoLetter = 'dogs'
rapture = 'rapture'
raptureHand = {'e': 1, 'u': 1, 'p': 2, 'r': 1, 't': 1, 'a': 3}
print(isValidWord(GoodWord, Hand, wordlist))  # expect True
print(isValidWord(BadWord, Hand, wordlist))  # expect False because not real word.
print(isValidWord(BadInput, Hand, wordlist))  # expect False because letter not in hand.
print(isValidWord(NoLetter, Hand, wordlist))  # expect False because no s left.
print(isValidWord(rapture, raptureHand, wordlist))  # expect False because only one r.
