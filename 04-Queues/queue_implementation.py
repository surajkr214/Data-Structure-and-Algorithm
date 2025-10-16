"""
Queue Implementation
Demonstrates FIFO (First In First Out) data structure.
"""

from collections import deque


class Queue:
    """Queue implementation using Python's deque for efficiency."""
    
    def __init__(self):
        self.items = deque()
    
    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0
    
    def enqueue(self, item):
        """
        Add an item to the rear of the queue.
        Time Complexity: O(1)
        """
        self.items.append(item)
    
    def dequeue(self):
        """
        Remove and return the front item from the queue.
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.popleft()
    
    def front(self):
        """
        Return the front item without removing it.
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]
    
    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)
    
    def display(self):
        """Display the queue contents."""
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue (front to rear):", list(self.items))


class CircularQueue:
    """Circular Queue implementation using a fixed-size list."""
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
        self.count = 0
    
    def is_empty(self):
        """Check if the queue is empty."""
        return self.count == 0
    
    def is_full(self):
        """Check if the queue is full."""
        return self.count == self.capacity
    
    def enqueue(self, item):
        """Add an item to the queue."""
        if self.is_full():
            raise OverflowError("Queue is full")
        
        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        
        self.queue[self.rear] = item
        self.count += 1
    
    def dequeue(self):
        """Remove and return the front item from the queue."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        item = self.queue[self.front]
        
        if self.front == self.rear:
            # Queue becomes empty
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        
        self.count -= 1
        return item
    
    def peek(self):
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[self.front]
    
    def size(self):
        """Return the number of items in the queue."""
        return self.count
    
    def display(self):
        """Display the queue contents."""
        if self.is_empty():
            print("Queue is empty")
            return
        
        elements = []
        i = self.front
        for _ in range(self.count):
            elements.append(self.queue[i])
            i = (i + 1) % self.capacity
        
        print("Circular Queue (front to rear):", elements)


def hot_potato_game(names, num):
    """
    Simulate the Hot Potato game using a queue.
    
    Args:
        names: List of player names
        num: Number of passes before elimination
    
    Returns:
        Name of the winner
    """
    queue = Queue()
    
    # Add all names to the queue
    for name in names:
        queue.enqueue(name)
    
    # Continue until only one person remains
    while queue.size() > 1:
        # Pass the potato num times
        for _ in range(num):
            queue.enqueue(queue.dequeue())
        
        # Eliminate the person holding the potato
        eliminated = queue.dequeue()
        print(f"{eliminated} is eliminated")
    
    return queue.dequeue()


# Example usage
if __name__ == "__main__":
    # Basic queue operations
    print("=== Basic Queue Operations ===")
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.display()
    
    print(f"Front element: {q.front()}")
    print(f"Dequeued: {q.dequeue()}")
    q.display()
    print(f"Size: {q.size()}")
    
    # Circular queue
    print("\n=== Circular Queue Operations ===")
    cq = CircularQueue(5)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    cq.display()
    
    print(f"Dequeued: {cq.dequeue()}")
    cq.enqueue(4)
    cq.enqueue(5)
    cq.enqueue(6)
    cq.display()
    
    # Hot Potato game
    print("\n=== Hot Potato Game ===")
    players = ["Alice", "Bob", "Charlie", "David", "Eve"]
    winner = hot_potato_game(players, 3)
    print(f"Winner: {winner}")
