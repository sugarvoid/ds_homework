from typing import Any, Callable, Optional


def identity(x):  # The identity function
    return x


class Array(object):
    def __init__(self, initial_size: int):
        self.__list: list = [None] * initial_size  # The array stored as a list
        self.__item_count: int = 0  # No items in array initially

    def __len__(self):  # Special def for len() func
        return self.__item_count  # Return number of items

    def get(self, n: int) -> Optional[Any]:  # Return the value at index n
        if 0 <= n and n < self.__item_count:  # Check if n is in bounds, and
            return self.__list[n]  # only return item if in bounds

    def set(self, n: int, value: Any) -> None:  # Set the value at index n
        if 0 <= n and n < self.__item_count:  # Check if n is in bounds, and
            self.__list[n] = value  # only set item if in bounds

    def insert(self, item: Any) -> None:  # Insert item at end
        self.__list[self.__item_count] = item  # Item goes at current end
        self.__item_count += 1  # Increment number of items

    def find(self, item: Any) -> int:  # Find index for item
        for j in range(self.__item_count):  # Among current items
            if self.__list[j] == item:  # If found,
                return j  # then return index to item
        return -1  # Not found -> return -1

    def search(self, item: Any) -> Optional[Any]:  # Search for item
        return self.get(self.find(item))  # and return item if found

    def delete(self, item: Any) -> None:  # Delete first occurrence
        for j in range(self.__item_count):  # of an item
            if self.__list[j] == item:  # Found item
                self.__item_count -= 1  # One fewer at end
                for k in range(j, self.__item_count):  # Move items from
                    self.__list[k] = self.__list[k + 1]  # right over 1
                return True  # Return success flag
        return False  # Made it here, so couldn't find the item

    def traverse(self, function: Callable = print) -> None:  # Traverse all items
        for j in range(self.__item_count):  # and apply a function
            function(self.__list[j])


# Implement an Ordered Array of Records structure
class OrderedRecordArray(object):
    def __init__(self, initialSize, key=identity):  # Constructor
        self.__a = [None] * initialSize  # The array stored as a list
        self.__nItems = 0  # No items in array initially
        self.__key = key  # Key function gets record key

    def __len__(self):  # Special def for len() func
        return self.__nItems  # Return number of items

    def get(self, n: int):  # Return the value at index n
        if n >= 0 and n < self.__nItems:  # Check if n is in bounds, and
            return self.__a[n]  # only return item if in bounds
        raise IndexError("Index " + str(n) + " is out of range")

    def traverse(self, function: Callable = print):  # Traverse all items
        for j in range(self.__nItems):  # and apply a function
            function(self.__a[j])

    def __str__(self):  # Special def for str() func
        ans = "["  # Surround with square brackets
        for i in range(self.__nItems):  # Loop through items
            if len(ans) > 1:  # Except next to left bracket,
                ans += ", "  # separate items with comma
            ans += str(self.__a[i])  # Add string form of item
        ans += "]"  # Close with right bracket
        return ans

    def find(self, key):  # Find index at or just below key
        lo = 0  # in ordered list
        hi = self.__nItems - 1  # Look between lo and hi
        while lo <= hi:
            mid = (lo + hi) // 2  # Select the midpoint
        if self.__key(self.__a[mid]) == key:  # Did we find it?
            return mid  # Return location of item
        elif self.__key(self.__a[mid]) < key:  # Is key in upper half?
            lo = mid + 1  # Yes, raise the lo boundary
        else:
            hi = mid - 1  # No, but could be in lower half
        return lo  # Item not found, return insertion point instead

    def search(self, key):
        idx = self.find(key)  # Search for a record by its key
        if idx < self.__nItems and self.__key(self.__a[idx]) == key:
            return self.__a[idx]  # and return item if found

    def insert(self, item: Any):  # Insert item into the correct position
        if self.__nItems >= len(self.__a):  # If array is full,
            raise Exception("Array overflow")  # raise exception
        j = self.find(self.__key(item))  # Find where item should go
        for k in range(self.__nItems, j, -1):  # Move bigger items right
            self.__a[k] = self.__a[k - 1]
        self.__a[j] = item  # Insert the item
        self.__nItems += 1  # Increment the number of items

    def delete(self, item: Any):  # Delete any occurrence
        j = self.find(self.__key(item))  # Try to find the item
        if j < self.__nItems and self.__a[j] == item:  # If found,
            self.__nItems -= 1  # One fewer at end
            for k in range(j, self.__nItems):  # Move bigger items left
                self.__a[k] = self.__a[k + 1]
        return True  # Return success flag

        return False  # Made it here; item not found


class OrderedArray(object):
    def __init__(self, initialSize: int):  # Constructor
        self.__a = [None] * initialSize  # The array stored as a list
        self.__nItems = 0  # No items in array initially

    def __len__(self):  # Special def for len() func
        return self.__nItems  # Return number of items

    def get(self, n):  # Return the value at index n
        if 0 <= n and n < self.__nItems:  # Check if n is in bounds,
            return self.__a[n]  # only return item if in bounds
        raise IndexError("Index " + str(n) + " is out of range")

    def traverse(self, function=print):  # Traverse all items and apply a function
        for j in range(self.__nItems):  # Loop through items
            function(self.__a[j])

    def __str__(self):  # Special def for str() func
        ans = "["  # Surround with square brackets
        for i in range(self.__nItems):  # Loop through items
            if len(ans) > 1:  # Except next to left bracket,
                ans += ", "  # separate items with a comma
            ans += str(self.__a[i])  # Add string form of item
        ans += "]"  # Close with right bracket
        return ans

    def find(self, item):  # Find index at or just below item in ordered list
        lo = 0  # Look between lo and hi
        hi = self.__nItems - 1
        while lo <= hi:
            mid = (lo + hi) // 2  # Select the midpoint
            if self.__a[mid] == item:  # Did we find it at midpoint?
                return mid  # Return location of item
            elif self.__a[mid] < item:  # Is item in upper half?
                lo = mid + 1  # Yes, raise the lo boundary
            else:
                hi = mid - 1  # No, but could be in lower half
        return lo  # Item not found, return insertion point instead

    def search(self, item):  # Search for item
        index = self.find(item)  # Find the index where item should go
        if index < self.__nItems and self.__a[index] == item:
            return self.__a[index]  # Return item if found

    def insert(self, item):  # Insert item into correct position
        if self.__nItems >= len(self.__a):  # If array is full,
            raise Exception("Array overflow")  # raise exception
        index = self.find(item)  # Find index where item should go
        for j in range(self.__nItems, index, -1):  # Move bigger items to the right
            self.__a[j] = self.__a[j - 1]  # Shift item
        self.__a[index] = item  # Insert the item
        self.__nItems += 1  # Increment the number of items

    def delete(self, item):  # Delete any occurrence of item
        j = self.find(item)  # Try to find the item
        if j < self.__nItems and self.__a[j] == item:  # If found
            self.__nItems -= 1  # One fewer at the end
            for k in range(j, self.__nItems):  # Move bigger items left
                self.__a[k] = self.__a[k + 1]
            return True  # Return success flag
        return False  # Item not found