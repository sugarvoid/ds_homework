class Array(object):
    def __init__(self, initial_size):  # Constructor
        # The array stored as a list
        self.__a = [None] * initial_size
        # No items in array initially
        self.__n_items = 0

    def __len__(self):  # Special def for len() func
        # Return number of items
        return self.__n_items

    def get(self, n):  # Return the value at index n
        # Check if n is in bounds
        if 0 <= n and n < self.__n_items:
            # Only return item if in bounds
            return self.__a[n]

    def set(self, n, value):  # Set the value at index n
        # Check if n is in bounds
        if 0 <= n and n < self.__n_items:
            # Only set item if in bounds
            self.__a[n] = value

    def swap(self, j, k):  # Swap the values at 2 indices
        # Check if indices are in bounds before processing
        if (0 <= j and j < self.__n_items and 0 <= k and k < self.__n_items):
            self.__a[j], self.__a[k] = self.__a[k], self.__a[j]

    def insert(self, item):  # Insert item at end
        # If array is full, raise exception
        if self.__n_items >= len(self.__a):
            raise Exception("Array overflow")
        # Item goes at current end
        self.__a[self.__n_items] = item
        # Increment number of items
        self.__n_items += 1

    def find(self, item):  # Find index for item
        # Among current items
        for j in range(self.__n_items):
            if self.__a[j] == item:
                # If found, return index to element
                return j
        # Not found, return -1
        return -1

    def search(self, item):  # Search for item
        # Return item if found
        return self.get(self.find(item))

    def delete(self, item):  # Delete first occurrence of an item
        # Search for the item
        for j in range(self.__n_items):
            if self.__a[j] == item:
                # One fewer at end
                self.__n_items -= 1
                # Move items from right over 1
                for k in range(j, self.__n_items):
                    self.__a[k] = self.__a[k + 1]
                # Return success flag
                return True
        # If not found, return False
        return False

    def traverse(self, function=print):  # Traverse all items
        # And apply a function
        for j in range(self.__n_items):
            function(self.__a[j])

    def __str__(self):  # Special def for str() func
        ans = "["  # Surround with square brackets
        for i in range(self.__n_items):  # Loop through items
            if len(ans) > 1:  # Except next to left bracket,
                ans += ", "  # Separate items with comma
            # Add string form of item
            ans += str(self.__a[i])
        # Close with right bracket
        ans += "]"
        return ans

    def bubble_sort(self):  # Sort by comparing adjacent values
        # Bubble up the elements
        for last in range(self.__n_items - 1, 0, -1):
            for inner in range(last):  # Inner loop goes up to last
                # If element is less than adjacent value, swap
                if self.__a[inner] > self.__a[inner + 1]:
                    self.swap(inner, inner + 1)

    def selection_sort(self):  # Sort by selecting min and swapping min to leftmost
        # Assume min is leftmost
        for outer in range(self.__n_items - 1):
            min_index = outer
            for inner in range(outer + 1, self.__n_items):  # Hunt to the right
                # If we find a new min, update the min index
                if self.__a[inner] < self.__a[min_index]:
                    min_index = inner
            # Swap leftmost element and min
            self.swap(outer, min_index)

    def insertion_sort(self):  # Sort by repeated inserts
        # Mark one element
        for outer in range(1, self.__n_items):
            temp = self.__a[outer]
            inner = outer  # Inner loop starts at mark
            # If marked element smaller, shift element to right
            while inner > 0 and temp < self.__a[inner - 1]:
                self.__a[inner] = self.__a[inner - 1]
                inner -= 1
            # Move marked element to 'hole'
            self.__a[inner] = temp
