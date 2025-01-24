# David Durham
# Week 1
# Project 2.7

from classes import Array, OrderedRecordArray
from random import choice, randint
from string import ascii_letters

# TODO: The book uses for the OrderRecordArray class, but is it needed? (investigate)
def second(x: list):
    return x[1]


def test_function():
    return "nothing"


# 2.1 Add a method that returns the value 
# of the highest number in the array, or None if the
# array has no numbers.
def project_2_1():
    _array_1 = Array(100)
    _array_1.insert(77)
    _array_1.insert(99)
    _array_1.insert(test_function)
    _array_1.insert(100)
    _array_1.insert(-49)
    _array_1.insert("alpha")
    _array_1.insert("beta")
    _array_1.insert("charlie")
    _array_1.insert("delta")
    print(f"The highest numeric value in array_1 is: {_array_1.get_max_num()}")


    _array_2 = Array(100)
    _array_2.insert(test_function)
    _array_2.insert("alpha")
    _array_2.insert(bytearray(5))
    _array_2.insert("beta")
    _array_2.insert("charlie")
    _array_2.insert("delta")
    _array_2.insert(True)
    print(f"The highest numeric value in array_2 is: {_array_2.get_max_num()}")


def project_2_2():
    _array = Array(100)
    _array.insert(77)
    _array.insert(99)
    _array.insert(100)
    _array.insert(-49)
    _array.insert("alpha")
    _array.insert("beta")
    _array.insert("charlie")
    _array.insert("delta")

    print("Before delete_max_num()")
    print(f"Array size: {len(_array)}. Highest numeric value: {_array.get_max_num()}")
    print(_array.delete_max_num())

    print("After delete_max_num()")
    print(f"Array size: {len(_array)}. Highest numeric value: {_array.get_max_num()}")


def project_2_4():
    _array = Array(100)
    _array.insert(77)
    _array.insert(77)
    _array.insert(77)
    _array.insert(77)
    _array.insert(99)
    _array.insert(100)
    _array.insert(-49)
    _array.insert("alpha")
    _array.insert("beta")
    _array.insert("charlie")
    _array.insert("delta")
    _array.insert("delta")
    _array.insert("delta")
    _array.insert("delta")

    print("Array before remove_dupes()")
    print(len(_array))
    # array.traverse()
    _array.remove_dupes()
    print("Array after remove_dupes()")
    print(len(_array))
    # array.traverse()


def project_2_7():
    # Create array and set array size to 5
    _array = OrderedRecordArray(5, second, resizable=True)

    # Add random data to arrow
    for _ in range(5):
        _random_letter = choice(ascii_letters)
        _random_int = randint(1, 50)
        _array.insert((_random_letter, _random_int))


    print(f"Array's size: {_array.get_size()}")
    print("Array containing", len(_array), "items:\n", _array)
    _array.insert(("new", 8))
    print("Array after insert has", len(_array), "items:\n", _array)
    print(f"Array's size: {_array.get_size()}")


if __name__ == "__main__":
    project_2_1()
    # project_2_2()
    # project_2_4()
    #project_2_7()
