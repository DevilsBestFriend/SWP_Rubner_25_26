from enum import Enum

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

class Card():
    def __init__(self, color: Color, number: Number):
        self.color = color
        self.number = number

    def __str__(self):
        # show enum name and value for Number, and the symbol/text for Color
        return f"{self.number.name}({self.number.value}) {self.color.value}"

def main ():
    cards = set()
    for color in Color:
        for number in Number:
            cards.add(Card(color, number))
    
    print (cards)


if __name__ == "__main__":
    main()
    
