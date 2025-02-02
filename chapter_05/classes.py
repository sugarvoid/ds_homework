class LinkedList(object):  
    # A linked list of data elements
    def __init__(self):  
        # Constructor
        self.__first = None  # Reference to first Link

    def getFirst(self):
        # Return the first link
        return self.__first  

    def setFirst(self, link):  
        # Change the first link to a new Link
        if link is None or isinstance(link, Link):  
            # It must be None or a Link object
            self.__first = link
        else:
            raise Exception("First link must be Link or None")

    def getNext(self):
        # First link is next
        return self.getFirst()

    def setNext(self, link):
        # First link is next
        self.setFirst(link)

    def isEmpty(self):  
        # Test for empty list
        return self.getFirst() is None  
        # True iff no first Link

    def first(self):  
        # Return the first item in the list
        if self.isEmpty():  
            # Raise an exception if the list is empty
            raise Exception('No first item in empty list')
        return self.getFirst().getData()  # Return data item (not Link)

    def traverse(self, func=print):  
        # Apply a function to all items in the list
        link = self.getFirst()  # Start with first link
        while link is not None:  # Keep going until no more links
            func(link.getData())  # Apply the function to the item
            link = link.getNext()  # Move on to next link

    def __len__(self):  
        # Get the length of the list
        l = 0
        link = self.getFirst()  # Start with first link
        while link is not None:  # Keep going until no more links
            l += 1  # Count link in chain
            link = link.getNext()  # Move on to next link
        return l

    def __str__(self):  
        # Build a string representation
        result = "["  # Enclose list in square brackets
        link = self.getFirst()  # Start with first link
        while link is not None:  # Keep going until no more links
            if len(result) > 1:  
                # After the first link, separate links with a right arrowhead
                result += " > "  
            result += str(link)  # Append string version of link
            link = link.getNext()  # Move on to next link
        return result + "]"  # Close with square bracket



class Link(object):  
    # One datum in a linked list
    def __init__(self, datum, next=None):  
        # Constructor
        self.__data = datum  # The datum for this link
        self.__next = next  # Reference to next Link

    def getData(self):  
        # Return the datum stored in this link
        return self.__data

    def setData(self, datum):  
        # Change the datum in this Link
        self.__data = datum

    def getNext(self):  
        # Return the next link
        return self.__next

    def setNext(self, link):  
        # Change the next link to a new Link
        if link is None or isinstance(link, Link):  
            # Must be Link or None
            self.__next = link
        else:
            raise Exception("Next link must be Link or None")

    def isLast(self):  
        # Test if link is last in the chain
        return self.getNext() is None  
        # True if & only if no next Link

    def __str__(self):  
        # Make a string representation of link
        return str(self.getData())
