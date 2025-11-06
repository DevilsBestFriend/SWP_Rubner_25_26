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
  HIGHCARD = 0
  PAIR = 1
  TWOPAIR = 2
  THREEOFAKIND = 3
  STRAIGHT = 4
  FLUSH = 5
  FULLHOUSE = 6
  FOUROFAKIND = 7
  STRAIGHTFLUSH = 8

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
    
def test_probability (cards, tests = 10000):
  results = [0,0,0,0,0,0,0,0,0]
  for _ in range(tests):
    hand = dealhand(cards)
    is_consecutive = all(hand[i+1].number.value == hand[i].number.value + 1 for i in range(4))
    is_same_suit = all(card.color == hand[0].color for card in hand)
    if is_consecutive and is_same_suit:
        results[Combinations.STRAIGHTFLUSH.value] += 1
        continue
    elif is_same_suit:
      results[Combinations.FLUSH.value] += 1
      continue
    elif is_consecutive:
      results[Combinations.STRAIGHT.value] += 1
      continue
    elif all(hand[i+1].number.value == hand[i].number.value for i in range(3)) or all(hand[i+1].number.value == hand[i].number.value for i in range(1,4)):
      results[Combinations.FOUROFAKIND.value] += 1
      continue
    elif (hand[0].number == hand[1].number == hand[2].number == hand[3].number) or (hand[1].number == hand[2].number == hand[3].number == hand[4].number):
      results[Combinations.FOUROFAKIND.value] += 1
      continue
    elif (hand[0].number == hand[1].number == hand[2].number and hand[3].number == hand[4].number) or (hand[0].number == hand[1].number and hand[2].number == hand[3].number == hand[4].number):
      results[Combinations.FULLHOUSE.value] += 1
      continue
    elif (hand[0].number == hand[1].number == hand[2].number) or (hand[1].number == hand[2].number == hand[3].number) or (hand[2].number == hand[3].number == hand[4].number):
      results[Combinations.THREEOFAKIND.value] += 1
      continue
    elif (hand[0].number == hand[1].number and hand[2].number == hand[3].number) or (hand[0].number == hand[1].number and hand[3].number == hand[4].number) or (hand[1].number == hand[2].number and hand[3].number == hand[4].number):
      results[Combinations.TWOPAIR.value] += 1
      continue
    elif hand[0].number == hand[1].number or hand[1].number == hand[2].number or hand[2].number == hand[3].number or hand[3].number == hand[4].number:
      results[Combinations.PAIR.value] += 1
      continue
    else:
      results[Combinations.HIGHCARD.value] += 1
      continue
  return results

def main ():
  cards = []
  for color in Color: # Generate a list of all cards
      for number in Number:
          cards.append(Card(color, number))
          
  tests = input("How many tests to run? [Default: 10000]")
  if len(tests) == 0:
    tests = 10000
  else:
    tests = int(tests)
  results = test_probability(cards, tests)
  
  name_relative = [
    ["Highcards\t", "50,1177%", Combinations.HIGHCARD],
    ["Pairs\t\t", "42,2569%", Combinations.PAIR],
    ["Two Pairs\t", "4,7539%", Combinations.TWOPAIR],
    ["Three of a Kinds", "2,1128%", Combinations.THREEOFAKIND],
    ["Straights\t", "0,3925%", Combinations.STRAIGHT],
    ["Flushs\t\t", "0,1965%", Combinations.FLUSH],
    ["Full Houses\t", "0,1441%", Combinations.FULLHOUSE],
    ["Pokers\t\t", "0,0240%", Combinations.FOUROFAKIND],
    ["Straight Flushs\t", "0,001544%", Combinations.STRAIGHTFLUSH],
  ]
  for nr in name_relative:
    print(f"{nr[0]}|\tAbsolute amount:\t{results[nr[2].value]}\tRelative amount: {results[nr[2].value]/tests*100:.6f}%\tTrue relative amount:\t{nr[1]}")
  
  
        
          
            
            



if __name__ == "__main__":
  main()
    
