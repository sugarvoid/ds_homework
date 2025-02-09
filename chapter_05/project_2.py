"""
Name:           David Durham
Week:           3
Project:        5.2
Description:    Implement a priority queue based on an ordered linked list. The items stored in the
                queue can be passed to a function that extracts their priority value (or key) as in the
                PriorityQueue.py module in Chapter 4. The remove operation on the priority queue
                should remove the item with the smallest key.
"""

from classes import PriorityOrderedList


def example():
    p_ordered_list = PriorityOrderedList()

    p_ordered_list.insert(26)
    p_ordered_list.insert(10)
    p_ordered_list.insert(5)
    p_ordered_list.insert(1)
    p_ordered_list.insert(54)
    p_ordered_list.insert(3)

    print("Initial peek")
    print(p_ordered_list.peek())
    p_ordered_list.remove()
    print("\nPeek after remove()")
    print(p_ordered_list.peek())


if __name__ == "__main__":
    example()
