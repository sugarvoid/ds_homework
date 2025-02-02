"""
Name:           David Durham
Week:           2
Project:        4.1
Description:    A demonstration of the revisions on the Stack class
                to handle if something is pushed on to a full stack,
                or popped off an empty stack.
"""

from classes import Stack


# Pushing and popping within its index range
def test_1_pass() -> None:
    _stack = Stack(10)
    for word in [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
    ]:
        _stack.push(word)

    # Pop 3 items
    for _ in range(3):
        _stack.pop()

    # Push 2 item
    for _ in range(2):
        _stack.push("extra")


# Popping from an empty stack
def test_2_fail() -> None:
    _stack = Stack(0)
    _stack.pop()


# Pushing to a full stack
def test_3_fail() -> None:
    _stack = Stack(10)
    for w in [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
    ]:
        _stack.push(w)

    # Try to push an 11th item on a Stack with a max of 10
    _stack.push("eleven")


if __name__ == "__main__":
    test_1_pass()
    # test_2_fail()
    # test_3_fail()
