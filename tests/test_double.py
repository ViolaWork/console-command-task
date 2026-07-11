from result import Result
from commands.double import DoubleCommand


def test_double():
    result = Result(7)
    command = DoubleCommand(result)

    try:
        command.execute()

        assert result.get_value() == 14
        print("the result was doubled")

    except AssertionError:
        print("the result could not be doubled")

def test_undo_in_double():
    result = Result(7)
    command = DoubleCommand(result)

    try:
        command.execute()
        command.undo()

        assert result.get_value() == 7
        print("the result could restore the original value")

    except AssertionError:
        print("the result could not restore the original value")



if __name__ == "__main__":
    test_double()
    test_undo_in_double()
