"""File to define Bear class"""

class Bear:
    
    age: int
    hunger_score: int

    def __init__(self, age2: int = 0, hunger_score2: int = 0):
        "Constructing a bear."
        self.age = age2
        self.hunger_score = hunger_score2
    
    # def __str__(self):
    #     """Printing method."""
    #     output: str = f"Age of bear: {self.age}\n"
    #     output += f"Hunger score of bear: {self.hunger_score}"
    #     return output

    def one_day(self):
        return None
    

# sara_bear: Bear = Bear(20,10)
# print(sara_bear)