"""File to define Bear class"""

class Bear:
    
    age: int
    hunger_score: int

    def __init__(self, age2: int = 0, hunger_score2: int = 0):
        "Constructing a bear."
        self.age = age2
        self.hunger_score = hunger_score2

    def one_day(self):
        return None