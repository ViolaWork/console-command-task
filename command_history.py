#Here for remembering executed commands so undo can work. i will use a Last in, First out (LIFO) data structure


class CommandHistory:
    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def get_last_command(self):
        if not self.is_empty():
            return self.commands.pop()
        return None

    def is_empty(self):
        return len(self.commands) == 0