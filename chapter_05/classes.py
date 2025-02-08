

from typing import Any


class LinkedList(object):  
    # A linked list of data elements
    def __init__(self):  
        # Constructor
        self.__first = None

    def get_first(self):
        # Return the first link
        return self.__first  

    def set_first(self, link):  
        # Change the first link to a new Link
        if link is None or isinstance(link, Link):  
            # It must be None or a Link object
            self.__first = link
        else:
            raise Exception("First link must be Link or None")
        
    def __iter__(self):
        # Define an iterator for the list
        _next = self.get_first()
        # Start with first Link
        while _next is not None:
            # yield data for the link
            yield _next.get_data() 
            # then move on to next link
            _next = _next.get_next() 

    def get_next(self):
        # First link is next
        return self.get_first()

    def set_next(self, link):
        # First link is next
        self.set_first(link)

    def is_empty(self):  
        # Test for empty list
        return self.get_first() is None  
        # True iff no first Link

    def first(self):  
        # Return the first item in the list
        if self.is_empty():  
            # Raise an exception if the list is empty
            raise Exception('No first item in empty list')
        # Return data item (not Link)
        return self.get_first().get_data()  

    def traverse(self, func=print):  
        # Apply a function to all items in the list using the iterator
        for data in self:
            # Apply the function to each datum
            func(data)  
    
    def __len__(self):  
        _count = 0
        for _ in self:
            _count += 1
        return _count

    def __str__(self):  
        # Join all elements with " > " using a generator expression
        _result = " > ".join(str(data) for data in self)  

        # Enclose the result in square brackets
        return f"[{_result}]"  
    
    
    def insert(self, datum: Any):
        # Insert a new datum at the start of the list

        # Create a new Link for the datum
        _link = Link(datum, self.get_first())  
        # Update list to include the new Link
        self.set_first(_link)  

    def find(self, goal, key=lambda x: x):
        # Find the first Link whose key matches the goal

        # Start at the first link
        _link = self.get_first()  

        # Search until the end of the list
        while _link is not None:  

            # Does this Link match?
            if key(_link.get_data()) == goal:  
                # If so, return the Link itself
                return _link  
            # Else, continue on along the list
            _link = _link.get_next()  
        # If no matching Link is found, return None
        return None  

    def search(self, goal, key=lambda x: x):
        # Find the first item whose key matches the goal

        # Look f_or the Link object that matches
        _link = self.find(goal, key) 

        # If found
        if _link is not None:  
             # Return its datum
            return _link.get_data() 
        # Return None if no matching datum is found
        return None  

    def insert_after(self, goal, newDatum, key=lambda x: x):
        # Insert a new datum after the first Link with a matching key

        # Find matching Link object
        _link = self.find(goal, key)  
        # If not found
        if _link is None: 
            # Return failure
            return False  
        
        # Create a new Link node with new datum
        newLink = Link(newDatum, _link.get_next())  
        # Insert after the matching link
        _link.set_next(newLink)  
        # Return success
        return True  




class Link(object):  
    # One datum in a linked list
    def __init__(self, datum, next_link=None):  

        # The datum for this link
        self.__data = datum  

        # Reference to next Link
        self.__next = next_link  

    def get_data(self):  
        # Return the datum stored in this link
        return self.__data

    def set_data(self, datum):  
        # Change the datum in this Link
        self.__data = datum

    def get_next(self):  
        # Return the next link
        return self.__next

    def set_next(self, link):  
        # Change the next link to a new Link
        if link is None or isinstance(link, Link):  
            # Must be Link or None
            self.__next = link
        else:
            raise Exception("Next link must be Link or None")

    def is_last(self):  
        # Test if link is last in the chain
        return self.get_next() is None  
        # True if & only if no next Link

    def __str__(self):  
        # Make a string representation of link
        return str(self.get_data())




