from typing import Any, Callable, Optional


# TODO: The book uses, this, but is it needed? (investigate)
def identity(x):
    return x


class Array(object):
    def __init__(self, initial_size: int):
        self.size = initial_size
        self.__item_limit = self.size
        # The array stored as a list
        self.__list: list = [None] * self.size
        # No items in array initially
        self.__item_count: int = 0

    # Special def for len() func
    def __len__(self):
        return self.__item_count

    def replace(self, new_array) -> None:
        self.__list = new_array
        self.__item_count = len(new_array)

    # Return the value at index n
    def get(self, index: int) -> Optional[Any]:
        """Returns the value a element at index

        Args:
            index (int): The index to search for

        Returns:
            Optional[Any]: The value of the element
        """
        # Check if index is in range
        if 0 <= index and index < self.__item_count:
            return self.__list[index]
        else:
            return None

    def set(self, index: int, new_value: Any) -> None:
        """Set the value of element at index

        Args:
            index (int): _description_
            new_value (Any): _description_
        """

        # Check if index is in range
        if 0 <= index and index < self.__item_count:
            self.__list[index] = new_value
        else:
            raise Exception(f"Failed to update at index:{index}. Out of range")

    def insert(self, item: Any) -> None:
        if self.__item_limit == self.__item_count:
            raise Exception(f"Failed to insert {item}. Array has reached its limit")
        self.__list[self.__item_count] = item
        self.__item_count += 1

    def find(self, item: Any) -> int:
        """Find index of item

        Args:
            item (Any): The value to look for

        Returns:
            int: The index of the value
        """
        for j in range(self.__item_count):
            if self.__list[j] == item:
                return j
        return -1  # Not found, return -1

    def search(self, item: Any) -> Optional[Any]:
        """Searches for value, returns if exist

        Args:
            item (Any): The item to search for

        Returns:
            Optional[Any]:
        """
        return self.get(self.find(item))

    def delete(self, item: Any) -> bool:
        """Deletes first occurrence of item

        Args:
            item (Any): The item to delete

        Returns:
            bool: Successful

        """
        for j in range(self.__item_count):
            if self.__list[j] == item:
                # Update array's item count
                self.__item_count -= 1
                # Shift remaining item over
                for k in range(j, self.__item_count):
                    self.__list[k] = self.__list[k + 1]
                return True
        return False

    def traverse(self, function: Callable = print) -> None:
        """Traverse all items

        Args:
            function (Callable, optional): What to do with each item. Defaults to print().
        """
        for j in range(self.__item_count):
            function(self.__list[j])

    def get_max_num(self) -> int | float | None:
        """Returns the value of the highest number in the array

        Returns:
            int | float: The value of the highest number, if exist. Otherwise returns None.
        """
        _tmp_list = []
        for item in self.__list:
            if isinstance(item, (int, float)):
                _tmp_list.append(item)

        if _tmp_list:
            return max(_tmp_list)

    def delete_max_num(self) -> int | float | None:
        """Returns and removes the value of the highest number in the array

        Returns:
            int | float: The value of the highest number, if exist. Otherwise returns None.
        """
        _tmp_list = []
        _highest = None
        for item in self.__list:
            if isinstance(item, (int, float)):
                _tmp_list.append(item)

        if _tmp_list:
            _tmp_list.sort()
            _highest = _tmp_list.pop()

            self.__list.remove(_highest)
            self.__item_count -= 1
            return _highest
        return None

    def remove_dupes(self) -> None:
        """Removes any duplicate entries in the array"""
        # TODO: Should I account for string case sensitivity or if a number is a string "77" vs 77
        _tmp_list = []
        for item in self.__list:
            # Since the array can be bigger than the number of items, need to make sure we don't touch the None values
            if item:
                if item not in _tmp_list:
                    _tmp_list.append(item)

        self.replace(_tmp_list)


