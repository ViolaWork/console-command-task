from command_history import CommandHistory

class DummyCommand:
    def execute(self):
        pass

    def undo(self):
        pass


def test_history_if_empty():
    history = CommandHistory()

    try:
        assert history.is_empty() is True
        print("history is empty")
    except AssertionError:
        print("history is not empty")


def test_history_after_adding_command():
    history = CommandHistory()
    command = DummyCommand()

    history.add_command(command)

    try:
        assert history.is_empty() is False
        print("after adding command, history is not empty")
    except AssertionError:
        print("after adding command, history is empty")


def test_get_last_command():
    history = CommandHistory()
    first = DummyCommand()
    second = DummyCommand()

    history.add_command(first)
    history.add_command(second)

    try:
        assert history.get_last_command() is second
        print("history knows the last command")
    except AssertionError:
        print("history does not know the last command")



if __name__ == "__main__":
    test_history_if_empty()
    test_history_after_adding_command()
    test_get_last_command()
