class Card:
    VALUES = list(range(3,36))
    
    
    def __init__(self, value: int):
        if value not in Card.VALUES:
              raise ValueError
        self.value = value
    
    
    def __repr__(self):
        return f'|{self.value}|'
    
    
    def __eq__(self, other):
        return self.value == other.value
    
    
    def save(self) -> str:
        """Example: Card(15) -> '15'."""
        return f'{self.value}'
    
    
    @staticmethod
    def load(text: str):
        """Example: load('15') -> Card(15)."""
        return Card(int(text))


    @staticmethod
    def all_cards(values: None | list[int] = None):
        if values is None:
            values = Card.VALUES
        cards = [Card(val) for val in values]
        return cards
        
    