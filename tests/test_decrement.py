from result import Result
from commands.decrement import MinusOneCommand


def test_minusone():
    result = Result(4)
    command = MinusOneCommand(result)

    try:
        command.execute()

        assert result.get_value() == 3
        print("it could subtract one from the result")

    except AssertionError:
        print("it could not subtract one from result")


def test_undo_in_minusone():
    result = Result(4)
    command = MinusOneCommand(result)

    try:
        command.execute()
        command.undo()

        assert result.get_value() == 4
        print("it could restore original value of result")

    except AssertionError:
        print("it could not restore original value of result")


if __name__ == "__main__":
    test_minusone()
    test_undo_in_minusone()