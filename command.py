# Here for execute and undo
# I create a class that defines rules for other classes
# execute: Should Execute the command and update the result
# undo: Should undo the command and update the result
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass