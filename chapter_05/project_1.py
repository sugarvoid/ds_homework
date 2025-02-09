"""
Name:           David Durham
Week:           3
Project:        5.1
Description:    Rewrite the traverse(), __str__(), and __len__() methods of the LinkedList
                class to use the iterator (created by the generator).
"""

from classes import LinkedList


def display_methods():
    linked_list = LinkedList()

    linked_list.insert("dog")
    linked_list.insert("cat")
    linked_list.insert("bird")

    print("\n__len__")
    print(linked_list.get_len_string())

    print("\nTraversing")
    linked_list.traverse()

    print("\n__str__")
    print(linked_list)

    # To showcase the dynamic len sentence
    linked_list.remove()
    linked_list.remove()

    print("\n __len__ (after removing all but one)")
    print(linked_list.get_len_string())


if __name__ == "__main__":
    display_methods()
