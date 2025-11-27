import unittest
from Poker.Poker import classify_hand, Combinations, Card, Color, Number

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
    self.assertEqual(classify_hand(hand), Combinations.STRAIGHT, "Error with Ace low straight")

if __name__ == '__main__':
  unittest.main()