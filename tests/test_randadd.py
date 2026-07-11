from result import Result
from commands.randadd import AddRandomCommand


def test_add_random():
    result = Result(10)
    command = AddRandomCommand(result)

    try:
        command.execute()

        new_value = result.get_value()

        assert 11 <= new_value <= 20
        print("It added a random value")

    except AssertionError:
        print("It did not add a valid random value")


def test_undo_in_add_random():
    result = Result(10)
    command = AddRandomCommand(result)

    try:
        command.execute()
        command.undo()

        assert result.get_value() == 10
        print("It restored the original value")

    except AssertionError:
        print("It could not restore the original value before the random addition")


if __name__ == "__main__":
    test_add_random()
    test_undo_in_add_random()
