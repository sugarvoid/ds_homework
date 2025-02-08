
# Chapter 5 Assignment

This week, I choose to do projects 5.1 and 5.2


## LinkedList Class class

### Added 
- `__iter__()` method from the book
- PriorityOrderedList class **(Project 5.2)**. As of now, it can only handle integers 

### Changed 
- Method names to use ~~the best case~~ snake_case.
- Tweaked the `traverse()`, `__str__()`, and `__len__()` methods to use the `_iter__()` method. **(Project 5.1)**
- Replaced default key parameter with a lambda for `find()` `search()` and `insert_after()`. So the LinkedList class does not depend on a function outside its class definition. 

