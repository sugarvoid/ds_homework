
# Chapter 2 Assignment

This week, I choose to do projects 2.1, 2.2, 2.4 and 2.7


## Array class

### Changed 
- Variable names to be more clear.
### Added 
- More detailed error when trying to call `insert()` when the array if already full.
- `get_max_num()` that returns the value of the highest number in the array, or None if the array has no numbers. **(Project 2.1)**
- `delete_max_num()` that returns the value of the highest number in the array, or None if the array has no numbers. But also removes that number from the array. **(Project 2.2)**
- `remove_dupes()` that removes any duplicate entries in the array. **(Project 2.4)**
- `replace()` that replaces the array with a new array, since so far 2 projects required the array be modified and this made it easier since the internal list and the item_count had to be updated if time.

## OrderedRecordArray class

### Changed 
- Variable names to be more clear.
### Added 
- `__increase_size()` to handle resizing the list when an insert is attempted when the array is full. I chose to go with a fixed increase size of 10. But thought about making it an optional argument. **(Project 2.7)**
- Resizable argument to the constructor, to account for when the user wants a array to stay at a fix length. Default is False. 
- `get_size()` to be able to check if resizing increased properly. **(Project 2.7)**


