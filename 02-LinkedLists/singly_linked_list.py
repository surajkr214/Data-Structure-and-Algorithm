"""
Singly Linked List Implementation
A linear data structure where each node points to the next node.
"""


class Node:
    """A node in the singly linked list."""
    
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    """Singly Linked List with common operations."""
    
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        """Check if the list is empty."""
        return self.head is None
    
    def insert_at_beginning(self, data):
        """
        Insert a new node at the beginning of the list.
        Time Complexity: O(1)
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self, data):
        """
        Insert a new node at the end of the list.
        Time Complexity: O(n)
        """
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
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
        
        new_node.next = current.next
        current.next = new_node
    
    def delete_at_beginning(self):
        """
        Delete the first node from the list.
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("List is empty")
        
        deleted_data = self.head.data
        self.head = self.head.next
        return deleted_data
    
    def delete_at_end(self):
        """
        Delete the last node from the list.
        Time Complexity: O(n)
        """
        if self.is_empty():
            raise IndexError("List is empty")
        
        if self.head.next is None:
            deleted_data = self.head.data
            self.head = None
            return deleted_data
        
        current = self.head
        while current.next.next:
            current = current.next
        
        deleted_data = current.next.data
        current.next = None
        return deleted_data
    
    def delete_by_value(self, value):
        """
        Delete the first node with the given value.
        Time Complexity: O(n)
        """
        if self.is_empty():
            raise ValueError("List is empty")
        
        if self.head.data == value:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
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
        prev = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
    
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
    
    def display(self):
        """Display the linked list."""
        if self.is_empty():
            print("List is empty")
            return
        
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print(" -> ".join(elements))


# Example usage
if __name__ == "__main__":
    # Create a linked list
    ll = SinglyLinkedList()
    
    print("Inserting elements...")
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_at_beginning(5)
    ll.display()  # 5 -> 10 -> 20 -> 30
    
    print(f"\nLength: {ll.get_length()}")
    
    print("\nInserting 15 at position 2...")
    ll.insert_at_position(15, 2)
    ll.display()  # 5 -> 10 -> 15 -> 20 -> 30
    
    print("\nSearching for 20...")
    position = ll.search(20)
    print(f"Found at position: {position}")
    
    print("\nDeleting first element...")
    deleted = ll.delete_at_beginning()
    print(f"Deleted: {deleted}")
    ll.display()  # 10 -> 15 -> 20 -> 30
    
    print("\nDeleting by value (15)...")
    ll.delete_by_value(15)
    ll.display()  # 10 -> 20 -> 30
    
    print("\nReversing the list...")
    ll.reverse()
    ll.display()  # 30 -> 20 -> 10
