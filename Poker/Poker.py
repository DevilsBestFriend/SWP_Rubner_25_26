from enum import Enum
import random
import unittest

class testClassifyHand(unittest.TestCase):
  def test_highcard(self):
    hand = [Card(Color.K, Number.TWO), Card(Color.P, Number.FOUR), Card(Color.H, Number.SIX), Card(Color.D, Number.EIGHT), Card(Color.K, Number.TEN)]
    self.assertEqual(classify_hand(hand), Combinations.HIGHCARD)

  def test_pair(self):
    hand = [Card(Color.K, Number.TWO), Card(Color.P, Number.TWO), Card(Color.H, Number.SIX), Card(Color.D, Number.EIGHT), Card(Color.K, Number.TEN)]
    self.assertEqual(classify_hand(hand), Combinations.PAIR)

  def test_twopair(self):
    hand = [Card(Color.K, Number.TWO), Card(Color.P, Number.TWO), Card(Color.H, Number.SIX), Card(Color.D, Number.SIX), Card(Color.K, Number.TEN)]
    self.assertEqual(classify_hand(hand), Combinations.TWOPAIR)

  def test_threeofakind(self):
    hand = [Card(Color.K, Number.TWO), Card(Color.P, Number.TWO), Card(Color.H, Number.TWO), Card(Color.D, Number.EIGHT), Card(Color.K, Number.TEN)]
    self.assertEqual(classify_hand(hand), Combinations.THREEOFAKIND)

  def test_straight(self):
    hand = [Card(Color.K, Number.TWO), Card(Color.P, Number.THREE), Card(Color.H, Number.FOUR), Card(Color.D, Number.FIVE), Card(Color.K, Number.SIX)]
    self.assertEqual(classify_hand(hand), Combinations.STRAIGHT)
    hand = [Card(Color.K, Number.ACE, ), Card(Color.P, Number.TWO), Card(Color.H, Number.THREE), Card(Color.D, Number.FOUR), Card(Color.K, Number.FIVE)]
    self.assertEqual(classify_hand(hand), Combinations.STRAIGHT)

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
    return str(self.number.value)+" "+str(self.color.value)
    
def dealhand(cards):
  hand = [random.sample(cards,5)]
  hand = sorted(hand[0], key=lambda x: x.number.value)
  return hand

def classify_hand(hand):
    is_consecutive = all(hand[i + 1].number.value == hand[i].number.value + 1 for i in range(4)) or hand[
      4].number == Number.ACE and hand[0].number == Number.TWO and all(
      hand[i + 1].number.value == hand[i].number.value + 1 for i in range(3))
    is_same_suit = all(card.color == hand[0].color for card in hand)
    if is_consecutive and is_same_suit:
      return Combinations.STRAIGHTFLUSH
    elif is_same_suit:
      return  Combinations.FLUSH
    elif is_consecutive:
      return Combinations.STRAIGHT
    elif all(hand[i + 1].number.value == hand[i].number.value for i in range(3)) or all(
            hand[i + 1].number.value == hand[i].number.value for i in range(1, 4)):
      return Combinations.FOUROFAKIND
    elif (hand[0].number == hand[1].number == hand[2].number and hand[3].number == hand[4].number) or (
            hand[0].number == hand[1].number and hand[2].number == hand[3].number == hand[4].number):
      return Combinations.FULLHOUSE
    elif (hand[0].number == hand[1].number == hand[2].number) or (
            hand[1].number == hand[2].number == hand[3].number) or (hand[2].number == hand[3].number == hand[4].number):
      return Combinations.THREEOFAKIND
    elif (hand[0].number == hand[1].number and hand[2].number == hand[3].number) or (
            hand[0].number == hand[1].number and hand[3].number == hand[4].number) or (
            hand[1].number == hand[2].number and hand[3].number == hand[4].number):
      return Combinations.TWOPAIR
    elif hand[0].number == hand[1].number or hand[1].number == hand[2].number or hand[2].number == hand[3].number or \
            hand[3].number == hand[4].number:
      return Combinations.PAIR
    else:
      return Combinations.HIGHCARD

def generate_cards():
    cards = []
    for color in Color:  # Generate a list of all cards
        for number in Number:
            cards.append(Card(color, number))
    return cards

def main ():
  cards = generate_cards()

  tests = input("How many tests to run? [Default: 10000]")
  try:
    tests = 10000 if len(tests) == 0 else int(tests) # ternary operator
  except ValueError:
      print("Invalid input, using default value of 10000")
      tests = 10000
  results = [0, 0, 0, 0, 0, 0, 0, 0, 0]
  for _ in range(tests):
    combination = classify_hand(dealhand(cards))
    results[combination.value] += 1
  
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
  #unittest.main()
  main()
