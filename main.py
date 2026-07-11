# Here for:
#  Reading the user input
#  Checking which command the user requested
#  Creating the correct command
#  Executing it

import sys

from result import Result
from command_history import CommandHistory

from commands.increment import AddOneCommand
from commands.decrement import MinusOneCommand
from commands.double import DoubleCommand
from commands.randadd import AddRandomCommand


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <initial_value>")
        return

    try:
        initial_value = int(sys.argv[1])
    except ValueError:
        print("use an integer as initial value")
        return

    result = Result(initial_value)
    history = CommandHistory()

    while True:
        user_input = input("Enter command: ").strip().lower()

        if user_input == "increment":
            command = AddOneCommand(result)
            command.execute()
            history.add_command(command)
            print(result.get_value())

        elif user_input == "decrement":
            command = MinusOneCommand(result)
            command.execute()
            history.add_command(command)
            print(result.get_value())

        elif user_input == "double":
            command = DoubleCommand(result)
            command.execute()
            history.add_command(command)
            print(result.get_value())

        elif user_input == "randadd":
            command = AddRandomCommand(result)
            command.execute()
            history.add_command(command)
            print(result.get_value())

        elif user_input == "undo":
            if history.is_empty():
                print("Nothing to undo")
            else:
                command = history.get_last_command()
                command.undo()
                print(result.get_value())

        elif  user_input == "exit":
            print("Program stopped")
            break

        else:
            print("please enter a valid command: increment, decrement, double, randadd, undo, exit")


if __name__ == "__main__":
    main()