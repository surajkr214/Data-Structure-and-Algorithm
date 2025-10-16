# Queues

## Overview
A queue is a linear data structure that follows the First In First Out (FIFO) principle. The first element inserted is the first one to be removed.

## Key Operations
- **Enqueue**: Add an element to the rear - O(1)
- **Dequeue**: Remove an element from the front - O(1)
- **Front/Peek**: View the front element - O(1)
- **isEmpty**: Check if queue is empty - O(1)

## Types of Queues
1. **Simple Queue**: Basic FIFO queue
2. **Circular Queue**: Last position connects to first
3. **Priority Queue**: Elements have priorities
4. **Deque**: Double-ended queue (insertion/deletion at both ends)

## Applications
1. CPU scheduling
2. Disk scheduling
3. Print queue
4. Breadth-First Search (BFS)
5. Handling of interrupts

## Files in this directory
- `queue_implementation.py`: Queue using list and collections.deque
- `circular_queue.py`: Circular queue implementation
