
#We Assume that: randadd adds a random integer between 1 and 10 inclusive.

import random
from command import Command

class AddRandomCommand(Command):
    def __init__(self, result):
        self.result = result
        self.random_value = None

    def execute(self):
        self.random_value = random.randint(1, 10)
        current_value = self.result.get_value()
        self.result.set_value(current_value + self.random_value)

    def undo(self):
        current_value = self.result.get_value()
        self.result.set_value(current_value - self.random_value)