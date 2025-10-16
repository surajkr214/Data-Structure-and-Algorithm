"""
Doubly Linked List Implementation
A linear data structure where each node points to both next and previous nodes.
"""


class Node:
    """A node in the doubly linked list."""
    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """Doubly Linked List with common operations."""
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def is_empty(self):
        """Check if the list is empty."""
        return self.head is None
    
    def insert_at_beginning(self, data):
        """
        Insert a new node at the beginning of the list.
        Time Complexity: O(1)
        """
        new_node = Node(data)
        
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def insert_at_end(self, data):
        """
        Insert a new node at the end of the list.
        Time Complexity: O(1) - because we maintain tail pointer
        """
        new_node = Node(data)
        
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    
    def insert_at_position(self, data, position):
        """
        Insert a new node at a specific position.
        Time Complexity: O(n)
        """
        if position == 0:
            self.insert_at_beginning(data)
            return
        
        new_node = Node(data)
        current = self.head
        
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        
        if current is None:
            raise IndexError("Position out of range")
        
        if current.next is None:
            # Inserting at end
            self.insert_at_end(data)
        else:
            # Insert in middle
            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node
    
    def delete_at_beginning(self):
        """
        Delete the first node from the list.
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("List is empty")
        
        deleted_data = self.head.data
        
        if self.head == self.tail:
            # Only one node
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        
        return deleted_data
    
    def delete_at_end(self):
        """
        Delete the last node from the list.
        Time Complexity: O(1) - because we maintain tail pointer
        """
        if self.is_empty():
            raise IndexError("List is empty")
        
        deleted_data = self.tail.data
        
        if self.head == self.tail:
            # Only one node
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        
        return deleted_data
    
    def delete_by_value(self, value):
        """
        Delete the first node with the given value.
        Time Complexity: O(n)
        """
        if self.is_empty():
            raise ValueError("List is empty")
        
        current = self.head
        
        while current:
            if current.data == value:
                if current == self.head:
                    self.delete_at_beginning()
                elif current == self.tail:
                    self.delete_at_end()
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return
            current = current.next
        
        raise ValueError(f"Value {value} not found in list")
    
    def search(self, value):
        """
        Search for a value in the list.
        Returns the position (0-indexed) or -1 if not found.
        Time Complexity: O(n)
        """
        current = self.head
        position = 0
        
        while current:
            if current.data == value:
                return position
            current = current.next
            position += 1
        
        return -1
    
    def reverse(self):
        """
        Reverse the linked list in-place.
        Time Complexity: O(n)
        """
        if self.is_empty():
            return
        
        current = self.head
        self.head, self.tail = self.tail, self.head
        
        while current:
            # Swap next and prev pointers
            current.next, current.prev = current.prev, current.next
            current = current.prev  # Move to next node (which is now prev)
    
    def get_length(self):
        """
        Get the length of the linked list.
        Time Complexity: O(n)
        """
        count = 0
        current = self.head
        
        while current:
            count += 1
            current = current.next
        
        return count
    
    def display_forward(self):
        """Display the linked list from head to tail."""
        if self.is_empty():
            print("List is empty")
            return
        
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print(" <-> ".join(elements))
    
    def display_backward(self):
        """Display the linked list from tail to head."""
        if self.is_empty():
            print("List is empty")
            return
        
        elements = []
        current = self.tail
        while current:
            elements.append(str(current.data))
            current = current.prev
        
        print(" <-> ".join(elements))


# Example usage
if __name__ == "__main__":
    # Create a doubly linked list
    dll = DoublyLinkedList()
    
    print("=== Creating Doubly Linked List ===")
    dll.insert_at_end(10)
    dll.insert_at_end(20)
    dll.insert_at_end(30)
    dll.insert_at_beginning(5)
    print("Forward: ", end="")
    dll.display_forward()  # 5 <-> 10 <-> 20 <-> 30
    print("Backward: ", end="")
    dll.display_backward()  # 30 <-> 20 <-> 10 <-> 5
    
    print(f"\nLength: {dll.get_length()}")
    
    print("\n=== Inserting 15 at position 2 ===")
    dll.insert_at_position(15, 2)
    dll.display_forward()  # 5 <-> 10 <-> 15 <-> 20 <-> 30
    
    print("\n=== Searching for 20 ===")
    position = dll.search(20)
    print(f"Found at position: {position}")
    
    print("\n=== Deleting first element ===")
    deleted = dll.delete_at_beginning()
    print(f"Deleted: {deleted}")
    dll.display_forward()  # 10 <-> 15 <-> 20 <-> 30
    
    print("\n=== Deleting last element ===")
    deleted = dll.delete_at_end()
    print(f"Deleted: {deleted}")
    dll.display_forward()  # 10 <-> 15 <-> 20
    
    print("\n=== Deleting by value (15) ===")
    dll.delete_by_value(15)
    dll.display_forward()  # 10 <-> 20
    
    print("\n=== Reversing the list ===")
    dll.reverse()
    print("Forward: ", end="")
    dll.display_forward()  # 20 <-> 10
    print("Backward: ", end="")
    dll.display_backward()  # 10 <-> 20
