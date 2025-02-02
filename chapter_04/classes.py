from typing import Any, Callable, Optional

# class InvalidStackOperation(Exception):
#     def __init__(self, message):
#         self.message = message
#         super().__init__(self.message)
#     def __str__(self):
#         return self.message


class Stack(object):
    # Constructor
    def __init__(self, size: int) -> None:
        # The stack stored as a list
        self.__max_size = size
        # No items initially
        self.__stack = [None] * self.__max_size
        self.__top = -1

    # Insert item at top of stack
    def push(self, item: Any) -> None:
        if self.is_full():
            raise OverflowError(
                f"Can not push [{str(item)}] into a Stack that is full."
            )
        else:
            # Advance the pointer
            self.__top += 1

            # Trim whitespace is item is string
            if isinstance(item, str):
                item = item.strip()
            # Store item
            self.__stack[self.__top] = item

    # Remove top item from stack
    def pop(self) -> Any | None:
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack.")
        else:
            # Top item
            top = self.__stack[self.__top]
            # Remove item reference
            self.__stack[self.__top] = None
            # Decrease the pointer
            self.__top -= 1
            # Return top item
            return top

    # Return top item
    def peek(self) -> Any | None:
        # If stack is not empty
        if not self.is_empty():
            # Return the top item
            return self.__stack[self.__top]

    # Check if stack is empty
    def is_empty(self) -> bool:
        return self.__top < 0

    # Check if stack is full
    def is_full(self) -> bool:
        # return len(self.__stack == self.__max_size)
        return self.__top + 1 == self.__max_size

    # Return # of items on stack
    def __len__(self) -> int:
        return self.__top + 1

    # Convert stack to string
    def __str__(self) -> str:
        # Start with left bracket
        ans = "["
        # Loop through current items
        for i in range(self.__top + 1):
            # Except next to left bracket,
            if len(ans) > 1:
                # separate items with comma
                ans += ", "
            # Add string form of item
            ans += str(self.__stack[i])
        # Close with right bracket
        ans += "]"
        return ans

    def get_stack_str(self):
        # TODO: Rename this function to something more fitting.
        _str = ""
        for item in self.__stack:
            if item is not None:
                _str += item
        return _str

    def get_reverse(self) -> Any:
        _reverse = ""
        for item in reversed(self.__stack):
            if item is not None:
                _reverse += item
        return _reverse
