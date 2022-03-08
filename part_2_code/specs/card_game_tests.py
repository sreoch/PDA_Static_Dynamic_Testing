import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def test_can_confirm_ace(self):
        self.ace = Card("Ace", 1);
        self.assertEqual(True, CardGame.check_for_ace(self, self.ace))

    def test_can_find_highest_card(self):
        self.card1 = Card("Hearts", 10);
        self.card2 = Card("Diamonds", 6);
        self.assertEqual(self.card1, CardGame.highest_card(self, self.card1, self.card2))

    def test_can_get_cards_total_value(self):
        self.card1 = Card("Hearts", 10);
        self.card2 = Card("Diamonds", 6);
        self.cards = [self.card1, self.card2];
        self.assertEqual("You have a total of 16", CardGame.cards_total(self, self.cards))