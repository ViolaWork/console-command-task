from command import Command

class DoubleCommand(Command):
    def __init__(self, result):
        self.result = result

    def execute(self):
        current_value = self.result.get_value()
        self.result.set_value(current_value * 2)

    def undo(self):
        current_value = self.result.get_value()
        self.result.set_value(int(current_value / 2))