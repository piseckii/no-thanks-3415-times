from src.card import Card
import random

class Deck:
    def __init__(self, cards: list[Card] | None = None):
        if cards == None:
            cards = Card.all_cards
        self.cards: list[Card] = cards
        
        
    def __repr__(self):
        """Вывод массива карт"""
        return f'{self.cards}'
    
    def __eq__(self, other):
        return self.cards == other.cards
        
      
    def save(self) -> list[str]:
        return [Card.save(card) for card in self.cards]
    
    
    @classmethod
    def load(cls, ls: list[str]):
        """Convert list[str] to list[Card]"""
        return cls(cards = [Card.load(txt) for txt in ls])


    def draw_card(self):
        """Берем карту из колоды и возвращаем ее."""
        return self.cards.pop(0)


    def shuffle(self):
        random.shuffle(self.cards)
        