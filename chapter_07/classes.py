def identity(x):
    # Identity function
    return x

import SortArray

class Array(SortArray.Array):
    # Base new Array class on SortArray
    def __part(self, pivot, lo, hi, key=identity):
        # Private function partitions array by items
        # whose keys are below or equal to pivot, and the rest to the right
        while lo <= hi:
            # Loop until no more items to inspect
            while key(self.get(lo)) < pivot:
                # Increment lo until we find a key that's not in the lower partition
                lo += 1
            while key(self.get(hi)) < pivot:
                # Decrement hi until it points to key in the lower partition
                hi -= 1
            if lo >= hi:
                # If lo is at or above hi, then the lower partition ends at lo
                return lo
            self.swap(lo, hi)
            # Swap the items at lo & hi
            lo, hi = lo + 1, hi - 1
            # Continue partitioning in between
        return lo  # Range to partition is now empty

    def quicksort(self, lo=0, hi=None, short=3, key=identity):
        # Sort items in an array between lo and hi indices using Hoare's quicksort algorithm
        if hi is None:
            # Fill in hi value if not specified
            hi = len(self) - 1  # as last item in array
        short = max(3, short)  # Enforce short limit >= 3
        if hi - lo + 1 <= short:
            # If subarray is short, then use insertion sort
            return self.insertion_sort(lo, hi, key)
        pivot_item = self.median_of_three(lo, hi, key)
        # Else find median key of lo, mid, hi and place item at hi index
        hi_part = self.__part(key(pivot_item), lo + 1, hi - 1, key)
        # Partition array around the key of the pivot item
        # and record where high part starts
        self.swap(hi_part, hi)
        # Swap pivot with high part start
        self.quicksort(lo, hi_part - 1, short, key)  # Sort lower part
        self.quicksort(hi_part + 1, hi, short, key)  # Sort higher part

    def median_of_three(self, lo, hi, key=identity):
        # Find median of lo, middle, and hi keys in subarray
        # and put median in hi position for partition
        mid = (lo + hi) // 2  # Compute middle index
        if key(self.get(lo)) > key(self.get(mid)):
            # Compare 1st pair of keys and swap if lo > mid
            self.swap(lo, mid)
        if key(self.get(lo)) > key(self.get(hi)):
            # Compare 2nd pair of keys and swap if hi is lowest
            self.swap(lo, hi)
        # At this point lo has the minimum of the 3 keys
        if key(self.get(hi)) > key(self.get(mid)):
            # Compare 3rd pair of keys again and swap if hi > mid
            self.swap(hi, mid)
        return self.get(hi)  # Return item with median key (@ hi)

    def insertion_sort(self, lo=0, hi=None, key=identity):
        # Sort subarray by repeated inserts
        # This insertion sort will be used on small subarrays by quicksort
        if hi is None:
            # Fill in hi value if not specified
            hi = len(self) - 1  # as last item in array
        for outer in range(lo + 1, hi + 1):
            # Mark one item
            temp = self.get(outer)  # Store marked item in temp
            temp_key = key(temp)
            inner = outer  # Inner loop starts at mark at right
            while inner > lo and temp_key < key(self.get(inner - 1)):
                # If inner hasn't reached lo and next item's key is smaller
                self.set(inner, self.get(inner - 1))
                # Shift next item to right & move inner left
                inner -= 1
            self.set(inner, temp)  # Move marked item to 'hole'
