from classes import LinkedList


linked_list = LinkedList()

# Insert some data into the list
linked_list.insert("dog")
linked_list.insert("cat")
linked_list.insert("bird")


print(f"LinkedList has {len(linked_list)} link{'s' if len(linked_list) != 1 else ''}")

linked_list.traverse()

print(linked_list)

