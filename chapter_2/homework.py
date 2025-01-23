from classes import Array, OrderedRecordArray
from random import choice, randint
from string import ascii_letters

MAX_SIZE = 100  # Max size of the array


def second(x: list):  # Key on second element of record
    return x[1]


def test_function():
    return "nothing"


def project_2_1():
    array = Array(MAX_SIZE)
    array.insert(77)
    array.insert(99)
    array.insert(test_function)
    array.insert(100)
    array.insert(-49)
    array.insert("alpha")
    array.insert("beta")
    array.insert("charlie")
    array.insert("delta")

    print(f"The max numeric value is: {array.get_max_num()}")


def project_2_2():
    array = Array(MAX_SIZE)
    array.insert(77)
    array.insert(99)
    array.insert(100)
    array.insert(-49)
    array.insert("alpha")
    array.insert("beta")
    array.insert("charlie")
    array.insert("delta")

    print("Before delete_max_num()")
    print(f"Array size: {len(array)}. Highest numeric value: {array.get_max_num()}")
    print(array.delete_max_num())

    print("After delete_max_num()")
    print(f"Array size: {len(array)}. Highest numeric value: {array.get_max_num()}")


def project_2_4():
    array = Array(MAX_SIZE)
    array.insert(77)
    array.insert(77)
    array.insert(77)
    array.insert(77)
    array.insert(99)
    array.insert(100)
    array.insert(-49)
    array.insert("alpha")
    array.insert("beta")
    array.insert("charlie")
    array.insert("delta")
    array.insert("delta")
    array.insert("delta")
    array.insert("delta")

    print("Array before remove_dupes()")
    print(len(array))
    # array.traverse()
    array.remove_dupes()
    print("Array after remove_dupes()")
    print(len(array))
    # array.traverse()


def project_2_7():
    maxSize = 5
    arr = OrderedRecordArray(maxSize, second, resizable=True)

    for _ in range(5):
        _random_letter = choice(ascii_letters)
        _random_int = randint(1,50)
        arr.insert((_random_letter, _random_int))

    print(f"Array's size: {arr.get_size()}")
    print("Array containing", len(arr), "items:\n", arr)
    arr.insert(("new", 8))
    print("Array after insert has", len(arr), "items:\n", arr)
    print(f"Array's size: {arr.get_size()}")


if __name__ == "__main__":
    # project_2_1()
    # project_2_2()
    #project_2_4()
    project_2_7()
