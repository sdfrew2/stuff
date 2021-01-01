
from collections import deque
import sys

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
    deck1 = parseDeck(fh)
    deck2 = parseDeck(fh)

state = (deque(deck1), deque(deck2))


class Game:
    def __init__(me, deck1, deck2):
        me.deck1 = deque(deck1)
        me.deck2 = deque(deck2)

    def winner(me):
        if len(me.deck1) == 0:
            return 1
        if len(me.deck2) == 0:
            return 0
        return None

    def run(me):
        while me.winner() == None:
            me.runTurn()
        return me.score([me.deck1, me.deck2][me.winner()])

    def score(me, deck):
        deck = list(deck)
        result = 0
        print(deck)
        for i in range(len(deck)):
            result += (1+i) * deck[len(deck) - 1 - i]
        return result

    def runTurn(me):
        (deck1, deck2) = (me.deck1, me.deck2)
        x1 = deck1.popleft()
        x2 = deck2.popleft()
        if x1 > x2:
            deck1.append(x1)
            deck1.append(x2)
        else:
            deck2.append(x2)
            deck2.append(x1)

def main():
    game = Game(deck1, deck2)
    print(game.run())
    print(game.deck1, game.deck2)

main()
