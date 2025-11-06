from enum import Enum
import random

class Color(Enum):
    K = "Kreuz ♣"
    P = "Pik ♠"
    H = "Herz ♥"
    D = "Karo ♦"

class Number(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

class Combinations(Enum):
    HIGHCARD = [[1,0,0,0,0],0]
    PAIR = [[1,1,0,0,0],1]
    TWOPAIR = [[1,1,2,2,0],2]
    THREEOFAKIND = [[1,1,1,0,0],3]
    STRAIGHT = [[1,2,3,4,5],4]
    FLUSH = [[2,2,2,2,2],5]
    FULLHOUSE = [[1,1,1,2,2],6]
    FOUROFAKIND = [[1,1,1,1,0],7]
    STRAIGHTFLUSH = [[1,2,3,4,5],8]

class Card():
    def __init__(self, color: Color, number: Number):
        self.color = color
        self.number = number

    def __str__(self):
        # show enum name and value for Number, and the symbol/text for Color
        return str(self.number.value)+" "+str(self.color.value)
    
def dealhand(cards):
    hand = [random.sample(cards,5)] # 5 cards to the player
    hand = sorted(hand[0], key=lambda x: x.number.value) # sort by the value of the number enum
    return hand
    

def main ():
    cards = []
    for color in Color: # Generate a list of all cards
        for number in Number:
            cards.append(Card(color, number))




if __name__ == "__main__":
    main()
    