class OrderedRecordArray(object):
    def __init__(
        self, initial_size: int, key: Callable = identity, resizable: bool = False
    ):
        self.__list = [None] * initial_size
        self.__item_limit = initial_size
        self.__item_count = 0
        self.__key = key
        self.__growth_amount = 10  # For when the array size is increased
        self.__is_resizable = resizable

    def __len__(self):
        return self.__item_count

    def get_size(self) -> int:
        """Get size of the array. (Not how many items)

        Returns:
            int:
        """
        return self.__item_limit

    def get(self, index: int) -> Optional[Any]:
        """Returns the value at index

        Args:
            index (int):

        Returns:
            Any:
        """
        # Check if index is in bounds, and
        if index >= 0 and index < self.__item_count:
            # Return item
            return self.__list[index]
        else:
            raise IndexError("Index " + str(index) + " is out of range")

    def traverse(self, function: Callable = print) -> None:
        """Traverse all items

        Args:
            function (Callable, optional): What to do with each item. Defaults to print().
        """
        for j in range(self.__item_count):
            function(self.__list[j])

    def __str__(self) -> str:
        _output_str = "["

        for i in range(self.__item_count):
            # Except next to left bracket
            if len(_output_str) > 1:
                # separate items with comma
                _output_str += ", "
            # Add string form of item
            _output_str += str(self.__list[i])
        # Close with right bracket
        _output_str += "]"
        return _output_str

    def find(self, key):
        """Find index at or just below key

        Args:
            key (_type_): _description_

        Returns:
            _type_: _description_
        """
        # in ordered list
        _low = 0

        # Look between low and high
        _high = self.__item_count - 1

        while _low <= _high:
            # Get the midpoint
            _mid = (_low + _high) // 2

            # Did we find it?
            if self.__key(self.__list[_mid]) == key:
                # Return location of item
                return _mid

            # Is key in upper half?
            elif self.__key(self.__list[_mid]) < key:
                # Yes, raise the lo boundary
                _low = _mid + 1
            else:
                # No, but could be in lower half
                _high = _mid - 1
        # Item not found, return insertion point instead
        return _low

    def search(self, key):
        """Searches for value based on its key

        Args:
            key (Any):

        Returns:
            Optional[Any]:
        """

        # Search for a record by its key
        _index = self.find(key)
        if _index < self.__item_count and self.__key(self.__list[_index]) == key:
            # and return item if found
            return self.__list[_index]
        else:
            return None

    def insert(self, item: Any):
        if self.__item_count >= len(self.__list):
            if self.__is_resizable:
                self.__increase_size()
            else:
                raise Exception("Array overflow")

        j = self.find(self.__key(item))  # Find where item should go
        for k in range(self.__item_count, j, -1):  # Move bigger items right
            self.__list[k] = self.__list[k - 1]
        self.__list[j] = item  # Insert the item
        self.__item_count += 1  # Increment the number of items

    def delete(self, item: Any):  # Delete any occurrence
        j = self.find(self.__key(item))  # Try to find the item
        if j < self.__item_count and self.__list[j] == item:  # If found,
            self.__item_count -= 1  # One fewer at end
            for k in range(j, self.__item_count):  # Move bigger items left
                self.__list[k] = self.__list[k + 1]
            return True  # Return success flag

        return False  # Made it here; item not found

    def __increase_size(self):
        """Increase size of Array"""

        # Determine the new size of the list
        _new_size = self.__item_limit + self.__growth_amount

        # Make the new list
        _new_list = [None] * _new_size

        # Loop through the current list and put the values into new one
        for i in range(self.__item_count):
            _new_list[i] = self.__list[i]

        # Use local variables to set Array properties
        self.__list = _new_list
        self.__item_limit = _new_size


class OrderedArray(object):
    def __init__(self, initial_size: int):
        self.__list = [None] * initial_size
        self.__item_count = 0

    def __len__(self):
        return self.__item_count

    def get(self, index):
        # Check if n is in bounds
        if 0 <= index and index < self.__item_count:
            return self.__list[index]
        else:
            raise IndexError(f"Index {str(index)} is out of range")

    def traverse(self, function=print):
        for j in range(self.__item_count):
            function(self.__list[j])

    def __str__(self):
        _output_str = "["
        for i in range(self.__item_count):
            if len(_output_str) > 1:
                _output_str += ", "
            _output_str += str(self.__list[i])
        _output_str += "]"
        return _output_str

    def find(self, item):
        """Find index at or just below item in ordered list

        Args:
            item (any):

        Returns:
            int: The index at or just below
        """

        # Look between lo and hi
        _low = 0
        _high = self.__item_count - 1
        while _low <= _high:
            # Get the midpoint
            _mid = (_low + _high) // 2

            # Did we find it at midpoint?
            if self.__list[_mid] == item:
                # Return location of item
                return _mid

            # Is item in upper half?
            elif self.__list[_mid] < item:
                # Yes, raise the lo boundary
                _low = _mid + 1
            else:
                # No, but could be in lower half
                _high = _mid - 1
        # Item not found, return insertion point instead
        return _low

    def search(self, item):  #
        """Search for item and return if found

        Args:
            item (_type_): The item to look for

        Returns:
            any:
        """
        # Find the index where item should go
        _index = self.find(item)
        if _index < self.__item_count and self.__list[_index] == item:
            return self.__list[_index]
        else:
            return None

    def insert(self, item):
        """Insert item into correct position

        Args:
            item (_type_): Item to insert
        """

        # If array is full,
        if self.__item_count >= len(self.__list):
            raise Exception("Array overflow")
        else:
            # Find index where item should go
            index = self.find(item)

            # Move bigger items to the right
            for j in range(self.__item_count, index, -1):
                # Shift item
                self.__list[j] = self.__list[j - 1]

            # Insert the item
            self.__list[index] = item

            # Increment the number of items
            self.__item_count += 1

    def delete(self, item):
        """Deletes any occurrence of item

        Args:
            item (_type_): The item to delete

        Returns:
            bool: Successful
        """
        # Try to find the item
        j = self.find(item)

        # If found
        if j < self.__item_count and self.__list[j] == item:
            # One fewer at the end
            self.__item_count -= 1

            # Move bigger items left
            for k in range(j, self.__item_count):
                self.__list[k] = self.__list[k + 1]
            return True

        # Item was not found
        return False
