from classes import Array

maxSize = 100  # Max size of the array
array = Array(maxSize)  # Create an array object

array.insert(77)  # Insert 10 items
array.insert(99)
array.insert(99)
array.insert(99)
array.insert("foo")
array.insert("bar")
array.insert("bar")
array.insert("bar")
#array.insert(44)
##array.insert(55)
#array.insert(12.34)
#array.insert(0)
array.insert("baz")
#array.insert(-17)
# print("Array containing", len(array), "items")
# array.traverse()
# print("Search for 12 returns", array.search(12))
# print("Search for 12.34 returns", array.search(12.34))
# print("Deleting 0 returns", array.delete(0))
# print("Deleting 17 returns", array.delete(17))
# print("Setting item at index 3 to 33")
# array.set(3, 33)
# print("Array after deletions has", len(array), "items")
# array.traverse()


print(f" size before delete_max_num() {len(array)}")
print( array.delete_max_num())
print(f" size after delete_max_num() {len(array)}")
