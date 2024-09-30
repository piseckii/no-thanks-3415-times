from src.card import Card

class Top:
    def __init__(self, card: Card | None = None, score: int = 0):
        self.card = card
        self.score = score
        
    
    def __repr__(self):
        return f'{self.card} score: {self.score}'
    
    
    def __eq__(self, other):
        return self.card == other.card and self.score == other.score
    
    
    def save(self) -> dict:
        return {'card': self.card.save(), 'score': self.score}
    
    
    @classmethod
    def load(cls, d: dict):
        return cls(card = Card.load(d['card']), score = d['score'])
        


