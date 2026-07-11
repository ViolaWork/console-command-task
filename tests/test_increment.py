from result import Result
from commands.increment import AddOneCommand

def test_increments():
    result = Result(5)
    command = AddOneCommand(result)

    try:
        command.execute()

        assert result.get_value() == 6
        print("Increment added one to the result")

    except AssertionError:
        print("Increment could not add one to result")


def test_undo_in_increment():
    result = Result(5)
    command = AddOneCommand(result)

    try:
        command.execute()
        command.undo()

        assert result.get_value() == 5
        print("Undo restored original value of result")

    except AssertionError:
        print("Undo could not restore original value Of result")


if __name__ == "__main__":
    test_increments()
    test_undo_in_increment()