class OrderedList(LinkedList):
    def __init__(self, key=lambda x: x):
        self.__first = None  # Reference to first Link, if any
        self.__key = key     # Function to retrieve key

    def get_first(self):
        return self.__first  # Return the first link

    def set_first(self, link):
        # Change the first link to a new Link
        if link is None or isinstance(link, Link):  # Must be Link or None
            self.__first = link
        else:
            raise Exception("First link must be Link or None")

    def find(self, goal):
        # Find the 1st Link whose key matches or is after the goal
        link = self.get_first()  # Start at first link, and search

        while link is not None and self.__key(link.getData()) < goal:  # While not at the end of the list and before the goal
            link = link.getNext()  # Advance to the next link

        return link  # Return Link at or just after goal, or None for end

    def search(self, goal):
        # Find the 1st datum whose key matches the goal
        link = self.find(goal)  # Look for Link object that matches

        if link is not None and self.__key(link.getData()) == goal:  # If Link found, and its key matches the goal
            return link.getData()  # Return its datum



# class PriorityQueue(object):
#     def __init__(self, pri=lambda x: x):  
#         self.__first = None  
#         self.__pri = pri

#     def insert(self, item):
#         # Insert item into the ordered linked list based on priority
#         new_link = Link(item)  # Create a new link for the item

#         # If the list is empty, or the new item has higher priority than the first item
#         if self.__first is None or self.__pri(item) < self.__pri(self.__first.get_data()):
#             new_link.set_next(self.__first)  # Point to the old first item
#             self.__first = new_link  # Make new item the first
#         else:
#             current: Link = self.__first
#             # Traverse the list to find the right position for the new item
#             while current.get_next() is not None and self.__pri(item) >= self.__pri(current.get_next().get_data()):
#                 current = current.get_next()

#             # Insert the new item in the right place
#             new_link.set_next(current.get_next()) #= current.next
#             current.set_next(new_link) #= new_link
    
#     def remove(self):
#         # Remove the item with the smallest priority (the first item in the list)
#         if self.is_empty():
#             raise Exception("Queue underflow")

#         # Remove the first link (smallest priority)
#         item = self.__first.get_data()
#         self.__first = self.__first.get_next()  # Move the first pointer to the next link
#         return item  # Return the removed item

#     def is_empty(self): return self.__first is None

#     def __len__(self): return self.__nItems
#     def peek(self):
#         if self.is_empty():
#             raise Exception("Queue is empty")
#         return self.__first.get_data()
    


class PriorityOrderedList():
    def __init__(self, key=lambda x: x):
        self.__first = None  
        self.__key = key 

    def get_first(self):
        return self.__first  # Return the first link

    def set_first(self, link):
        # Change the first link to a new Link
        if link is None or isinstance(link, Link):  # Must be Link or None
            self.__first = link
        else:
            raise Exception("First link must be Link or None")

    def insert(self, item):

        if not isinstance(item, (int, float)):
            raise TypeError(f"PriorityOrderedList class can only handle numbers, but got {type(item).__name__}")
        

        # Insert the item in sorted order based on the key
        new_link = Link(item)  # Create a new link for the item

        print(f"new item = {item}")

        # If the list is empty or the new item has a smaller priority (key), it goes at the front
        if self.__first is None or self.__key(item) < self.__key(self.__first.get_data()):
            print("adding item, but list already has something")
            new_link.set_next(self.__first)  # Point to the old first item
            self.__first = new_link  # Make new item the first
        else:
            print("new item????")
            current: Link = self.__first
            
            # Traverse the list to find the right position for the new item
            while current.get_next() is not None and self.__key(item) >= self.__key(current.get_next().get_data()):
                current = current.get_next()

            # Insert the new item in the right place
            new_link.set_next(current.get_next())
            current.set_next(new_link)
        #self.set_first(new_link)

    def remove(self):
        # Remove the item with the smallest priority (the first item in the list)
        if self.isEmpty():
            raise Exception("Queue underflow")

        # Remove the first link (smallest priority)
        item = self.__first.get_data()
        self.__first = self.__first.get_next()  # Move the first pointer to the next link
        return item  # Return the removed item

    def isEmpty(self):
        return self.__first is None  # Return True if the list is empty

    def peek(self):
        # Return the first item (smallest priority) without removing it
        if self.isEmpty():
            raise Exception("Queue is empty")
        return self.__first.get_data()

    def __len__(self):
        # Return the length of the list
        length = 0
        current = self.__first
        while current is not None:
            length += 1
            current = current.get_next()
        return length
