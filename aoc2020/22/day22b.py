
from collections import deque
from itertools import islice
import sys
from functools import lru_cache
def parseDeck(fh):
    fh.readline()
    deck = [] 
    for line in fh:
        if line == "\n":
            break
        line = line.strip()
        deck.append(int(line))
    return deck

with open(sys.argv[1]) as fh:
    deck1 = tuple(parseDeck(fh))
    deck2 = tuple(parseDeck(fh))

def scoreDeck(deck):
    deck = list(deck)
    result = 0
    for i in range(len(deck)):
        result += (1+i) * deck[len(deck) - 1 - i]
    return result

#@lru_cache(maxsize = None)
def runGame(d1, d2):
    deck1 = deque(d1)
    deck2 = deque(d2)
    visited = set()
    while True:
        state = (tuple(deck1), tuple(deck2))
        if state in visited:
            return (0, scoreDeck(deck1))
        visited.add(state)
        if len(deck1) == 0:
            return (1, scoreDeck(deck2))
        if len(deck2) == 0:
            return (0, scoreDeck(deck1))
        x1 = deck1.popleft()
        x2 = deck2.popleft()
        if x1 <= len(deck1) and x2 <= len(deck2):
            subgame = runGame(tuple(islice(deck1, x1)), tuple(islice(deck2, x2)))
            (winner, score) = subgame
            if winner == 0:
                deck1.append(x1)
                deck1.append(x2)
            else:
                deck2.append(x2)
                deck2.append(x1)
        else:
            if x1 > x2:
                deck1.append(x1)
                deck1.append(x2)
            else:
                deck2.append(x2)
                deck2.append(x1)

    



def main():
    (winner, score) = runGame(deck1, deck2)
    print(winner, score)

main()
